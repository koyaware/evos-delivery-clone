from aiogram import Dispatcher
from aiogram.types import Message

from commands.admins import Commands
from filters.admin import UserFilter
from keyboards.reply import SETTINGS_KEYBOARD


async def user_settings(message: Message):
    await message.answer("Выберите команду: ", reply_markup=SETTINGS_KEYBOARD)


def register_user_settings_handlers(dp: Dispatcher):
    dp.register_message_handler(
        user_settings, UserFilter(), text=Commands.settings.value
    )