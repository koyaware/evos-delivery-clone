from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from buttons.inline import keyboard
from commands.admins import MenuCommands, ShowGarnishCommands
from keyboards.reply import SHOW_GARNISH_KEYBOARDS
from models import Products


async def show_garnish_menu(message: Message):
    products: Products = await Products.query.where(
        Products.name == "МЕНЮ SHOW_GARNISH"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=SHOW_GARNISH_KEYBOARDS)


async def show_first_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Кетчуп"
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
        Products.name == "Майонез"
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
        Products.name == "Сырный соус"
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
        Products.name == "Чесночный соус"
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
        Products.name == "Рис"
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
        Products.name == "Салат"
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
        Products.name == "Лепешка"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=f"{product.desc}\n\nСтоимость: <b>{product.price}</b>",
                                     reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


async def show_eighth_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Чили соус"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=f"{product.desc}\n\nСтоимость: <b>{product.price}</b>",
                                     reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


def register_garnish_handler(dp: Dispatcher):
    dp.register_message_handler(
        show_garnish_menu, text=MenuCommands.show_garnish.value
    )
    dp.register_message_handler(
        show_first_case, text=ShowGarnishCommands.first_case.value
    )
    dp.register_message_handler(
        show_second_case, text=ShowGarnishCommands.second_case.value
    )
    dp.register_message_handler(
        show_third_case, text=ShowGarnishCommands.third_case.value
    )
    dp.register_message_handler(
        show_fourth_case, text=ShowGarnishCommands.fourth_case.value
    )
    dp.register_message_handler(
        show_fifth_case, text=ShowGarnishCommands.fifth_case.value
    )
    dp.register_message_handler(
        show_sixth_case, text=ShowGarnishCommands.sixth_case.value
    )
    dp.register_message_handler(
        show_seventh_case, text=ShowGarnishCommands.seventh_case.value
    )
    dp.register_message_handler(
        show_eighth_case, text=ShowGarnishCommands.eighth_case.value
    )