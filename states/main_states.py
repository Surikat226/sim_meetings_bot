from aiogram.fsm.state import State, StatesGroup


class MainStates(StatesGroup):
    """
    Здесь хранятся основные состояния бота
    """
    main_menu = State()
    riding_menu = State()
    who_is_near_menu = State()
    get_location_menu = State()
