from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from buttons.inline import keyboard
from commands.admins import MenuCommands, ShowShawarmaCommands
from keyboards.reply import SHOW_SHAWARMA_KEYBOARDS
from models import Products


async def show_shawarma_menu(message: Message):
    products: Products = await Products.query.where(
        Products.name == "МЕНЮ SHOW_SHAWARMA"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=SHOW_SHAWARMA_KEYBOARDS)


async def show_first_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Шаурма с говядиной Мини"
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
        Products.name == "Шаурма с говядиной"
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
        Products.name == "Шаурма с курицей Мини"
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
        Products.name == "Шаурма с курицей"
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
        Products.name == "Шаурма острая с говядиной Мини"
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
        Products.name == "Шаурма острая с курицей Мини"
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
        Products.name == "Шаурма острая с курицей"
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
        Products.name == "Шаурма острая с говядиной"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=f"{product.desc}\n\nСтоимость: <b>{product.price}</b>",
                                     reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


def register_shawarma_handler(dp: Dispatcher):
    dp.register_message_handler(
        show_shawarma_menu, text=MenuCommands.show_shawarma.value
    )
    dp.register_message_handler(
        show_first_case, text=ShowShawarmaCommands.first_case.value
    )
    dp.register_message_handler(
        show_second_case, text=ShowShawarmaCommands.second_case.value
    )
    dp.register_message_handler(
        show_third_case, text=ShowShawarmaCommands.third_case.value
    )
    dp.register_message_handler(
        show_fourth_case, text=ShowShawarmaCommands.fourth_case.value
    )
    dp.register_message_handler(
        show_fifth_case, text=ShowShawarmaCommands.fifth_case.value
    )
    dp.register_message_handler(
        show_sixth_case, text=ShowShawarmaCommands.sixth_case.value
    )
    dp.register_message_handler(
        show_seventh_case, text=ShowShawarmaCommands.seventh_case.value
    )
    dp.register_message_handler(
        show_eighth_case, text=ShowShawarmaCommands.eighth_case.value
    )