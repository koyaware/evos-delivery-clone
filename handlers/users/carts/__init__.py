from aiogram import Dispatcher

from handlers.users.carts.cart import register_my_cart_handlers
from handlers.users.carts.delete_cart import register_delete_cart_handlers
from handlers.users.carts.order_time import register_order_time_handlers
from handlers.users.carts.send_order import register_send_order_handlers


def register_all_carts_handlers(dp: Dispatcher):
    register_my_cart_handlers(dp)
    register_delete_cart_handlers(dp)
    register_order_time_handlers(dp)
    register_send_order_handlers(dp)