# main.py
import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from database import init_db  # Функція асинхронної ініціалізації БД

# Імпорт усіх роутерів
from handlers.start import router as start_router
from handlers.menu import router as menu_router
from handlers.balance import router as balance_router
from handlers.withdraw import router as withdraw_router
from handlers.earn import router as earn_router
from handlers.promotion import router as promo_router
from handlers.stars import router as stars_router
from handlers.settings import router as settings_router
from handlers.profile import router as profile_router
from handlers.support import router as support_router
from handlers.admin import router as admin_router


async def main():
    # Ініціалізація бази даних (створення таблиць)
    await init_db()

    # Створюємо об'єкти бота та диспетчера
    bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    # Підключаємо всі роутери
    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(balance_router)
    dp.include_router(withdraw_router)
    dp.include_router(earn_router)
    dp.include_router(promo_router)
    dp.include_router(stars_router)
    dp.include_router(settings_router)
    dp.include_router(profile_router)
    dp.include_router(support_router)
    dp.include_router(admin_router)

    print("Bot is running...")

    # Запускаємо полінг
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
