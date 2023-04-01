from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from buttons.inline import keyboard
from commands.admins import MenuCommands, ShowHotDogCommands
from keyboards.reply import SHOW_HOT_DOG_KEYBOARDS
from models import Products


async def show_hot_dog_menu(message: Message):
    products: Products = await Products.query.where(
        Products.name == "МЕНЮ SHOW_HOT_DOG"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=SHOW_HOT_DOG_KEYBOARDS)


async def show_first_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Хот-дог"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


async def show_second_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Даблхот-дог"
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
        Products.name == "Хот-дог Мини"
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
        Products.name == "Картофель Фри"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


async def show_fifth_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Картофель по-деревенски"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


async def show_sixth_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Хот-дог детский"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


async def show_seventh_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Саб с курицей"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


async def show_eighth_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Саб с говядиной"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


async def show_ninth_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Саб с курицей и сыром"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


async def show_tenth_case(message: Message, state: FSMContext):
    products: Products = await Products.query.where(
        Products.name == "Саб с говядиной и сыром"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url,
                                     caption=product.desc, reply_markup=keyboard)
        await state.update_data(product_id=product.Id)
        await state.update_data(product_amount=1)


def register_hot_dog_handler(dp: Dispatcher):
    dp.register_message_handler(
        show_hot_dog_menu, text=MenuCommands.show_hot_dog.value
    )
    dp.register_message_handler(
        show_first_case, text=ShowHotDogCommands.first_case.value
    )
    dp.register_message_handler(
        show_second_case, text=ShowHotDogCommands.second_case.value
    )
    dp.register_message_handler(
        show_third_case, text=ShowHotDogCommands.third_case.value
    )
    dp.register_message_handler(
        show_fourth_case, text=ShowHotDogCommands.fourth_case.value
    )
    dp.register_message_handler(
        show_fifth_case, text=ShowHotDogCommands.fifth_case.value
    )
    dp.register_message_handler(
        show_sixth_case, text=ShowHotDogCommands.sixth_case.value
    )
    dp.register_message_handler(
        show_seventh_case, text=ShowHotDogCommands.seventh_case.value
    )
    dp.register_message_handler(
        show_eighth_case, text=ShowHotDogCommands.eighth_case.value
    )
    dp.register_message_handler(
        show_ninth_case, text=ShowHotDogCommands.ninth_case.value
    )
    dp.register_message_handler(
        show_tenth_case, text=ShowHotDogCommands.tenth_case.value
    )