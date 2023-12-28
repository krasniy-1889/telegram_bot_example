from aiogram import Router

from handlers.start import start_router

all_routers = Router(name="routers")

all_routers.include_routers(start_router)
