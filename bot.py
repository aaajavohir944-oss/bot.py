import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎬 Anime"), KeyboardButton(text="🤖 AI Yordamchi")],
        [KeyboardButton(text="🔍 Qidiruv"), KeyboardButton(text="⭐ Sevimlilar")]
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Xush kelibsiz AniAI Hub botga 👋", reply_markup=menu)

@dp.message()
async def menu_handler(message: types.Message):
    await message.answer("Bu tugma hali ishlab chiqilmoqda 🚧")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
