from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from app.utils.static_data import FilterTexts


user_location_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=FilterTexts.send_geo, request_location=True)],
        [KeyboardButton(text=FilterTexts.back)]
    ],
    resize_keyboard=True
)
