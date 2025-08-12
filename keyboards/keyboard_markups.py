from aiogram.types import ReplyKeyboardMarkup
from keyboards import main_menu_kb, user_location_kb


def get_main_menu_kb() -> ReplyKeyboardMarkup:
    """
    Возвращает клавиатуру главного меню
    """

    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=main_menu_kb
    )
    return keyboard


def get_user_location_kb() -> ReplyKeyboardMarkup:
    """
    Возвращает клавиатуру отправки геопозиции пользователя
    """

    keyboard = ReplyKeyboardMarkup(
        keyboard=user_location_kb,
        resize_keyboard=True
    )
    return keyboard
