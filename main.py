import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import register_all

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

register_all(dp)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
