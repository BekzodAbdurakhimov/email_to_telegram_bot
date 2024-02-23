import asyncio
from telegram import Bot


async def main():
    # Укажите токен вашего бота
    bot_token = '6452119678:AAGMhU7raXCiqjIttu6ntt30UXyR44pFTQ4'

    # Укажите ID вашей группы
    group_id = 1002016969091

    # Инициализация бота
    bot = Bot(token=bot_token)

    # Отправка сообщения в группу
    await bot.send_message(chat_id=group_id, text='message!')


# Запуск асинхронной функции
asyncio.run(main())
