from aiogram import types
from aiogram.dispatcher import FSMContext

from robot.keyboards.default import make_buttons
from const_texts import c_create, c_example, c_contact, c_cancel
from loader import dp


# Echo bot
@dp.message_handler(text=c_cancel, state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text="Yaxshi. Ortga qaytamiz.",
        reply_markup=make_buttons(
            words=[c_create, c_example, c_contact],
            row_width=2
        )
    )
