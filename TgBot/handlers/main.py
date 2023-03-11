from aiogram import Dispatcher

from TgBot.handlers.user import register_users_handlers
from TgBot.handlers.admin import register_admin_handlers


def register_all_handlers(dp: Dispatcher) -> None:
    handlers = (
        register_users_handlers,
        register_admin_handlers
    )
    for handler in handlers:
        handler(dp)
