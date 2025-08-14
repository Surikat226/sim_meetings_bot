from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🚴 Я катаюсь")],
        [KeyboardButton(text="📍 Кто рядом")]
    ],
    resize_keyboard=True
)