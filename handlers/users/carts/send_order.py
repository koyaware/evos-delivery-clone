from aiogram import Dispatcher
from aiogram.types import Message

from commands.admins import MyCartCommands
from config import Config
from keyboards.reply import MY_CART_KEYBOARDS
from models import Users, CartProducts, Products, Cart


async def send_order(message: Message):
    users: Users = await Users.query.where(
        Users.is_user == True
    ).gino.all()
    if not users:
        return await message.answer("У вас нет прав!\nВы забанены!")
    config: Config = message.bot.get('config')
    for conf in config.tg_bot.admin_ids:
        for user in users:
            carts: Cart = await Cart.query.where(
                Cart.user_id == user.tg_id
            ).gino.all()
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
                        product_name.append(f'{product.name}')
                        user_phone.append(user.phone_number)
                        for i in user_phone:
                            if i not in user_phone_number:
                                user_phone_number.append(i)
                        product_price.append(product.price)
                        price = sum(map(int, product_price * cart_product.amount))
        await message.bot.send_message(conf, f"Новый заказ от {message.from_user.id}!\n\n"
                                             f"Номер телефон пользователя: "
                                             f"<code>{chr(10).join([str(i) for i in user_phone_number])}</code>\n"
                                             f"\nЗаказ пользователя: \n\n"
                                             f"<b>{chr(10).join([str(i) for i in product_name])}</b>\n"
                                             f"\nСтоимость заказа вместе с доставкой: <b>{price}</b>")
        await message.answer("Ваш заказ принят! \nЖдите звонка от курьера!", reply_markup=MY_CART_KEYBOARDS)


def register_send_order_handlers(dp: Dispatcher):
    dp.register_message_handler(
        send_order, text=MyCartCommands.place_order.value
    )