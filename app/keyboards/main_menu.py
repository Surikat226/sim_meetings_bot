from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from app.utils.static_data import FilterTexts


main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=FilterTexts.im_riding)],
        [KeyboardButton(text=FilterTexts.whos_near)]
    ],
    resize_keyboard=True
)
