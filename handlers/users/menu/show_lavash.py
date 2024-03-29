from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from buttons.inline import keyboard
from commands.admins import MenuCommands, ShowLavashCommands
from filters.admin import UserFilter
from keyboards.reply import SHOW_LAVASH_KEYBOARDS
from models import Products


async def show_lavash_menu(message: Message):
    products: Products = await Products.query.where(
        Products.name == "МЕНЮ SHOW_LAVASH"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc,
                                     reply_markup=SHOW_LAVASH_KEYBOARDS)


async def show_first_lavash_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Лаваш с говядиной"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=f"{product.desc}\n\nСтоимость: <b>{product.price}</b>",
                                     reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


async def show_second_lavash_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Лаваш с курицей"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=f"{product.desc}\n\nСтоимость: <b>{product.price}</b>",
                                     reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


async def show_third_lavash_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Лаваш с говядиной Мини"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=f"{product.desc}\n\nСтоимость: <b>{product.price}</b>",
                                     reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


async def show_fourth_lavash_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Лаваш с курицей Мини"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=f"{product.desc}\n\nСтоимость: <b>{product.price}</b>",
                                     reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


async def show_fifth_lavash_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Лаваш с говядиной и сыром"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=f"{product.desc}\n\nСтоимость: <b>{product.price}</b>",
                                     reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


async def show_sixth_lavash_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Лаваш с курицей и сыром"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=f"{product.desc}\n\nСтоимость: <b>{product.price}</b>",
                                     reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


async def show_seventh_lavash_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Лаваш с говядиной и сыром Мини"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=f"{product.desc}\n\nСтоимость: <b>{product.price}</b>",
                                     reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


async def show_eighth_lavash_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Лаваш с курицей и сыром Мини"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=f"{product.desc}\n\nСтоимость: <b>{product.price}</b>",
                                     reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


async def show_ninth_lavash_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Лаваш острый с говядиной"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=f"{product.desc}\n\nСтоимость: <b>{product.price}</b>",
                                     reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


async def show_tenth_lavash_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Лаваш острый с курицей"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=f"{product.desc}\n\nСтоимость: <b>{product.price}</b>",
                                     reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


async def show_eleventh_lavash_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Фиттер"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=f"{product.desc}\n\nСтоимость: <b>{product.price}</b>",
                                     reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


def register_lavash_handler(dp: Dispatcher):
    dp.register_message_handler(
        show_lavash_menu, text=MenuCommands.show_lavash.value
    )
    dp.register_message_handler(
        show_first_lavash_case, UserFilter(), text=ShowLavashCommands.first_case.value
    )
    dp.register_message_handler(
        show_second_lavash_case, UserFilter(), text=ShowLavashCommands.second_case.value
    )
    dp.register_message_handler(
        show_third_lavash_case, UserFilter(), text=ShowLavashCommands.third_case.value
    )
    dp.register_message_handler(
        show_fourth_lavash_case, UserFilter(), text=ShowLavashCommands.fourth_case.value
    )
    dp.register_message_handler(
        show_fifth_lavash_case, UserFilter(), text=ShowLavashCommands.fifth_case.value
    )
    dp.register_message_handler(
        show_sixth_lavash_case, UserFilter(), text=ShowLavashCommands.sixth_case.value
    )
    dp.register_message_handler(
        show_seventh_lavash_case, UserFilter(), text=ShowLavashCommands.seventh_case.value
    )
    dp.register_message_handler(
        show_eighth_lavash_case, UserFilter(),  text=ShowLavashCommands.eighth_case.value
    )
    dp.register_message_handler(
        show_ninth_lavash_case, UserFilter(), text=ShowLavashCommands.ninth_case.value
    )
    dp.register_message_handler(
        show_tenth_lavash_case, UserFilter(), text=ShowLavashCommands.tenth_case.value
    )
    dp.register_message_handler(
        show_eleventh_lavash_case, UserFilter(), text=ShowLavashCommands.eleventh_case.value
    )