import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import config
from database.database import Database
from handlers.start import router as start_router
from handlers.addmovies import router as addmovie_router
from handlers.searchmovie import router as search_router
from handlers.admin import router as admin_router
from handlers.stats import router as stats_router

async def main():
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    db = Database()
    await db.connect()

    dp["db"] = db

    dp.include_router(start_router)
    dp.include_router(search_router)
    dp.include_router(addmovie_router)
    dp.include_router(stats_router)
    dp.include_router(admin_router)


    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
