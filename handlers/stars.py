# handlers/stars.py
from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()

@router.callback_query(lambda c: c.data == "stars")
async def buy_stars(query: CallbackQuery):
    # Реалізація покупки за баланс чи інтеграція з криптоплатежем опущена
    await query.message.answer("⭐ Купівля Telegram Stars: ця функція тут демонструє тільки інтерфейс. Реалізації платежу немає.")
