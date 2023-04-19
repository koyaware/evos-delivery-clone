from aiogram import Dispatcher

from handlers.users.settings.change_name import register_change_user_name_handlers
from handlers.users.settings.settings import register_user_settings_handlers


def register_all_settings_handlers(dp: Dispatcher):
    register_user_settings_handlers(dp)
    register_change_user_name_handlers(dp)