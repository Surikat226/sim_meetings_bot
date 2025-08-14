from aiogram import types
from aiogram.fsm.context import FSMContext
from keyboards.user_location import user_location_kb
from states.main_states import MainStates


async def riding_now(message: types.Message, state: FSMContext):
    """
    Кнопка "🚴 Я катаюсь"
    """
    await message.answer(
        "Отправь свою геопозицию (можно в реальном времени), чтобы другие могли тебя найти.",
        reply_markup=user_location_kb
    )
    await state.set_state(MainStates.riding_menu)
