from aiogram.types import CallbackQuery
from config import BOT_USERNAME
from texts import TEXTS
from utils import get_user  # функція повинна повертати об'єкт користувача з його мовою

def register_referral(dp):
    @dp.callback_query(lambda c: c.data == "earn")
    async def referral_handler(call: CallbackQuery):
        user = get_user(call.from_user.id)  # повертає об'єкт користувача
        link = f"https://t.me/{BOT_USERNAME}?start={call.from_user.id}"

        # Беремо мову користувача або англійську за замовчуванням
        lang = getattr(user, "language", "EN").upper()
        text = TEXTS["referral_link"].get(lang, TEXTS["referral_link"]["EN"]).format(link=link)

        await call.message.answer(text)
        await call.answer()
