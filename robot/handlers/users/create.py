from aiogram import types
from aiogram.dispatcher import FSMContext

from asgiref.sync import sync_to_async
from .midjourney import draw_picture
from loader import dp, bot
from const_texts import c_create, c_example, c_contact, c_create_description, c_create_image, c_example_get_caption, c_error_words, c_block_words
from robot.states import CreateImage
from robot.keyboards.default import make_buttons

from robot.models import Permission, TelegramUser, Request

from datetime import datetime, timezone


@dp.message_handler(text=c_create)
async def bot_echo(message: types.Message):
    await CreateImage.create_image.set()
    await message.answer(text=c_create_description)


@dp.message_handler(state=CreateImage.create_image)
async def bot_echo(message: types.Message, state: FSMContext):
    user = await TelegramUser.objects.aget(tg_id=message.from_user.id)

    admin_permission_lang = await Permission.objects.aget(name='googletrans')
    admin_permission_midjourney = await Permission.objects.aget(name='midjourney')

    input = message.text.lower().strip()

    request_count = await Request.objects.filter(user=user).acount()
    if request_count <= 3:
        await message.answer(
            text=c_create_image
        )
        result = draw_picture(
            admin_permission_midjourney=admin_permission_midjourney.permission_status,
            admin_permission_lang=admin_permission_lang.permission_status,
            input=input
        )[0]
        await bot.send_photo(
            chat_id=message.from_user.id,
            photo=result,
            caption=c_example_get_caption(input),
            reply_markup=make_buttons(
                words=[c_create, c_example, c_contact],
                row_width=2
            )
        )
        await state.finish()
        await sync_to_async(user.set_request_count)()
        await Request.objects.acreate(user=user)

    else:
        result = None
        await message.answer(
            text=c_block_words
        )
        await state.finish()
        return
