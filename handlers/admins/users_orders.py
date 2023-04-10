from aiogram import Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from commands.admins import AdminCommands
from filters import AdminFilter
from models import Users, Cart, CartProducts, Products


async def users_orders(message: Message):
    users: Users = await Users.query.where(
        Users.is_user == True
    ).gino.all()
    if not users:
        return await message.answer("У вас нет прав!\nВы забанены!")
    for user in users:
        carts: Cart = await Cart.query.where(
            Cart.user_id == user.tg_id
        ).gino.all()
        if not carts:
            return await message.answer("Что-то пошло не zxc.")
        choice_kb = InlineKeyboardMarkup()
        choice_kb.add(
            InlineKeyboardButton("Завершить заказ.", callback_data="end_delete")
        )
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
                if not products:
                    return await message.answer("Что-то пошло не qwe.")
                for product in products:
                    product_name.append(f'Название: {product.name}.')
                    product_name.append(f"Количество: {cart_product.amount}.")
                    user_phone.append(user.phone_number)
                    for i in user_phone:
                        if i not in user_phone_number:
                            user_phone_number.append(i)
                    product_price.append(product.price)
                    price = sum(map(int, product_price * cart_product.amount))
    await message.bot.send_message(message.from_user.id, f"Заказ от {user.tg_id}!\n\n"
                                         f"Номер телефон пользователя: "
                                         f"<code>{chr(10).join([str(i) for i in user_phone_number])}</code>\n"
                                         f"\nЗаказ пользователя: \n\n"
                                         f"<b>{chr(10).join([str(i) for i in product_name])}</b>\n"
                                         f"\nСтоимость заказа вместе с доставкой: <b>{price + 10000}</b>",
                                   reply_markup=choice_kb)


def register_users_orders_handlers(dp: Dispatcher):
    dp.register_message_handler(
        users_orders, AdminFilter(), text=AdminCommands.user_orders.value
    )