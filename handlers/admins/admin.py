from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from commands.admins import Commands
from filters.admin import AdminFilter
from keyboards.reply import ADMIN_KEYBOARDS
from models import Products, Users


async def admin_start(message: Message, state: FSMContext):
    await state.finish()
    users = await Users.query.where(
        Users.tg_id == message.from_user.id
    ).gino.first()
    if not users:
        await Users.create(tg_id=message.from_user.id)
    is_user = await Users.query.where(
        Users.is_user == True
    ).gino.all()
    if not is_user:
        await message.answer("У вас нет прав!")
        return
    await message.answer("Привет, админ! Выбери команду: ", reply_markup=ADMIN_KEYBOARDS)


async def is_active(message: Message):
    users: Users = await Users.query.where(
        Users.tg_id == Users.tg_id
    ).gino.all()
    if not users:
        await message.answer("Пользователей не найдено!")
        return
    for user in users:
        await message.bot.send_message(message.from_user.id, f"ID Пользователя: <b>{user.tg_id}</b>\n"
                                                             f"Не судимый: <b>{user.is_user}</b>")


def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(
        admin_start, AdminFilter(), commands=['start'], state='*', commands_prefix='!/'
    )
    dp.register_message_handler(
        is_active, AdminFilter(), text=Commands.is_active.value
    )