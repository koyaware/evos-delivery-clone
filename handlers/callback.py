from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from models import Cart, CartProducts


async def cb_handler(callback: CallbackQuery, state: FSMContext):
    cart_users: Cart = await Cart.query.where(
        Cart.user_id == callback.from_user.id).gino.all()
    if not cart_users:
        await Cart.create(user_id=callback.from_user.id)
    for cart_user in cart_users:
        cart_id = cart_user.Id
        carts: CartProducts = await CartProducts.query.where(
            CartProducts.cart_id == cart_id
        ).gino.all()
        for cart in carts:
            products_id = cart.products_id
    cb_data = callback.data

    if cb_data == 'plus_item':
        async with state.proxy() as data:
            product_amount = data['product_amount']
        product_amount += 1
        await state.update_data(product_amount=product_amount)
        return await callback.answer(f"Количество штук: {product_amount}")

    elif cb_data == 'minus_item':
        async with state.proxy() as data:
            product_amount = data['product_amount']
        product_amount -= 1
        if product_amount < 1:
            return await callback.answer("У вас не может быть меньше товаров!")
        await state.update_data(product_amount=product_amount)
        return await callback.answer(f"Количество штук: {product_amount}")

    elif cb_data == 'add_item':
        async with state.proxy() as data:
            product_id = data['product_id']
            product_amount = data['product_amount']
        await CartProducts.create(products_id=product_id, cart_id=cart_id, amount=product_amount)
        await state.update_data(product_amount=1)
        return await callback.answer('Добавлено в корзину!')

    elif cb_data == 'remove_item' or products_id:
        if not carts:
            return await callback.message.answer("Корзина пуста!\nИли Вы этого не добавляли!")
        await cart.delete()
        await state.update_data(product_amount=1)
        await callback.answer('Вы успешно удалили с корзины!')
        return await callback.bot.edit_message_reply_markup(message_id=callback.message.message_id,
                                                            chat_id=callback.message.from_user.id)


def register_all_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        cb_handler
    )