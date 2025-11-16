import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers.start import register_start
from handlers.referral import register_referral
from handlers.earnings import register_earnings
from handlers.withdraw import register_withdraw
from handlers.promotion import register_promotion
from handlers.stars import register_stars
from handlers.admin import register_admin

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

register_start(dp)
register_referral(dp)
register_earnings(dp)
register_withdraw(dp)
register_promotion(dp)
register_stars(dp)
register_admin(dp)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
