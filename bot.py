!pip install aiogram -q
from aiogram import Bot, Dispatcher, types
import logging
import asyncio
import sys

API_TOKEN = ''
logging.basicConfig(level=logging.INFO)
dp = Dispatcher()

async def main():
   bot = Bot(token=API_TOKEN)
   await dp.start_polling(bot)

if __name__ == "__main__":
  await main()

!wget https://raw.githubusercontent.com/vifirsanova/compling/refs/heads/main/tasks/task3/faq.json

import json

with open('faq.json', encoding='utf-8') as f:
  data = json.load(f)

data

from aiogram.filters import Command

dp = Dispatcher()

@dp.message(Command("start", "help"))
async def send_welcome(message: types.Message):
  await message.answer("Привет! Я бот, который может отвечать на частые вопросы.")

@dp.message()
async def answer_faq(message: types.Message):
  text = message.text.lower()
  response = faq.get(text, "Я не знаю ответа на этот вопрос.")
  await message.answer(response)

async def main():
    bot = Bot(token=API_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    await main()

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
dp = Dispatcher()
kb = [
    [
        KeyboardButton(text="О компании"),
        KeyboardButton(text="Связаться с оператором")
     ]
]
keyboard = ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,
    input_field_placeholder="Выберите действие"
    )
@dp.message(Command("start"))
async def start_command(message: types.Message):
  await message.answer("С чем вам помочь?", reply_markup=keyboard)

@dp.message(lambda message: message.text == "О компании")
async def about_bot(message: types.Message):
  await message.answer("Наша компания занимается доставкой товаров по всей стране.")

@dp.message(lambda message: message.text == "Связаться с оператором")
async def about_bot(message: types.Message):
  await message.answer("Перевожу на оператора...")

async def main():
    bot = Bot(token=API_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    await main()
