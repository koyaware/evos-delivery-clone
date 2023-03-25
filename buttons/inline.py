from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram.utils.callback_data import CallbackData

# cart_cb = CallbackData('cart', 'action', 'amount')

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Добавить в корзину 🗑️', callback_data='add_item'),
     InlineKeyboardButton('Удалить с корзины ❌', callback_data='remove_item')],
    [InlineKeyboardButton('+', callback_data='plus_item'),
     InlineKeyboardButton('-', callback_data='minus_item')]
])