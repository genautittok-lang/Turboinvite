from aiogram.types import CallbackQuery
from texts import TEXTS
from utils import get_user

def register_earnings(dp):
    @dp.callback_query(lambda c: c.data == "balance")
    async def balance_handler(call: CallbackQuery):
        user = get_user(call.from_user.id)
        if user:
            text = TEXTS["balance"]["EN"].format(
                balance=user["balance"],
                currency=user["currency"],
                referrals=user["referrals_count"]
            )
            await call.message.answer(text)
        else:
            await call.message.answer("User not found!")
        await call.answer()
