from operator import and_

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from keyboards.reply import USER_KEYBOARDS
from models import Users


async def user_location(message: Message, state: FSMContext):
    if message.location is not None:
        async with state.proxy() as data:
            phone_number = data['phone_number']
        users: Users = await Users.query.where(and_(
            Users.tg_id == message.from_user.id,
            Users.phone_number == phone_number
        )).gino.all()
        if users:
            await Users.delete.where(Users.tg_id == message.from_user.id).gino.status()
        await Users.create(tg_id=message.from_user.id,
                           phone_number=phone_number,
                           location_latitude=str(message.location.latitude),
                           location_longitude=str(message.location.longitude))
        return await message.bot.send_message(message.from_user.id,
                                              "Успешная регистрация!\nЕсли нужно сменить локацию, зайдите в настройки."
                                              "\nПривет, пользователь! Выбери команду: ",
                                              reply_markup=USER_KEYBOARDS)


def register_user_locations_handlers(dp: Dispatcher):
    dp.register_message_handler(
        user_location, content_types=['location']
    )
