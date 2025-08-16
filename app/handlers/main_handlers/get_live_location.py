from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from app.states.main_states import MainStates
from app.utils.logging import log_handler


get_live_location_router = Router()


@log_handler
@get_live_location_router.message(F.location)
async def get_live_location(message: types.Message, state: FSMContext):
    """
    Принимает реалтайм-геопозицию от пользователя
    """
    loc = message.location
    if loc.live_period:  # Если есть live_period, значит это стрим
        await message.answer("✅ Отлично! Ты начал транслировать live-локацию 🚴")
        await state.set_state(MainStates.get_live_location_menu)
    else:
        await message.answer(
            "ℹ️ Ты отправил разовую точку - это не совсем то, что нужно :(\n"
            "Попробуй ещё раз отправить свою геопозицию в реальном времени (воспользуйся инструкцией выше)"
        )
