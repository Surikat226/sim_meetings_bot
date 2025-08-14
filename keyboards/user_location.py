from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


user_location_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📍 Отправить геопозицию", request_location=True)]
    ],
    resize_keyboard=True
)
