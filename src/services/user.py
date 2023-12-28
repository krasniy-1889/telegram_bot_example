from aiogram.types import User
from loguru import logger

from repositories.user import UserRepository


class UserService:
    def __init__(self):
        self.user_repo = UserRepository()

    async def add_user(self, data: User):
        user = {
            "telegram_id": data.id,
            "username": data.username,
            "first_name": data.first_name,
            "last_name": data.last_name,
            "is_bot": data.is_bot,
        }
        return await self.user_repo.add_one(user)

    async def check_user_exists_by_telegram_id(self, telegram_id: int):
        logger.debug("check_user_exists_by_telegram_id")
        res = await self.user_repo.check_user_exists_by_telegram_id(telegram_id)
        return res
