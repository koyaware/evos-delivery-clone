from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from keyboards.reply import SEND_LOCATION_KEYBOARD


async def user_start_ph_number(message: Message, state: FSMContext):
    if message.contact is not None:
        await state.update_data(phone_number=message.contact.phone_number, name=message.contact.first_name)
        return await message.bot.send_message(message.from_user.id, "Отлично! Отправьте вашу геолокацию.",
                                              reply_markup=SEND_LOCATION_KEYBOARD)


def register_user_phone_numbers_handlers(dp: Dispatcher):
    dp.register_message_handler(
        user_start_ph_number, content_types=['contact']
    )
