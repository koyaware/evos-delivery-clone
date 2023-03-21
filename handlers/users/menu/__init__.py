from aiogram import Dispatcher

from handlers.users.menu.show_lavash import register_lavash_handler
from handlers.users.menu.show_set import register_set_handler


def register_all_menu_handlers(dp: Dispatcher):
    register_set_handler(dp)
    register_lavash_handler(dp)