import typing

from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message

from config import Config


class AdminFilter(BoundFilter):

    async def check(self, message: Message):
        config: Config = message.bot.get('config')
        return message.from_user.id in config.tg_bot.admin_ids