# handlers/start.py
from aiogram import Router
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart
from aiogram.utils.deep_linking import decode_payload
from database import SessionLocal
from models import User
from texts import TEXTS
from keyboards.main_menu import main_menu

router = Router()

# --- Клавіатура вибору мови ---
lang_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Українська", callback_data="set_lang_uk")],
    [InlineKeyboardButton(text="English", callback_data="set_lang_en")],
    [InlineKeyboardButton(text="Русский", callback_data="set_lang_ru")]
])

# --- Клавіатура вибору валюти ---
currency_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="UAH", callback_data="set_currency_UAH")],
    [InlineKeyboardButton(text="USD", callback_data="set_currency_USD")],
    [InlineKeyboardButton(text="RUB", callback_data="set_currency_RUB")]
])

@router.message(CommandStart(deep_link=True))
async def cmd_start(message: Message):
    args = message.text.split(' ')[1:]  # аргументи після /start
    payload = args[0] if args else None

    db = SessionLocal()
    try:
        # Перевіряємо/створюємо користувача
        user = db.query(User).filter_by(user_id=message.from_user.id).first()
        if not user:
            user = User(
                user_id=message.from_user.id,
                name=message.from_user.full_name,
                language='uk',
                currency='UAH',
                balance=0.0,
                invited=0,
                level='Newbie',
                referrer_id=None
            )
            # Обробка реферального payload
            if payload:
                try:
                    ref_id = int(decode_payload(payload))
                    ref_user = db.query(User).filter_by(user_id=ref_id).first()
                    if ref_user:
                        ref_user.invited += 1
                        user.referrer_id = ref_id
                except Exception:
                    pass
            db.add(user)
            db.commit()

        # Привітання за ім'ям та пропозиція обрати мову
        name = message.from_user.full_name
        await message.answer(f"👋 Привіт, {name}!\nОберіть мову:", reply_markup=lang_keyboard)
    finally:
        db.close()


@router.callback_query(lambda c: c.data.startswith("set_lang_"))
async def set_language(query: CallbackQuery):
    lang = query.data.split("_")[-1]  # 'uk', 'en' або 'ru'
    user_id = query.from_user.id

    db = SessionLocal()
    try:
        user = db.query(User).filter_by(user_id=user_id).first()
        if user:
            user.language = lang
            db.commit()
        # Після вибору мови запитуємо валюту
        await query.message.answer("Оберіть валюту:", reply_markup=currency_keyboard)
    finally:
        db.close()


@router.callback_query(lambda c: c.data.startswith("set_currency_"))
async def set_currency(query: CallbackQuery):
    cur = query.data.split("_")[-1]  # 'UAH', 'USD' або 'RUB'
    user_id = query.from_user.id

    db = SessionLocal()
    try:
        user = db.query(User).filter_by(user_id=user_id).first()
        if user:
            user.currency = cur
            db.commit()
            # Після мови і валюти вітаємо користувача і показуємо головне меню
            welcome_text = texts[user.language]['welcome'].format(name=user.name)
            await query.message.answer(welcome_text, reply_markup=main_menu)
    finally:
        db.close()
