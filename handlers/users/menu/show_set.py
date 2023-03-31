from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from buttons.inline import keyboard
from commands.admins import MenuCommands, ShowSetCommands
from keyboards.reply import SHOW_SET_KEYBOARDS
from models import Products


async def show_set_menu(message: Message):
    products: Products = await Products.query.where(
        Products.name == "МЕНЮ SHOW_SET"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=SHOW_SET_KEYBOARDS)


async def show_first_set_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Комбо плюс Pepsi"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await state.update_data(product_id=product.Id)
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=keyboard)


async def show_second_set_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Детское комбо"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await state.update_data(product_id=product.Id)
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=keyboard)


async def show_third_set_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Фит Комбо"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await state.update_data(product_id=product.Id)
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=keyboard)


def register_set_handler(dp: Dispatcher):
    dp.register_message_handler(
        show_set_menu, text=MenuCommands.show_set.value
    )
    dp.register_message_handler(
        show_first_set_case, text=ShowSetCommands.first_case.value
    )
    dp.register_message_handler(
        show_second_set_case, text=ShowSetCommands.second_case.value
    )
    dp.register_message_handler(
        show_third_set_case, text=ShowSetCommands.third_case.value
    )