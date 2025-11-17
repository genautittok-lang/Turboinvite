from aiogram import types
from aiogram.filters import CommandStart
from keyboards import language_menu, main_menu
from texts import TEXTS
from utils import add_user, set_language, get_user, update_balance, add_referral
from config import REF_BONUS

def register_start(dp):
    @dp.message(CommandStart())
    async def start_handler(msg: types.Message):
        user_id = msg.from_user.id
        name = msg.from_user.full_name or msg.from_user.username or "User"
        # language default EN until user chooses
        add_user(user_id, name, "EN")

        # handle referral if present in /start argument
        if msg.text and "?start=" in msg.text:
            try:
                ref_id = int(msg.text.split("=")[-1])
                if ref_id != user_id:
                    # add referral count and bonus in default currency (we'll use inviter's currency)
                    inviter = get_user(ref_id)
                    if inviter:
                        currency = inviter["currency"] or "USD"
                        bonus = REF_BONUS.get(currency, REF_BONUS["USD"])
                        update_balance(ref_id, bonus, currency, tx_type="referral")
                        add_referral(ref_id)
            except:
                pass

        await msg.answer(TEXTS["choose_language"]["EN"], reply_markup=language_menu())
