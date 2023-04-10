from aiogram import Dispatcher
from aiogram.types import Message

from commands.admins import MyCartCommands
from keyboards.reply import MY_CART_KEYBOARDS
from models import Users


async def order_time(message: Message):
    is_user = await Users.query.where(
        Users.is_user == True
    ).gino.all()
    if not is_user:
        return await message.answer("У вас нет прав!\nВы забанены!")
    await message.answer("Примерное время доставки: <b>30 минут</b>.", reply_markup=MY_CART_KEYBOARDS)


def register_order_time_handlers(dp: Dispatcher):
    dp.register_message_handler(
        order_time, text=MyCartCommands.order_time.value
    )