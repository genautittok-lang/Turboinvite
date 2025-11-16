from aiogram.types import CallbackQuery

def register_stars(dp):
    @dp.callback_query(lambda c: c.data == "stars")
    async def stars_handler(call: CallbackQuery):
        await call.message.answer(
            "Купівля Telegram Stars — тут буде логіка вибору кількості та оплати. (Розширити за потребою)"
        )
        await call.answer()
