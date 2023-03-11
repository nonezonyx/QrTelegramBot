from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from aiogram.utils.exceptions import ValidationError
import logging
from os import getenv
from TgBot.handlers import register_all_handlers
from TgBot.config import BOT_NAME, WEBAPP_PORT, WEBAPP_HOST
from TgBot.filters import register_all_filters


TOKEN = getenv(f"{BOT_NAME}_TOKEN", "")
WEBHOOK_HOST = getenv("domain", "")
WEBHOOK_PATH = getenv(f"{BOT_NAME}_API_PATH", "")
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"


async def on_startup(dp: Dispatcher):
    logging.info("Starting")
    bot: Bot = dp.bot

    await bot.set_webhook(WEBHOOK_URL)

    register_all_handlers(dp)
    register_all_filters(dp)


async def on_shutdown(dp: Dispatcher):
    logging.info('Shutting down..')
    bot: Bot = dp.bot
    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()
    logging.info('Bye!')


def start_telegram_bot() -> None:
    try:
        bot = Bot(TOKEN, parse_mode="HTML")
        dp = Dispatcher(bot)
        executor.start_webhook(
            dispatcher=dp,
            webhook_path=WEBHOOK_PATH,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            skip_updates=True,
            host=WEBAPP_HOST,
            port=WEBAPP_PORT,
        )
    except ValidationError:
        logging.critical(f"Invalid TOKEN at '{BOT_NAME}_TOKEN'")
        exit()
