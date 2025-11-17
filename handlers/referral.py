# handlers/referral.py
from aiogram.types import CallbackQuery
from config import BOT_USERNAME
from texts import texts
from utils import get_user

def register_referral(dp):
    @dp.callback_query(lambda c: c.data == "earn")
    async def referral_handler(call: CallbackQuery):
        user = get_user(call.from_user.id)
        if not user:
            await call.message.answer("Користувача не знайдено!")
            return

        # Генеруємо унікальне реферальне посилання для кожного
        link = f"https://t.me/{BOT_USERNAME}?start={user.user_id}"

        # Беремо мову користувача або англійську за замовчуванням
        lang = getattr(user, "language", "en")
        text = texts.get(lang, texts["en"])["referral_link"].format(link=link)

        await call.message.answer(text)
        await call.answer()

