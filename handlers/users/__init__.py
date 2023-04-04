from aiogram import Dispatcher

from .carts import register_all_carts_handlers
from .menu import register_all_menu_handlers
from .user import register_user_handlers


def register_all_user_handlers(dp: Dispatcher):
    register_user_handlers(dp)
    register_all_menu_handlers(dp)
    register_all_carts_handlers(dp)