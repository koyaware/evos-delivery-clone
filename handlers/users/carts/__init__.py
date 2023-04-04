from aiogram import Dispatcher

from handlers.users.carts.cart import register_my_cart_handlers
from handlers.users.carts.delete_cart import register_delete_cart_handlers


def register_all_carts_handlers(dp: Dispatcher):
    register_my_cart_handlers(dp)
    register_delete_cart_handlers(dp)