from aiogram import Dispatcher
from aiogram.types import Message
from sqlalchemy import and_

from commands.admins import AdminCommands
from filters import AdminFilter
from models import OrderHistory, Users, CartProducts, Products


async def user_orders_completed(message: Message):
    orders: OrderHistory = await OrderHistory.query.where(
        OrderHistory.completed == True
    ).gino.all()
    if not orders:
        return await message.answer('Нет выполненных заказов!')
    for order in orders:
        users: Users = await Users.query.where(and_(
            Users.tg_id == order.user_id,
            Users.location_latitude == Users.location_latitude,
            Users.location_longitude == Users.location_longitude
        )).gino.all()
        product_name = []
        user_phone = []
        user_phone_number = []
        product_price = []
        order_time = []
        for user in users:
            cart_products: CartProducts = await CartProducts.query.where(
                CartProducts.Id == order.cart_products
            ).gino.all()
            for cart_product in cart_products:
                products: Products = await Products.query.where(
                    Products.Id == cart_product.products_id
                ).gino.all()
                for product in products:
                    location_latitude = map(float, user.location_latitude)
                    location_longitude = map(float, user.location_longitude)
                    order_time.append(f"Дата: {order.order_date}")
                    product_name.append(f"Название: {product.name}")
                    product_name.append(f"Количество: {cart_product.amount}.")
                    user_phone.append(user.phone_number)
                    for i in user_phone:
                        if i not in user_phone_number:
                            user_phone_number.append(i)
                    product_price.append(product.price)
                    price = sum(map(int, product_price * cart_product.amount))
        await message.bot.send_message(message.from_user.id, f"Выполненный заказ от {order.user_id}!\n\n"
                                                             f"Номер телефон пользователя: "
                                                             f"<code>{chr(10).join([str(i) for i in user_phone_number])}</code>\n"
                                                             f"\nЗаказ пользователя: \n\n"
                                                             f"<b>{chr(10).join([str(i) for i in product_name])}</b>\n"
                                                             f"\nСтоимость заказа без доставки: <b>{price}</b>сум.\n"
                                                             f"\nДата оформления заказа: {order_time}"
                                                             f"\n🔻 Геолокация пользователя: 🔻")
    await message.bot.send_location(chat_id=message.from_user.id,
                                    latitude=location_latitude,
                                    longitude=location_longitude)


def register_user_orders_completed_handlers(dp: Dispatcher):
    dp.register_message_handler(
        user_orders_completed, AdminFilter(), text=AdminCommands.order_history_completed.value
    )