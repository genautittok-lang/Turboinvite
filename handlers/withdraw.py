# handlers/withdraw.py
from aiogram import Router
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Text
from database import SessionLocal
from models import User, Transaction
from texts import texts

router = Router()

MIN_WITHDRAW = 50.0  # приклад мінімальної суми

@router.callback_query(lambda c: c.data == "withdraw")
async def initiate_withdraw(query: CallbackQuery):
    db = SessionLocal()
    user = db.query(User).filter_by(user_id=query.from_user.id).first()
    if user.balance < MIN_WITHDRAW:
        await query.message.answer("Недостатньо коштів для виведення.")
    else:
        # Просимо користувача ввести суму
        text = texts[user.language]['ask_withdraw'].format(min=MIN_WITHDRAW, currency=user.currency)
        await query.message.answer(text)

@router.message()
async def process_withdraw(message: Message):
    # Цей хендлер перехоплює введення суми (спрощено без FSM)
    db = SessionLocal()
    user = db.query(User).filter_by(user_id=message.from_user.id).first()
    try:
        amount = float(message.text)
    except ValueError:
        await message.answer("Будь ласка, введіть числову суму.")
        return
    if amount < MIN_WITHDRAW or amount > user.balance:
        await message.answer("Невірна сума для виведення.")
        return
    # Зменшуємо баланс і створюємо транзакцію
    user.balance -= amount
    tx = Transaction(user_id=user.id, type='withdraw', amount=amount, description='Виведення коштів')
    db.add(tx)
    db.commit()
    await message.answer(texts[user.language]['withdraw_pending'])
