from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

# from buttons.inline import keyboard
from commands.admins import Commands, MenuCommands, ShowSetCommands, ShowLavashCommands
from keyboards.reply import USER_KEYBOARDS, MENU_KEYBOARDS, SHOW_SET_KEYBOARDS, SHOW_LAVASH_KEYBOARDS
from models import Users, Products, Trash


async def user_start(message: Message, state: FSMContext):
    await state.finish()
    users = await Users.query.where(
        Users.tg_id == message.from_user.id
    ).gino.first()
    if not users:
        await Users.create(tg_id=message.from_user.id)
    is_user = await Users.query.where(
        Users.is_user == True
    ).gino.all()
    if not is_user:
        await message.answer("У вас нет прав!\nВы забанены!")
        return
    await message.answer("Привет, смертный! Выбери команду: ", reply_markup=USER_KEYBOARDS)


async def main_menu(message: Message):
    await message.answer("Выберите категорию: ", reply_markup=MENU_KEYBOARDS)


async def show_set_menu(message: Message):
    products: Products = await Products.query.where(
        Products.name == "МЕНЮ SHOW_SET"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url, reply_markup=SHOW_SET_KEYBOARDS)


async def show_first_set_case(message: Message):
    products: Products = await Products.query.where(
        Products.name == "Комбо плюс Pepsi"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url, caption=product.desc)
        # await Trash.create(user_id=message.from_user.id,
        #                    products_id=product.Id)


async def show_second_set_case(message: Message):
    products: Products = await Products.query.where(
        Products.name == "Детское комбо"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url, caption=product.desc)
        # await Trash.create(user_id=message.from_user.id,
        #                    products_id=product.Id)


async def show_third_set_case(message: Message):
    products: Products = await Products.query.where(
        Products.name == "ФитCOMBO"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url)
        # await Trash.create(user_id=message.from_user.id,
        #                    products_id=product.Id)


async def show_lavash_menu(message: Message):
    products: Products = await Products.query.where(
        Products.name == "МЕНЮ SHOW_LAVASH"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url, reply_markup=SHOW_LAVASH_KEYBOARDS)
        # await Trash.create(user_id=message.from_user.id,
        #                    products_id=product.Id)


async def show_first_lavash_case(message: Message):
    products: Products = await Products.query.where(
        Products.name == "Лаваш с говядиной"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url)
        # await Trash.create(user_id=message.from_user.id,
        #                    products_id=product.Id)


async def show_second_lavash_case(message: Message):
    products: Products = await Products.query.where(
        Products.name == "Лаваш с курицей"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url)
        # await Trash.create(user_id=message.from_user.id,
        #                    products_id=product.Id)


async def show_third_lavash_case(message: Message):
    products: Products = await Products.query.where(
        Products.name == "Лаваш с говядиной Мини"
    ).gino.all()
    if not products:
        await message.answer("Что-то пошло не так...")
    for product in products:
        await message.bot.send_photo(message.from_user.id, photo=product.photo_url)
        # await Trash.create(user_id=message.from_user.id,
        #                    products_id=product.Id)


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(
        user_start, commands=['start'], state='*', commands_prefix='!/'
    )
    dp.register_message_handler(
        main_menu, text=Commands.main_menu.value
    )
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
    dp.register_message_handler(
        show_lavash_menu, text=MenuCommands.show_lavash.value
    )
    dp.register_message_handler(
        show_first_lavash_case, text=ShowLavashCommands.first_case.value
    )
    dp.register_message_handler(
        show_second_lavash_case, text=ShowLavashCommands.second_case.value
    )
    dp.register_message_handler(
        show_third_lavash_case, text=ShowLavashCommands.third_case.value
    )