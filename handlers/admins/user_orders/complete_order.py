from aiogram import Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from commands.admins import AdminCommands
from filters import AdminFilter
from models import OrderHistory, Users


async def order_complete(message: Message):
    orders: OrderHistory = await OrderHistory.query.where(
        OrderHistory.Id == OrderHistory.Id
    ).gino.all()
    if not orders:
        return await message.answer('Нет заказов!')
    for order in orders:
        inline_keyboard = InlineKeyboardMarkup()
        users: Users = await Users.query.where(
            Users.tg_id == order.user_id
        ).gino.all()
        for user in users:
            inline_keyboard.add(
                InlineKeyboardButton(f'🗙 {user.phone_number}', callback_data=order.user_id)
            )
    await message.answer("Заказы упорядочены по ID пользователям.",
                         reply_markup=inline_keyboard)


def register_user_order_complete_handlers(dp: Dispatcher):
    dp.register_message_handler(
        order_complete, AdminFilter(), text=AdminCommands.order_complete.value
    )