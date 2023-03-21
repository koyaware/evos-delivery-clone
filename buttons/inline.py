from aiogram import types
from aiogram.utils.callback_data import CallbackData

cart_cb = CallbackData('cart', 'action', 'amount')


def get_keyboard(amount):
    return types.InlineKeyboardMarkup().row(
        types.InlineKeyboardButton("Добавить в корзину 🗑️", callback_data=cart_cb.new(action='add_item',
                                                                                      amount=amount)),
        types.InlineKeyboardButton("Удалить с корзины 🗑️", callback_data=cart_cb.new(action='remove_item',
                                                                                     amount=amount)))