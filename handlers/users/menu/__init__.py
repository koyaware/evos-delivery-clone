from aiogram import Dispatcher

from handlers.users.menu.show_burger import register_burger_handler
from handlers.users.menu.show_hot_dog import register_hot_dog_handler
from handlers.users.menu.show_lavash import register_lavash_handler
from handlers.users.menu.show_set import register_set_handler
from handlers.users.menu.show_shawarma import register_shawarma_handler


def register_all_menu_handlers(dp: Dispatcher):
    register_set_handler(dp)
    register_lavash_handler(dp)
    register_shawarma_handler(dp)
    register_burger_handler(dp)
    register_hot_dog_handler(dp)