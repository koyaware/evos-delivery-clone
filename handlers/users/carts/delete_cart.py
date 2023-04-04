from aiogram import Dispatcher
from aiogram.types import Message

from commands.admins import MyCartCommands
from keyboards.reply import USER_KEYBOARDS
from models import CartProducts


async def empty_the_trash(message: Message):
    cart = await CartProducts.query.where(
        CartProducts.Id == CartProducts.Id
    ).gino.all()
    if not cart:
        await message.answer("Ваша корзина пуста!")
    await CartProducts.delete.where(CartProducts.Id == CartProducts.Id).gino.status()
    await message.answer("Корзина успешно очищена!", reply_markup=USER_KEYBOARDS)


def register_delete_cart_handlers(dp: Dispatcher):
    dp.register_message_handler(
        empty_the_trash, text=MyCartCommands.delete_cart.value
    )