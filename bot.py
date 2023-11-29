import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from config import TOKEN
from transcriptor import transcript
import asyncio

logging.basicConfig(filename='logs.txt', level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
# TOKEN = os.getenv('TOKEN')
bot = Bot(token = TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

@dp.message(CommandStart())
async def cmd_start(msg: types.Message):
 
    await msg.answer(text = f'Enter your name is cyryllic letters:')


@dp.message()
async def message(msg: types.Message):
    user_name = msg.from_user.first_name
    user_msg = transcript(msg.text)
    await msg.answer(text = f'Hello, {user_name}, your transcribed name is: {user_msg}')

async def main() -> None:
    bot = Bot(token = TOKEN)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
