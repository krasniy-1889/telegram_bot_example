from sqlalchemy import exists, select
from models import UserORM
from schemas.user import UserReadDTO
from utils.repository import SQLAlchemyRepository
from database import session_factory
from loguru import logger


class UserRepository(SQLAlchemyRepository):
    model = UserORM

    # async def find_one_by_telegram_id(self, telegram_id: int) -> UserReadDTO | None:
    async def find_one_by_telegram_id(self, telegram_id: int) -> UserReadDTO:
        async with session_factory() as session:
            query = select(self.model).where(self.model.telegram_id == telegram_id)
            res = await session.execute(query)
            return res.scalar_one().to_read_model()

    async def check_user_exists_by_telegram_id(self, telegram_id: int):
        async with session_factory() as session:
            query = select(self.model.id).where(self.model.telegram_id == telegram_id)
            res = await session.execute(query)
            return bool(res.scalar_one_or_none())
