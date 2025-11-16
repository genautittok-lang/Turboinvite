from aiogram import types
from aiogram.filters import CommandStart
from keyboards import main_menu, language_menu
from texts import TEXTS
from utils import add_user, update_balance

def register_start(dp):
    @dp.message(CommandStart())
    async def start_handler(msg: types.Message):
        user_id = msg.from_user.id
        username = msg.from_user.username or msg.from_user.first_name
        add_user(user_id, username)

        # Language choice
        await msg.answer(
            "Оберіть мову / Select your language / Выберите язык",
            reply_markup=language_menu()
        )

        # Referral bonus check
        if "?start=" in msg.text:
            ref_id = msg.text.split("=")[-1]
            if ref_id.isdigit() and int(ref_id) != user_id:
                update_balance(int(ref_id), 0.25)  # Bonus USD (можеш розширити під UAH/RUB)
