from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message
from sqlalchemy import and_

from config import Config
from models import Users, Cart, OrderHistory


class AdminFilter(BoundFilter):

    async def check(self, message: Message):
        config: Config = message.bot.get('config')
        return message.from_user.id in config.tg_bot.admin_ids


class UserFilter(BoundFilter):

    async def check(self, message: Message):
        users: Users = await Users.query.where(and_(
            Users.tg_id == message.from_user.id,
            Users.phone_number == Users.phone_number,
            Users.is_user == True
        )).gino.all()
        for user in users:
            return user.is_user == True


class CartFilter(BoundFilter):

    async def check(self, message: Message):
        cart_users: Cart = await Cart.query.where(
            Cart.user_id == message.from_user.id
        ).gino.all()
        for cart_user in cart_users:
            return cart_user.user_id == message.from_user.id