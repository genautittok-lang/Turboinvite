import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import register_all

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN env var not set")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
register_all(dp)

async def main():
    try:
        await dp.start_polling(bot)
    except Exception as e:
        print("Polling error:", e)

if __name__ == "__main__":
    asyncio.run(main())
