from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from buttons.inline import keyboard
from commands.admins import MenuCommands, ShowBurgerCommands
from filters.admin import UserFilter
from keyboards.reply import SHOW_BURGER_KEYBOARDS
from models import Products


async def show_burger_menu(message: Message):
    products: Products = await Products.query.where(
        Products.name == "МЕНЮ SHOW_BURGER"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=SHOW_BURGER_KEYBOARDS)


async def show_first_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Гамбургер"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=f"{product.desc}\nСтоимость: <b>{product.price}</b>",
                                     reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


async def show_second_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Даблбургер"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


async def show_third_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Даблчизбургер"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


async def show_fourth_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Чизбургер"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


def register_burger_handler(dp: Dispatcher):
    dp.register_message_handler(
        show_burger_menu, UserFilter(), text=MenuCommands.show_burger.value
    )
    dp.register_message_handler(
        show_first_case, UserFilter(), text=ShowBurgerCommands.first_case.value
    )
    dp.register_message_handler(
        show_second_case, UserFilter(), text=ShowBurgerCommands.second_case.value
    )
    dp.register_message_handler(
        show_third_case, UserFilter(), text=ShowBurgerCommands.third_case.value
    )
    dp.register_message_handler(
        show_fourth_case, UserFilter(), text=ShowBurgerCommands.fourth_case.value
    )