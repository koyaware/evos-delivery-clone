from aiogram import Dispatcher

from .callback import register_callback_handlers
from .menu import register_all_menu_handlers
from .user import register_user_handlers


def register_all_user_handlers(dp: Dispatcher):
    register_callback_handlers(dp)
    register_user_handlers(dp)
    register_all_menu_handlers(dp)