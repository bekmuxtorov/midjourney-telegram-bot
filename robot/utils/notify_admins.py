import logging

from aiogram import Dispatcher

from django.conf import settings


async def on_startup_notify(dp: Dispatcher):
    for admin in settings.ADMINS_LIST:
        try:
            await dp.bot.send_message(admin, "Bot ishga tushirildi")

        except Exception as err:
            logging.exception(err)
