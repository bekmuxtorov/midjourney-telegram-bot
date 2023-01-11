from aiogram.dispatcher.filters.state import StatesGroup, State


class Contact(StatesGroup):
    admin_message = State()
    send_admin = State()
