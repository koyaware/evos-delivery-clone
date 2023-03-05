from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

# from buttons.inline import keyboard
from commands.admins import Commands, MenuCommands, ShowSetCommands
from keyboards.reply import USER_KEYBOARDS, MENU_KEYBOARDS, SHOW_SET_KEYBOARDS
from models import Users, Products


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