from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from app.states.main_states import MainStates
from ...utils.static_data import FilterTexts


who_is_near_router = Router()


@who_is_near_router.message(F.text == FilterTexts.whos_near)
async def who_is_near(message: types.Message, state: FSMContext):
    """
    Кнопка "📍 Кто рядом". Отображает пользователей поблизости, которые включили режим "Я катаюсь"
    """
    await message.answer("Функция 'Кто рядом' скоро будет доступна! 😉")
    await state.set_state(MainStates.who_is_near_menu)
