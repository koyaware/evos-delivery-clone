from aiogram import Dispatcher

from .admin import register_admin_handlers


def register_all_admin_handlers(dp: Dispatcher):
    register_admin_handlers(dp)