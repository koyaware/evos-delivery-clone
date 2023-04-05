from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from buttons.inline import keyboard
from commands.admins import MenuCommands, ShowDesertsCommands
from keyboards.reply import SHOW_DESERTS_KEYBOARDS
from models import Products


async def show_deserts_menu(message: Message):
    products: Products = await Products.query.where(
        Products.name == "МЕНЮ SHOW_DESERTS"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=SHOW_DESERTS_KEYBOARDS)


async def show_first_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Медовик"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=f"{product.desc}\n\nСтоимость: <b>{product.price}</b>",
                                     reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


async def show_second_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Чизкейк"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=f"{product.desc}\n\nСтоимость: <b>{product.price}</b>",
                                     reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


async def show_third_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Донат Ягодный микс"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=f"{product.desc}\n\nСтоимость: <b>{product.price}</b>",
                                     reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


async def show_fourth_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Донат Карамельный"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=f"{product.desc}\n\nСтоимость: <b>{product.price}</b>",
                                     reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


def register_deserts_handler(dp: Dispatcher):
    dp.register_message_handler(
        show_deserts_menu, text=MenuCommands.show_deserts.value
    )
    dp.register_message_handler(
        show_first_case, text=ShowDesertsCommands.first_case.value
    )
    dp.register_message_handler(
        show_second_case, text=ShowDesertsCommands.second_case.value
    )
    dp.register_message_handler(
        show_third_case, text=ShowDesertsCommands.third_case.value
    )
    dp.register_message_handler(
        show_fourth_case, text=ShowDesertsCommands.fourth_case.value
    )