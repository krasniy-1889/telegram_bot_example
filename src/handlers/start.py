from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from loguru import logger

from services.user import UserService

start_router = Router()


@start_router.message(CommandStart())
async def command_start_handler(
    message: Message,
    user_service: UserService = UserService(),
) -> None:
    logger.debug("Start command")
    exists = await user_service.check_user_exists_by_telegram_id(message.from_user.id)
    if exists:
        logger.debug("User exists")
        await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
        return

    await user_service.add_user(message.from_user)  # type: ignore
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
