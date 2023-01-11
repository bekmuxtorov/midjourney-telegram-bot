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

# Echo bot


@ dp.message_handler(text=c_create)
async def bot_echo(message: types.Message):
    await CreateImage.create_image.set()
    await message.answer(text=c_create_description)


@ dp.message_handler(state=CreateImage.create_image)
async def bot_echo(message: types.Message, state: FSMContext):
    await CreateImage.create_image.set()
    tg_id = message.from_user.id
    user = await TelegramUser.objects.aget(tg_id=tg_id)
    admin_permission_lang = await Permission.objects.aget(name='admin_permission_lang')
    admin_permission_midjourney = await Permission.objects.aget(name='admin_permission_midjourney')
    print('='*20)
    print(f'User: {user}')
    print(f'admin_permission_lang: {admin_permission_lang.permission_status}')
    print(
        f'admin_permission_midjourney: {admin_permission_midjourney.permission_status}')
    print('='*20)
    input = message.text.lower().strip()
    filtered_queryset = await sync_to_async(Request.objects.filter)(user=user)
    filtered_queryset = list(filtered_queryset)

    try:
        delta = datetime.now(timezone.utc) - filtered_queryset[-2].create_add
        print(delta)

        if delta.seconds > 43200:
            await message.answer(
                text=c_create_image
            )
            result = draw_picture(
                admin_permission_midjourney=admin_permission_midjourney.permission_status,
                admin_permission_lang=admin_permission_lang.permission_status,
                input=input
            )[0]

        else:
            result = None
            msg = c_block_words
    except Exception:
        try:
            await message.answer(
                text=c_create_image
            )
            result = draw_picture(
                admin_permission_midjourney=admin_permission_midjourney.permission_status,
                admin_permission_lang=admin_permission_lang.permission_status,
                input=input
            )[0]
        except Exception:
            result = None
            msg = c_error_words

    print(result)
    if result:
        await bot.send_photo(
            chat_id=tg_id,
            photo=result,
            caption=c_example_get_caption(input),
            reply_markup=make_buttons(
                words=[c_create, c_example, c_contact],
                row_width=2
            )
        )
        print(f"User: {user}")
        await state.finish()

        await Request.objects.acreate(user=user)

    elif msg:
        await message.answer(
            text=msg
        )

    await sync_to_async(user.set_request_count)()
    print('Status: Yaratildi')
    await state.finish()
