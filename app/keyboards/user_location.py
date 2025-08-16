from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from app.utils.static_data import FilterTexts


user_location_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=FilterTexts.back)]
    ],
    resize_keyboard=True
)
