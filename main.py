from aiogram import Bot, Dispatcher, types, executor
import random
import decouple
from config import token

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"Я загадал число от 1 до 3 угадайте {message.from_user.full_name}!")

@dp.message_handler()
async def guess_number(message:types.Message):
    user_number = message.text.strip()
    if not user_number.isdigit:
        await message.answer("Введите только число пожалуйста")

    user_number = int(user_number)
    bot_number = random.randint(1, 3)

    if user_number == bot_number:
        await message.answer("Правильно! Вы отгадали!")
    else:
        await message.answer(f"Неправильно! Я загадал число {bot_number}")


if __name__ == '__main__':
    executor.start_polling(dp)

    