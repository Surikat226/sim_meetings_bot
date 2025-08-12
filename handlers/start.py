from aiogram import types
from keyboards.keyboard_markups import get_main_menu_kb


async def cmd_start(message: types.Message):
    """
    /start — приветственное сообщение
    """
    await message.answer(
        f"Привет, {message.from_user.first_name}! 🚀\n"
        "Я помогу тебе находить других райдеров поблизости.\n"
        "Выбери действие ниже:",
        reply_markup=get_main_menu_kb()
    )
