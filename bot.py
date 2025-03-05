!pip install aiogram -q
from aiogram import Bot, Dispatcher, types  # Основные классы для работы с ботом
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # Импортируем необходимые классы
import logging  # Логирование для отслеживания работы бота
import asyncio  # Модуль для работы с асинхронным кодом

API_TOKEN = ''  

# Настраиваем логирование
logging.basicConfig(level=logging.INFO)

# Создаем объект бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

!wget https://raw.githubusercontent.com/vifirsanova/compling/refs/heads/main/tasks/task3/faq.json
import json

with open('faq.json', encoding='utf-8') as f:
  data = json.load(f)

data

faq_keywords = {
    "цены": "цены, стоимость, заказ, оплата",
    "часы работы": "часы работы, время работы, доступность",
    "доставка": "доставка, сроки доставки, стоимость доставки, отслеживание",
    "возврат": "возврат, обмен, возврат товара, гарантия",
    "контакты": "связаться, телефон, email, адрес"
}

# Определение клавиатуры
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
    await message.answer("Здравствуйте! Чем я могу вам помочь?", reply_markup=keyboard)

@dp.message()
async def answer_faq(message: types.Message):
    text = message.text.lower()

    if text == "о компании":
        await message.answer("Наша компания занимается доставкой товаров по всей стране.")
        return
    elif text == "связаться с оператором":
        await message.answer("Перевожу на оператора...")
        return

    # Поиск ответа по ключевым словам
    response = "Я не знаю ответа на этот вопрос."
    for category, keywords in faq_keywords.items():
        if any(keyword in text for keyword in keywords.split(", ")):
            for item in data["faq"]:
                if category in item["question"].lower():
                    response = item["answer"]
                    break
            break

    await message.answer(response)

async def main():
    bot = Bot(token=API_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    await main()
