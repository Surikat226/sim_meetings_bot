from aiogram import types
from aiogram.fsm.context import FSMContext
from keyboards.main_menu import main_menu_kb
from states.main_states import MainStates


async def cmd_start(message: types.Message, state: FSMContext):
    """
    /start — приветственное сообщение
    """
    await message.answer(
        f"Привет, {message.from_user.first_name}! 🚀\n"
        "Я помогу тебе находить других райдеров поблизости.\n"
        "Выбери действие ниже:",
        reply_markup=main_menu_kb
    )
    await state.set_state(MainStates.main_menu)
