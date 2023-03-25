from aiogram import Dispatcher

from .admins import register_all_admin_handlers
from .callback import register_all_callback_handlers
from .users import register_all_user_handlers


def register_all_handlers(dp: Dispatcher):
    register_all_admin_handlers(dp)
    register_all_user_handlers(dp)
    register_all_callback_handlers(dp)