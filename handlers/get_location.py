from aiogram import types
from keyboards.main_menu import main_menu_kb


async def get_location(message: types.Message):
    """
    Принимает геопозицию от пользователя
    """
    lat = message.location.latitude
    lon = message.location.longitude
    await message.answer(
        f"✅ Я получил твоё местоположение!\n"
        f"Широта: {lat}\nДолгота: {lon}",
        reply_markup=main_menu_kb
    )
