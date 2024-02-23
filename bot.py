import telebot
import imaplib

# Замените эти значения своими
BOT_TOKEN = "6452119678:AAGMhU7raXCiqjIttu6ntt30UXyR44pFTQ4"
GROUP_ID = -123456789
GMAIL_EMAIL = "YOUR_GMAIL_EMAIL"
GMAIL_PASSWORD = "YOUR_GMAIL_PASSWORD"

# Подключение к Telegram-боту
bot = telebot.TeleBot(BOT_TOKEN)

# Подключение к Gmail
client = imaplib.IMAP4_SSL("imap.gmail.com", 993)
client.login(GMAIL_EMAIL, GMAIL_PASSWORD)


# Функция для обработки сообщений
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "This bot scraps data from email and sends it to the telegram group")


@bot.message_handler(commands=["get_emails"])
def get_emails(message):
    # Получение писем из Gmail
    client.select("inbox")
    status, emails = client.search(None, "ALL")
    if status == "OK":
        for email_id in emails[0].split():
            status, email_data = client.fetch(email_id, "(RFC822)")
            if status == "OK":
                # Обработка данных письма
                message_text = email_data[0][1].decode("utf-8")
                # Отправка данных в Telegram-группу
                bot.send_message(GROUP_ID, message_text)


# Запуск бота
bot.polling()

