# handlers/promotion.py
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()

@router.callback_query(lambda c: c.data == "promotion")
async def promotion(query: CallbackQuery):
    # Тут би було замовлення підписок з урахуванням рівня (знижки)
    await query.message.answer("🚀 Функція розкрутки: тут має бути логіка замовлення підписок із знижками за рівнем.")
