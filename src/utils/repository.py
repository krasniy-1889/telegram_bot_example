from abc import ABC, abstractmethod
from loguru import logger
from sqlalchemy import insert, select

from database import Base, session_factory


class SQLAlchemyRepository:
    model = None | Base

    async def add_one(self, data: dict):
        async with session_factory() as session:
            query = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(query)
            await session.commit()
            logger.debug("User succesfully added")
            return res.scalar_one()

    async def find_all(self):
        async with session_factory() as session:
            query = select(self.model)
            res = await session.execute(query)
            return res.scalars().all()
