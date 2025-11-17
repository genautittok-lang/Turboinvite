# handlers/menu.py
from aiogram import Router
from aiogram.types import CallbackQuery
from database import SessionLocal
from models import User

router = Router()

@router.callback_query(lambda c: c.data == "balance")
async def show_balance(query: CallbackQuery):
    db = SessionLocal()
    user = db.query(User).filter_by(user_id=query.from_user.id).first()
    txt = texts[user.language]['balance_info'].format(
        balance=user.balance, currency=user.currency,
        invited=user.invited, level=user.level
    )
    await query.message.answer(txt)

@router.callback_query(lambda c: c.data == "profile")
async def show_profile(query: CallbackQuery):
    db = SessionLocal()
    user = db.query(User).filter_by(user_id=query.from_user.id).first()
    txt = texts[user.language]['profile_info'].format(
        name=user.name, user_id=user.user_id,
        level=user.level, invited=user.invited
    )
    await query.message.answer(txt)
