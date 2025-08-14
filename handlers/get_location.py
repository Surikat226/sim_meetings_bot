from aiogram import types
from aiogram.fsm.context import FSMContext
from keyboards.main_menu import main_menu_kb
from states.main_states import MainStates


async def get_location(message: types.Message, state: FSMContext):
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
    await state.set_state(MainStates.get_location_menu)
