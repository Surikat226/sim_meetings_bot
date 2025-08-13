from aiogram import types
from keyboards import user_location_kb


async def riding_now(message: types.Message):
    """
    Кнопка "🚴 Я катаюсь"
    """
    await message.answer(
        "Отправь свою геопозицию (можно в реальном времени), чтобы другие могли тебя найти.",
        reply_markup=user_location_kb
    )
