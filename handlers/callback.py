from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from models import Cart, CartProducts


async def cb_handler(callback: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        product_id = data['product_id']
    cart_user: Cart = await Cart.query.where(
        Cart.user_id == callback.message.from_user.id)
    if not cart_user:
        await Cart.create(user_id=callback.message.from_user.id)
    cart = await CartProducts.query.where(
        CartProducts.cart_id != cart_user.user_id)
    cb_data = callback.data

    if cb_data == 'add_item':
        if not cart:
            await CartProducts.create(products_id=product_id)
            return await callback.bot.send_message(callback.message.from_user.id, 'Добавлено в корзину!')
        await state.finish()
        return await callback.message.answer("Корзина пуста!")

    elif cb_data == 'remove_item':
        if not cart:
            await CartProducts.delete(products_id=product_id)
            return await callback.bot.send_message(callback.from_user.id, 'Вы успешно удалили с корзины!')
        await state.finish()
        return await callback.message.answer("Корзина пуста!\nИли Вы этого не добавляли!")


def register_all_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        cb_handler
    )