from aiogram import Dispatcher

from handlers.users.user_auth.user_location import register_user_locations_handlers
from handlers.users.user_auth.user_ph_number import register_user_phone_numbers_handlers


def register_all_user_auths(dp: Dispatcher):
    register_user_phone_numbers_handlers(dp)
    register_user_locations_handlers(dp)