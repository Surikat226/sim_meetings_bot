from aiogram import types
from aiogram.fsm.context import FSMContext
from states.main_states import MainStates


async def who_is_near(message: types.Message, state: FSMContext):
    """
    Кнопка "📍 Кто рядом"
    """
    await message.answer("Функция 'Кто рядом' скоро будет доступна! 😉")
    await state.set_state(MainStates.who_is_near_menu)
