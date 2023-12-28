from loguru import logger
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

from config import settings
from handlers.routers import all_routers

WEB_SERVER_HOST = "127.0.0.1"
WEB_SERVER_PORT = 8080

WEBHOOK_PATH = "/webhook"
WEBHOOK_SECRET = settings.WEBHOOK_SECRET
BASE_WEBHOOK_URL = settings.WEBHOOK_URL


async def on_startup(bot: Bot) -> None:
    await bot.delete_webhook()
    await bot.set_webhook(
        f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}",
        secret_token=WEBHOOK_SECRET,
    )


def main():
    dp = Dispatcher()
    dp.include_routers(all_routers)  # type: ignore
    dp.startup.register(on_startup)
    bot = Bot(settings.TG_TOKEN, parse_mode=ParseMode.HTML)
    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=WEBHOOK_SECRET,
    )
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)

    web.run_app(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT)


if __name__ == "__main__":
    logger.add(sys.stderr, level="DEBUG")
    main()
