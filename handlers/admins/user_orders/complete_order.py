from aiogram import Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from commands.admins import AdminCommands
from filters import AdminFilter
from models import OrderHistory


async def order_complete(message: Message):
    orders: OrderHistory = await OrderHistory.query.where(
        OrderHistory.Id == OrderHistory.Id
    ).gino.all()
    if not orders:
        return await message.answer('Нет заказов!')
    for order in orders:
        inline_keyboard = InlineKeyboardMarkup()
        inline_keyboard.add(
            InlineKeyboardButton(f'🗙 {order.user_id}', callback_data=order.Id)
        )
    await message.answer("Заказы упорядочены по ID пользователям.",
                         reply_markup=inline_keyboard)


def register_user_order_complete_handlers(dp: Dispatcher):
    dp.register_message_handler(
        order_complete, AdminFilter(), text=AdminCommands.order_complete.value
    )