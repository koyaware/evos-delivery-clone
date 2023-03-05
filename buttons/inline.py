from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TRASH = InlineKeyboardButton("Добавить в корзину 🗑️", callback_data="add_to_trash")


keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("-", callback_data="remove_item"),
            TRASH,
            InlineKeyboardButton("+", callback_data="add_item")
        ]
    ]
)