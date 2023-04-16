from aiogram import Dispatcher
from aiogram.types import Message

from commands.admins import AdminCommands
from filters import AdminFilter
from keyboards.reply import ADMIN_ORDER_CHOOSE_KEYBOARDS


async def users_orders(message: Message):
    await message.answer("Выберите вариант: ", reply_markup=ADMIN_ORDER_CHOOSE_KEYBOARDS)


def register_user_orders_choose_handlers(dp: Dispatcher):
    dp.register_message_handler(
        users_orders, AdminFilter(), text=AdminCommands.user_orders.value
    )