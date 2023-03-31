from aiogram import Dispatcher
from aiogram.types import Message

from commands.admins import Commands
from models import Cart, CartProducts, Products


async def my_cart(message: Message):
    users: Cart = await Cart.query.where(
        Cart.user_id == message.from_user.id
    ).gino.all()
    if not users:
        await message.answer("Ваша корзина пуста!")
    for user in users:
        carts: CartProducts = await CartProducts.query.where(
            CartProducts.cart_id == user.Id
        ).gino.all()
        if not carts:
            await message.answer("Ваша корзина пуста!")
        for cart in carts:
            products: Products = await Products.query.where(
                Products.Id == cart.products_id
            ).gino.all()
            if not products:
                await message.answer("Ваша корзина пуста!")
            for product in products:
                await message.bot.send_message(message.from_user.id, f"У вас в корзине: <b>{product.name}</b>\n\n"
                                                                     f"Стоимость: <b>{product.price}</b>")


def register_my_cart_handlers(dp: Dispatcher):
    dp.register_message_handler(
        my_cart, text=Commands.my_cart.value
    )