from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from sqlalchemy import and_

from commands.admins import Commands
from filters.admin import UserFilter
from keyboards.reply import USER_KEYBOARDS, MENU_KEYBOARDS
from misc.states import PhoneNumberState
from models import Users


async def user_start(message: Message):
    users = await Users.query.where(and_(
        Users.tg_id == message.from_user.id,
        Users.phone_number == Users.phone_number
    )).gino.all()
    if not users:
        await PhoneNumberState.phone_number.set()
        return await message.answer("Введите номер телефона: \nПример: +998901234567")
    is_user = await Users.query.where(
        Users.is_user == True
    ).gino.all()
    if not is_user:
        return await message.answer("У вас нет прав!\nВы забанены!")
    await message.answer("Привет, пользователь! Выбери команду: ", reply_markup=USER_KEYBOARDS)


async def user_start_ph_number(message: Message, state: FSMContext):
    phone_number = await Users.query.where(and_(
        Users.tg_id == message.from_user.id,
        Users.phone_number == message.text
    )).gino.all()
    if phone_number:
        return await message.answer('Введено неверное значение!')
    if message.text.startswith("+998"):
        if len(message.text) != 13:
            return await message.answer("Введено неверное значение!\nПопробуйте заново через /start !")
        await Users.create(tg_id=message.from_user.id, phone_number=message.text)
        await state.finish()
        return await message.bot.send_message(message.from_user.id, "Привет, пользователь! Выбери команду: ",
                                              reply_markup=USER_KEYBOARDS)


async def main_menu(message: Message, state: FSMContext):
    await message.answer("Выберите категорию: ", reply_markup=MENU_KEYBOARDS)
    await state.update_data(product_amount=1)


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(
        user_start, UserFilter(), text=["!start", "/start", Commands.come_back.value]
    )
    dp.register_message_handler(
        user_start_ph_number, UserFilter(), state=PhoneNumberState.phone_number
    )
    dp.register_message_handler(
        main_menu, UserFilter(), text=Commands.main_menu.value
    )