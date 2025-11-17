# handlers/earn.py
from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.utils.deep_linking import create_start_link
from texts import texts

router = Router()

@router.callback_query(lambda c: c.data == "earn")
async def show_referral(query: CallbackQuery):
    user_id = query.from_user.id
    # Генеруємо deep-link з кодом користувача
    link = await create_start_link(query.bot, payload=str(user_id))
    # Приклад: https://t.me/MyBot?start=123456789
    await query.message.answer(texts['uk']['referral_link'].format(link=link))
