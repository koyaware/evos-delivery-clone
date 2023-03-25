from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from sqlalchemy import and_

from models import Trash


async def cb_handler(callback: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        product_id = data['product_id']
    cart = await Trash.query.where(and_(
        Trash.user_id == callback.message.from_user.id,
        Trash.products_id == product_id)).gino.all()
    cb_data = callback.data

    if cb_data == "add_item":
        if not cart:
            await Trash.create(user_id=callback.message.from_user.id,
                               products_id=product_id)
            return await callback.bot.send_message(callback.message.from_user.id, 'Добавлено в корзину!')
        await state.finish()
        return await callback.message.answer("Корзина пуста!")

    elif cb_data == "remove_item":
        if not cart:
            return await callback.message.answer("Корзина пуста!\nИли Вы этого не добавляли!")
        await Trash.delete(user_id=callback.from_user.id,
                           products_id=product_id)
        await state.finish()
        return await callback.bot.send_message(callback.from_user.id, 'Вы успешно удалили с корзины!')


def register_all_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        cb_handler
    )