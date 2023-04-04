from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from commands.admins import Commands
from keyboards.reply import MY_CART_KEYBOARDS
from models import Cart, CartProducts, Products


async def my_cart(message: Message, state: FSMContext):
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
        product_keyboard = InlineKeyboardMarkup()
        product_name = []
        product_price = []
        for cart in carts:
            products: Products = await Products.query.where(
                Products.Id == cart.products_id
            ).gino.all()
            if not products:
                await message.answer("Ваша корзина пуста!")
            for product in products:
                product_keyboard.add(
                    InlineKeyboardButton(f'🗙 {product.name}', callback_data=product.Id)
                )
                product_name.append(cart.amount)
                product_name.append(product.name)
                product_price.append(product.price)
                price = sum(map(int, product_price))
        await message.bot.send_message(message.from_user.id,
                                       f"У вас в корзине: \n"
                                       f"<b>{chr(10).join([str(i) for i in product_name])}</b>\n\n"
                                       f"Стоимость: {price} сум.\n"
                                       f"Доставка: 10000 сум.\n"
                                       f"Общая сумма: <b>{price + 10000} сум.</b>",
                                       reply_markup=product_keyboard)
        await message.answer("Для удаления товара, вы можете нажать кнопку очистить корзину "
                             "или удалить выборочно выше.",
                             reply_markup=MY_CART_KEYBOARDS)


def register_my_cart_handlers(dp: Dispatcher):
    dp.register_message_handler(
        my_cart, text=Commands.my_cart.value
    )