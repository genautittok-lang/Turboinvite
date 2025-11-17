# handlers/referral.py
from aiogram.types import CallbackQuery
from config import BOT_USERNAME
from texts import TEXTS
from utils import get_user  # має повертати об’єкт користувача з .language

def register_referral(dp):
    @dp.callback_query(lambda c: c.data == "earn")
    async def referral_handler(call: CallbackQuery):
        user = get_user(call.from_user.id)
        if not user:
            await call.answer("Користувач не знайдений.", show_alert=True)
            return

        link = f"https://t.me/{BOT_USERNAME}?start={call.from_user.id}"
        lang = getattr(user, "language", "en")  # за замовчуванням англійська
        text = TEXTS[lang]['referral_link'].format(link=link)

        await call.message.answer(text)
        await call.answer()
