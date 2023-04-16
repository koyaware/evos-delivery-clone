from aiogram import Dispatcher
from aiogram.types import Message
from sqlalchemy import and_

from commands.admins import MyCartCommands
from config import Config
from filters.admin import UserFilter
from keyboards.reply import MY_CART_KEYBOARDS
from models import Users, CartProducts, Products, Cart, OrderHistory


async def send_order(message: Message):
    config: Config = message.bot.get('config')
    for conf in config.tg_bot.admin_ids:
        users: Users = await Users.query.where(
            Users.tg_id == message.from_user.id
        ).gino.all()
        for user in users:
            carts: Cart = await Cart.query.where(
                Cart.user_id == message.from_user.id
            ).gino.all()
            if not carts:
                return await message.answer("Ваша корзина пуста!")
            product_name = []
            user_phone = []
            user_phone_number = []
            product_price = []
            for cart in carts:
                cart_products: CartProducts = await CartProducts.query.where(
                    CartProducts.cart_id == cart.Id
                ).gino.all()
                for cart_product in cart_products:
                    products = await Products.query.where(
                        Products.Id == cart_product.products_id
                    ).gino.all()
                    for product in products:
                        product_name.append(f"Название: {product.name}")
                        product_name.append(f"Количество: {cart_product.amount}.")
                        user_phone.append(user.phone_number)
                        for i in user_phone:
                            if i not in user_phone_number:
                                user_phone_number.append(i)
                        product_price.append(product.price)
                        price = sum(map(int, product_price * cart_product.amount))
                        orders = await OrderHistory.query.where(and_(
                            OrderHistory.user_id == message.from_user.id,
                            OrderHistory.cart_products == cart_product.Id,
                            OrderHistory.completed == False
                        )).gino.all()
                        if orders:
                            return await message.answer("Ваш заказ уже рассматривается.")
                        await OrderHistory.create(
                            user_id=message.from_user.id,
                            cart_products=cart_product.Id,
                            completed=False
                        )
            await message.bot.send_message(conf, f"Новый заказ от {message.from_user.id}!\n\n"
                                                 f"Номер телефон пользователя: "
                                                 f"<code>{chr(10).join([str(i) for i in user_phone_number])}</code>\n"
                                                 f"\nЗаказ пользователя: \n\n"
                                                 f"<b>{chr(10).join([str(i) for i in product_name])}</b>\n"
                                                 f"\nСтоимость заказа вместе с доставкой: <b>{price + 10000}</b>сум.")
            await message.answer("Ваш заказ принят! \nЖдите звонка от курьера!", reply_markup=MY_CART_KEYBOARDS)


def register_send_order_handlers(dp: Dispatcher):
    dp.register_message_handler(
        send_order, UserFilter(), text=MyCartCommands.place_order.value
    )