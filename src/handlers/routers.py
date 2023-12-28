from aiogram import Router
from handlers.start import start_router

all_routers = Router()

all_routers.include_routers(start_router)
