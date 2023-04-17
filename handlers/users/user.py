from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from sqlalchemy import and_

from commands.admins import Commands
from filters.admin import UserFilter
from keyboards.reply import USER_KEYBOARDS, MENU_KEYBOARDS, SEND_CONTACT_KEYBOARD
from models import Users


async def user_start(message: Message):
    users = await Users.query.where(and_(
        Users.tg_id == message.from_user.id,
        Users.phone_number == Users.phone_number,
        Users.location_latitude == Users.location_latitude,
        Users.location_longitude == Users.location_longitude
    )).gino.all()
    if not users:
        return await message.answer("Отправьте ваш номер телефона.",
                                    reply_markup=SEND_CONTACT_KEYBOARD)
    is_user = await Users.query.where(
        Users.is_user == True
    ).gino.all()
    if not is_user:
        return await message.answer("У вас нет прав!\nВы забанены!")
    await message.answer("Привет, пользователь! Выбери команду: ", reply_markup=USER_KEYBOARDS)


async def main_menu(message: Message, state: FSMContext):
    await message.answer("Выберите категорию: ", reply_markup=MENU_KEYBOARDS)
    await state.update_data(product_amount=1)


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(
        user_start, text=["!start", "/start", Commands.come_back.value]
    )
    dp.register_message_handler(
        main_menu, UserFilter(), text=Commands.main_menu.value
    )