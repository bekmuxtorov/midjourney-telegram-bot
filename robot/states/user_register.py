from aiogram.dispatcher.filters.state import StatesGroup, State


class UserRegister(StatesGroup):
    username = State()
    first_name = State()
    last_name = State()
    password = State()
