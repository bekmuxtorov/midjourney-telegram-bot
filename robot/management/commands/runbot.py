from django.core.management.base import BaseCommand, CommandError

from aiogram import executor

from loader import dp

from robot.middlewares import *
from robot.handlers import *

from robot.utils.notify_admins import on_startup_notify
from robot.utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)


class Command(BaseCommand):
    help = 'RUN COMMAND: python manage.py runbot'

    def handle(self, *args, **options):
        executor.start_polling(dp, on_startup=on_startup)
