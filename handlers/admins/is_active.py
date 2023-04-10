from aiogram import Dispatcher
from aiogram.types import Message

from commands.admins import AdminCommands
from filters import AdminFilter
from models import Users


async def is_active(message: Message):
    users: Users = await Users.query.where(
        Users.tg_id == Users.tg_id
    ).gino.all()
    if not users:
        return await message.answer("Пользователей не найдено!")
    is_users = []
    for user in users:
        is_users.append(f'ID Пользователя: {user.tg_id}')
        is_users.append(f'Не судимый: {user.is_user}\n')
    await message.bot.send_message(message.from_user.id, f"<b>{chr(10).join([str(i) for i in is_users])}</b>\n")


def register_is_active_handlers(dp: Dispatcher):
    dp.register_message_handler(
        is_active, AdminFilter(), text=AdminCommands.is_active.value
    )