from aiogram import Dispatcher

from .admin import register_admin_handlers
from .is_active import register_is_active_handlers
from .user_orders import register_all_user_orders_handlers


def register_all_admin_handlers(dp: Dispatcher):
    register_admin_handlers(dp)
    register_is_active_handlers(dp)
    register_all_user_orders_handlers(dp)