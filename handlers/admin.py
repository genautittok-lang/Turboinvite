# handlers/admin.py
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text, Command
from database import SessionLocal
from models import User
from config import ADMIN_IDS

router = Router()

@router.message(Command("admin"))
async def admin_help(message: Message):
    if message.from_user.id in ADMIN_IDS:
        await message.answer("Адмін-панель:\n/check_withdraws\n/ban <user_id>\n/balance_set <user_id> <amount>\n/broadcast <text>")
    else:
        await message.answer("У вас немає доступу до адмін-панелі.")

@router.message(Command("check_withdraws"))
async def check_withdraws(message: Message):
    if message.from_user.id not in ADMIN_IDS:
        return
    # Тут би вибирали всі pending-заявки і показували їх
    await message.answer("Перелік заявок на виведення (приклад):")

@router.message(Text(startswith="/ban"))
async def ban_user(message: Message):
    if message.from_user.id not in ADMIN_IDS:
        return
    parts = message.text.split()
    if len(parts) == 2:
        uid = int(parts[1])
        db = SessionLocal()
        user = db.query(User).filter_by(user_id=uid).first()
        if user:
            user.is_banned = True
            db.commit()
            await message.answer(f"Користувача {uid} заблоковано.")
        else:
            await message.answer("Користувача не знайдено.")
