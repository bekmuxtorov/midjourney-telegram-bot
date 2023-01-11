from asgiref.sync import sync_to_async
from aiogram import types
from aiogram.types.input_file import InputFile

from loader import dp, bot
from const_texts import c_example, c_example_get_caption, c_create, c_contact, c_null_base
from robot.models import Example
from robot.keyboards.default import make_buttons


def get_image(image_url):
    return InputFile(path_or_bytesio=image_url)


@dp.message_handler(text=c_example)
async def bot_echo(message: types.Message):
    try:
        chat_id = message.from_user.id
        example_photos = await sync_to_async(list)(Example.objects.all())
        for indx, example_photo in enumerate(example_photos, start=1):
            await bot.send_photo(
                chat_id=chat_id,
                photo=get_image(example_photo.image.path),
                caption=c_example_get_caption(example_photo.description, indx),
                reply_markup=make_buttons(
                    words=[c_create, c_example, c_contact],
                    row_width=2
                )
            )

    except Exception:
        print('='*5 + c_null_base + '='*5)
        await message.answer(text=c_null_base)
