from aiogram import types
from utils import create_withdraw_request, get_user
from texts import TEXTS

def register_withdraw(dp):
    @dp.message(commands=["withdraw"])
    async def withdraw_cmd(msg: types.Message):
        user = get_user(msg.from_user.id)
        lang = user["language"] if user else "EN"
        # очікуємо формат: /withdraw <amount> <currency> <method>:<details>
        # приклад: /withdraw 50 USD card:1234
        parts = msg.text.split(maxsplit=2)
        if len(parts) < 3:
            await msg.reply("Usage: /withdraw <amount> <currency> <method>:<details>\nExample: /withdraw 50 USD card:1234")
            return
        try:
            amount = float(parts[1])
            rest = parts[2]
            if ":" in rest:
                currency, methoddetails = rest.split(maxsplit=1)
            else:
                await msg.reply("Provide currency and method, e.g. USD card:1234")
                return
            currency = currency.upper()
            if ":" in methoddetails:
                method, details = methoddetails.split(":", 1)
            else:
                method = methoddetails
                details = ""
        except Exception as e:
            await msg.reply("Invalid format. See example.")
            return

        req_id = create_withdraw_request(msg.from_user.id, amount, currency, method, details)
        await msg.reply(TEXTS["withdraw_started"][lang])
