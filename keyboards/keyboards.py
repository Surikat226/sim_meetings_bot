from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_kb = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text="🚴 Я катаюсь")],
        [KeyboardButton(text="📍 Кто рядом")]
    ]
)

user_location_kb = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text="📍 Отправить геопозицию", request_location=True)]
    ]
)
