from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from sqlalchemy import and_

from buttons.inline import cart_cb
from models import Trash


async def add_item(callback: CallbackQuery, callback_data: dict, state: FSMContext):
    amount = int(callback_data['amount'])
    amount += 1
    async with state.proxy() as data:
        product_id = data['product_id']
    cart = await Trash.query.where(and_(
        Trash.user_id == callback.message.from_user.id,
        Trash.products_id == product_id)).gino.all()
    if not cart:
        await Trash.create(user_id=callback.message.from_user.id,
                           products_id=product_id,
                           amount=amount)
        return await callback.bot.send_message(callback.message.from_user.id, 'Добавлено в корзину!')
    await state.finish()
    return await callback.message.answer("Корзина пуста!")


async def remove_item(callback: CallbackQuery, callback_data: dict, state: FSMContext):
    amount = int(callback_data['amount'])
    amount += 1
    async with state.proxy() as data:
        product_id = data['product_id']
    cart = await Trash.query.where(and_(
        Trash.user_id == callback.message.from_user.id,
        Trash.products_id == product_id)).gino.all()
    if not cart:
        return await callback.message.answer("Корзина пуста!\nИли Вы этого не добавляли!")
    await Trash.delete(user_id=callback.from_user.id,
                       products_id=product_id)
    await state.finish()
    return await callback.bot.send_message(callback.from_user.id, 'Вы успешно удалили с корзины!')


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        add_item, cart_cb.filter(action='add_item')
    )
    dp.register_callback_query_handler(
        remove_item, cart_cb.filter(action='remove_item')
    )