from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from app.keyboards.user_location import user_location_kb
from app.states.main_states import MainStates
from app.utils.static_data import FilterTexts
from app.utils.logging import log_handler


riding_now_router = Router()


@riding_now_router.message(F.text == FilterTexts.im_riding)
@log_handler
async def riding_now(message: types.Message, state: FSMContext):
    """
    Кнопка "🚴 Я катаюсь". Должна переводить пользователя в режим показа своей текущей геолокации другим пользователям
    """

    await message.answer(
        "Чтобы поделиться live-локацией:\n"
        "1. Нажми 📎 (скрепка) → «Геопозиция»\n"
        "2. Выбери «Транслировать свою геопозицию в реальном времени»\n"
        "3. Укажи время трансляции\n"
        "4. Отправь её сюда 🚴",
        reply_markup=user_location_kb
    )
    await state.set_state(MainStates.riding_menu)
