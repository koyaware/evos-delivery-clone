from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from buttons.inline import keyboard
from commands.admins import MenuCommands, ShowDishesCommands
from keyboards.reply import SHOW_DISHES_KEYBOARDS
from models import Products


async def show_dishes_menu(message: Message):
    products: Products = await Products.query.where(
        Products.name == "МЕНЮ SHOW_DISHES"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=SHOW_DISHES_KEYBOARDS)


async def show_first_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Донар с говядиной"
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
        Products.name == "Донар с курицей"
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
        Products.name == "Стрипсы"
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
        Products.name == "Ифтар кофте с говядиной"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=f"{product.desc}\n\nСтоимость: <b>{product.price}</b>",
                                     reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


async def show_fifth_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Ифтар стрипс с курицей"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=f"{product.desc}\n\nСтоимость: <b>{product.price}</b>",
                                     reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


async def show_sixth_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Донар-бокс с говядиной"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=f"{product.desc}\n\nСтоимость: <b>{product.price}</b>",
                                     reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


async def show_seventh_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Донар-бокс с курицей"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=f"{product.desc}\n\nСтоимость: <b>{product.price}</b>",
                                     reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


def register_dishes_handler(dp: Dispatcher):
    dp.register_message_handler(
        show_dishes_menu, text=MenuCommands.show_dishes.value
    )
    dp.register_message_handler(
        show_first_case, text=ShowDishesCommands.first_case.value
    )
    dp.register_message_handler(
        show_second_case, text=ShowDishesCommands.second_case.value
    )
    dp.register_message_handler(
        show_third_case, text=ShowDishesCommands.third_case.value
    )
    dp.register_message_handler(
        show_fourth_case, text=ShowDishesCommands.fourth_case.value
    )
    dp.register_message_handler(
        show_fifth_case, text=ShowDishesCommands.fifth_case.value
    )
    dp.register_message_handler(
        show_sixth_case, text=ShowDishesCommands.sixth_case.value
    )
    dp.register_message_handler(
        show_seventh_case, text=ShowDishesCommands.seventh_case.value
    )