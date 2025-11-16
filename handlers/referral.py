from aiogram.types import CallbackQuery
from config import BOT_USERNAME
from texts import TEXTS
from utils import get_user

def register_referral(dp):
    @dp.callback_query(lambda c: c.data == "earn")
    async def referral_handler(call: CallbackQuery):
        user = get_user(call.from_user.id)
        link = f"https://t.me/{BOT_USERNAME}?start={call.from_user.id}"
        text = TEXTS["referral_link"]["EN"].format(link=link)
        await call.message.answer(text)
        await call.answer()
