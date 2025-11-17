# handlers/support.py
from aiogram import Router
from aiogram.types import CallbackQuery
from texts import TEXTS

router = Router()

@router.callback_query(lambda c: c.data == "support")
async def support(query: CallbackQuery):
    user_id = query.from_user.id
    # Мова користувача (як приклад беремо українську якщо не знайдено)
    lang = 'uk'
    txt = texts[lang]['support']
    await query.message.answer(txt)
