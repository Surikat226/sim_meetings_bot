from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart
from app.keyboards.main_menu import main_menu_kb
from app.states.main_states import MainStates
from app.utils.logging import log_handler


start_router = Router()


@log_handler
@start_router.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext):
    """
    /start — Приветствует пользователя и показывает стартовое (главное) меню
    """

    await message.answer(
        f"Привет, {message.from_user.first_name}! 🚀\n"
        "Я помогу тебе находить других райдеров поблизости.\n"
        "Выбери действие ниже:",
        reply_markup=main_menu_kb
    )
    await state.set_state(MainStates.main_menu)
