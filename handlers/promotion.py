from aiogram.types import CallbackQuery

def register_promotion(dp):
    @dp.callback_query(lambda c: c.data == "promo")
    async def promo_handler(call: CallbackQuery):
        await call.message.answer(
            "Розкрутка каналів — тут буде логіка вибору каналу, підписників та ціни. (Розширити за потребою)"
        )
        await call.answer()
