from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from const_texts import c_cancel


def make_buttons(words: list, row_width: int = 1) -> ReplyKeyboardMarkup:
    buttons_group = ReplyKeyboardMarkup(
        row_width=row_width, resize_keyboard=True)
    for word in words:
        if word is not None:
            buttons_group.insert(KeyboardButton(text=word))
    return buttons_group
