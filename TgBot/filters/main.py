from aiogram import Dispatcher
from aiogram.dispatcher.filters import Filter
from aiogram.types import Message

from TgBot.database.methods.other import is_admin


class IsAdmin(Filter):
    key = "is_admin"

    async def check(self, message: Message) -> bool:
        return is_admin(Message.from_user.id)


def register_all_filters(dp: Dispatcher):
    dp.bind_filter(IsAdmin)
