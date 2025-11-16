from aiogram.types import CallbackQuery
from config import MIN_WITHDRAW
from utils import get_user

def register_withdraw(dp):
    @dp.callback_query(lambda c: c.data == "withdraw")
    async def withdraw_handler(call: CallbackQuery):
        user = get_user(call.from_user.id)
        required = MIN_WITHDRAW.get(user["currency"], 50)
        if user["balance"] >= required:
            await call.message.answer("Введіть суму для виводу та метод (карта, крипто, і т.д.) — тут реалізувати логіку форми.")
        else:
            await call.message.answer("Недостатньо коштів для виводу.")
        await call.answer()
