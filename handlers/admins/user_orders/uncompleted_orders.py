from aiogram import Dispatcher
from aiogram.types import Message

from commands.admins import AdminCommands
from filters import AdminFilter
from models import OrderHistory, Users, CartProducts, Products


async def user_orders_uncompleted(message: Message):
    orders: OrderHistory = await OrderHistory.query.where(
        OrderHistory.completed == False
    ).gino.all()
    if not orders:
        return await message.answer('Нет новых заказов!')
    for order in orders:
        users: Users = await Users.query.where(
            Users.tg_id == order.user_id
        ).gino.all()
        product_name = []
        user_phone = []
        user_phone_number = []
        product_price = []
        cart_products: CartProducts = await CartProducts.query.where(
            CartProducts.Id == order.cart_products
        ).gino.all()
        for user in users:
            for cart_product in cart_products:
                products: Products = await Products.query.where(
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
        await message.bot.send_message(message.from_user.id, f"Выполненный заказ от {order.user_id}!\n\n"
                                                             f"Номер телефон пользователя: "
                                                             f"<code>{chr(10).join([str(i) for i in user_phone_number])}</code>\n"
                                                             f"\nЗаказ пользователя: \n\n"
                                                             f"<b>{chr(10).join([str(i) for i in product_name])}</b>\n"
                                                             f"\nСтоимость заказа без доставки: <b>{price}</b>сум.")


def register_user_orders_uncompleted_handlers(dp: Dispatcher):
    dp.register_message_handler(
        user_orders_uncompleted, AdminFilter(), text=AdminCommands.order_history_uncompleted.value
    )