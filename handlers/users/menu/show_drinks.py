from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from buttons.inline import keyboard
from commands.admins import MenuCommands, ShowHotDogCommands, ShowDrinksCommands
from keyboards.reply import SHOW_DRINKS_KEYBOARDS
from misc.states import ProductsIdState
from models import Products


async def show_drinks_menu(message: Message):
    products: Products = await Products.query.where(
        Products.name == "МЕНЮ SHOW_DRINKS"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=SHOW_DRINKS_KEYBOARDS)


async def show_first_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Сок Блисс, 1 литр"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=keyboard)
        await ProductsIdState.product_id.set()
        await state.update_data(product_id=product.Id)


async def show_second_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Сок Дена без сахара, 0,33"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=keyboard)
        await ProductsIdState.product_id.set()
        await state.update_data(product_id=product.Id)


async def show_third_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Вода без газа 0,5л"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=keyboard)
        await ProductsIdState.product_id.set()
        await state.update_data(product_id=product.Id)


async def show_fourth_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Пепси, 1,5л"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=keyboard)
        await ProductsIdState.product_id.set()
        await state.update_data(product_id=product.Id)


async def show_fifth_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Пепси, разлив 0,4л"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=keyboard)
        await ProductsIdState.product_id.set()
        await state.update_data(product_id=product.Id)


async def show_sixth_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Пепси, 0,5л"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=keyboard)
        await ProductsIdState.product_id.set()
        await state.update_data(product_id=product.Id)


async def show_seventh_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Чай черный"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=keyboard)
        await ProductsIdState.product_id.set()
        await state.update_data(product_id=product.Id)


async def show_eighth_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Капучино"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=keyboard)
        await ProductsIdState.product_id.set()
        await state.update_data(product_id=product.Id)


async def show_ninth_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Американо"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=keyboard)
        await ProductsIdState.product_id.set()
        await state.update_data(product_id=product.Id)


async def show_tenth_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Латте"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=keyboard)
        await ProductsIdState.product_id.set()
        await state.update_data(product_id=product.Id)


async def show_eleventh_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Стакан 200мл"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=keyboard)
        await ProductsIdState.product_id.set()
        await state.update_data(product_id=product.Id)


def register_drinks_handler(dp: Dispatcher):
    dp.register_message_handler(
        show_drinks_menu, text=MenuCommands.show_drinks.value
    )
    dp.register_message_handler(
        show_first_case, text=ShowDrinksCommands.first_case.value
    )
    dp.register_message_handler(
        show_second_case, text=ShowDrinksCommands.second_case.value
    )
    dp.register_message_handler(
        show_third_case, text=ShowDrinksCommands.third_case.value
    )
    dp.register_message_handler(
        show_fourth_case, text=ShowDrinksCommands.fourth_case.value
    )
    dp.register_message_handler(
        show_fifth_case, text=ShowDrinksCommands.fifth_case.value
    )
    dp.register_message_handler(
        show_sixth_case, text=ShowDrinksCommands.sixth_case.value
    )
    dp.register_message_handler(
        show_seventh_case, text=ShowDrinksCommands.seventh_case.value
    )
    dp.register_message_handler(
        show_eighth_case, text=ShowDrinksCommands.eighth_case.value
    )
    dp.register_message_handler(
        show_ninth_case, text=ShowDrinksCommands.ninth_case.value
    )
    dp.register_message_handler(
        show_tenth_case, text=ShowDrinksCommands.tenth_case.value
    )
    dp.register_message_handler(
        show_eleventh_case, text=ShowDrinksCommands.eleventh_case.value
    )