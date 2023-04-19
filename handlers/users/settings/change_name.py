from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from commands.admins import Commands
from filters.admin import UserFilter
from misc.states import UserNameState


async def user_name(message: Message):
    await UserNameState.name.set()
    await message.answer("Напишите имя: ")


async def change_user_name(callback: CallbackQuery):
    pass


def register_change_user_name_handlers(dp: Dispatcher):
    dp.register_message_handler(
        user_name, UserFilter(), text=Commands.change_name.value
    )
    dp.register_message_handler(
        change_user_name, UserFilter(), state=UserNameState.name
    )