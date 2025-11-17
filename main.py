# main.py
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from config import BOT_TOKEN
from database import init_db, SessionLocal
import handlers.start as start_handler
import handlers.menu as menu_handler
import handlers.balance as balance_handler
import handlers.withdraw as withdraw_handler
import handlers.earn as earn_handler
import handlers.promotion as promo_handler
import handlers.stars as stars_handler
import handlers.settings as settings_handler
import handlers.profile as profile_handler
import handlers.support as support_handler
import handlers.admin as admin_handler

async def main():
    # Ініціалізуємо БД (створення таблиць)
    await init_db()
    # Створюємо об'єкти бота та диспетчера
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Підключаємо всі роутери/обробники
    # (кожний модуль handlers.* сам реєструє свої хендлери)
    dp.include_router(start_handler.router)
    dp.include_router(menu_handler.router)
    dp.include_router(balance_handler.router)
    dp.include_router(withdraw_handler.router)
    dp.include_router(earn_handler.router)
    dp.include_router(promo_handler.router)
    dp.include_router(stars_handler.router)
    dp.include_router(settings_handler.router)
    dp.include_router(profile_handler.router)
    dp.include_router(support_handler.router)
    dp.include_router(admin_handler.router)

    # Запускаємо опитування Telegram-серверу
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
