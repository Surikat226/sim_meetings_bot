from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from app.keyboards.main_menu import main_menu_kb
from app.states.main_states import MainStates
from ...utils.static_data import FilterTexts


back_to_main_from_sub_router = Router()


@back_to_main_from_sub_router.message(F.text == FilterTexts.back)
async def back_to_main_from_sub(message: types.Message, state: FSMContext):
    """
    Хендлер для возврата в главное меню из сабменю
    """
    # FIXME Если возможно, избавиться от текста и просто возвращать юзера обратно
    await message.answer("Вернулись в главное меню!", reply_markup=main_menu_kb)
    await state.set_state(MainStates.main_menu)
