from aiogram import Dispatcher, Bot
from aiogram.types import Message
from aiogram.dispatcher.webhook import SendMessage

from TgBot.database.methods.create import create_user

from TgBot.libs.qr import make_qr


async def __start(msg: Message):
    user_id = msg.from_user.id
    create_user(user_id)
    return SendMessage(user_id, f"Hi, <b>{msg.from_user.first_name}</b>!\nI convert text to Qr-code")


async def __qmake_qr_code(msg: Message):
    bot: Bot = msg.bot
    qr_file = make_qr(data=msg.text)
    await bot.send_photo(msg.chat.id, qr_file.getvalue())


def register_users_handlers(dp: Dispatcher):
    dp.register_message_handler(__start, commands=["start"])
    dp.register_message_handler(__qmake_qr_code, content_types=["text"])
