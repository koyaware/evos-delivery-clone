from aiogram import Dispatcher
from aiogram.types import Message

from commands.admins import MyCartCommands
from filters.admin import CartFilter, UserFilter
from keyboards.reply import MY_CART_KEYBOARDS


async def order_time(message: Message):
    await message.answer("Примерное время доставки: <b>30 минут</b>.", reply_markup=MY_CART_KEYBOARDS)


def register_order_time_handlers(dp: Dispatcher):
    dp.register_message_handler(
        order_time, UserFilter(), CartFilter(), text=MyCartCommands.order_time.value
    )