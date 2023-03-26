from aiogram import types
from aiogram.dispatcher import FSMContext

from const_texts import c_contact, c_contact_message, c_cancel, c_send_admin_succsess
from loader import dp, bot

from robot.states.admin_message import Contact
from robot.keyboards.default import make_buttons
from robot.models import Message, TelegramUser
from core.settings import ADMINS_LIST


@dp.message_handler(text=c_contact)
async def bot_help(message: types.Message):
    await message.answer(
        text=c_contact_message
    )
    await Contact.admin_message.set()


@dp.message_handler(state=Contact.admin_message)
async def bot_help(message: types.Message, state: FSMContext):
    admin_message = message.text
    full_name = message.from_user.full_name
    user_id = message.from_user.id
    user_name = message.from_user.username
    user = await TelegramUser.objects.aget(tg_id=user_id)

    admin_full_message = f"Ismi: {full_name}\n" \
        f"User ID: {user_id}\n" \
        f"Username: {user_name}\n\n" \
        f"Xabar: {admin_message}"

    for admin in ADMINS_LIST:
        await bot.send_message(
            chat_id=admin,
            text=admin_full_message
        )

    await bot.send_message(
        chat_id=user_id,
        text=c_send_admin_succsess,
        reply_markup=make_buttons(c_cancel)
    )
    await Message.objects.acreate(
        user=user,
        message=admin_message
    )

    await state.finish()
