from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from sqlalchemy.sql.elements import and_

from models import Cart, CartProducts


async def cb_handler(callback: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        product_id = data['product_id']
    cart_users: Cart = await Cart.query.where(
        Cart.user_id == callback.from_user.id).gino.all()
    if not cart_users:
        await Cart.create(user_id=callback.from_user.id)
    for cart_user in cart_users:
        cart_id = cart_user.Id
        carts: CartProducts = await CartProducts.query.where(and_(
            CartProducts.cart_id == cart_id,
            CartProducts.products_id == product_id
        )).gino.all()
    cb_data = callback.data

    if cb_data == 'plus_item':
        return await callback.answer("+")

    elif cb_data == 'minus_item':
        return await callback.answer("-")

    elif cb_data == 'add_item':
        await CartProducts.create(products_id=product_id, cart_id=cart_id)
        return await callback.answer('Добавлено в корзину!')

    elif cb_data == 'remove_item':
        if not carts:
            return await callback.message.answer("Корзина пуста!\nИли Вы этого не добавляли!")
        for cart in carts:
            await cart.delete()
            return await callback.answer('Вы успешно удалили с корзины!')


def register_all_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        cb_handler
    )