from aiogram import Dispatcher

from handlers.admins.user_orders.order_list import register_user_orders_list_handlers
from handlers.admins.user_orders.user_orders_choose import register_user_orders_choose_handlers


def register_all_user_orders_handlers(dp: Dispatcher):
    register_user_orders_choose_handlers(dp)
    register_user_orders_list_handlers(dp)