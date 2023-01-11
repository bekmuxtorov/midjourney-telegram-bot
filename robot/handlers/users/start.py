import logging

from asgiref.sync import sync_to_async
from robot.models import TelegramUser

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot
from const_texts import c_get_hello, c_about_us, c_create, c_example, c_contact
from robot.keyboards.default import make_buttons


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    telegram_user, _ = await TelegramUser.objects.aget_or_create(
        full_name=message.from_user.full_name,
        username=message.from_user.username,
        tg_id=message.from_user.id,
        chat_id=message.chat.id,
    )
    logging.info("New user")
    chat_id = message.from_user.id
    await bot.send_animation(
        chat_id=chat_id,
        animation="https://t.me/sinovuchun4101/15",
        caption=c_get_hello(message.from_user.full_name),
        reply_markup=make_buttons(
            words=[c_create, c_example, c_contact],
            row_width=2
        )
    )
