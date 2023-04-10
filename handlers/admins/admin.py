from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from commands.admins import Commands
from filters.admin import AdminFilter
from keyboards.reply import ADMIN_KEYBOARDS
from models import Users


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
    await state.update_data(product_amount=1)


def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(
        admin_start, AdminFilter(), text=["!start", "/start", Commands.come_back.value]
    )