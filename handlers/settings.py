# handlers/settings.py
from aiogram import Router
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from database import SessionLocal
from models import User
from texts import texts
from keyboards.settings_menu import settings_menu

router = Router()

@router.callback_query(lambda c: c.data == "settings")
async def open_settings(query: CallbackQuery):
    # Показуємо меню налаштувань
    await query.message.answer("⚙️ Налаштування:", reply_markup=settings_menu)

@router.callback_query(lambda c: c.data == "change_lang")
async def change_language(query: CallbackQuery):
    # Аналогічно до старту – запитуємо мову
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Українська", callback_data="set_lang_uk")],
        [InlineKeyboardButton(text="English", callback_data="set_lang_en")],
        [InlineKeyboardButton(text="Русский", callback_data="set_lang_ru")]
    ])
    await query.message.answer("Оберіть мову:", reply_markup=keyboard)

@router.callback_query(lambda c: c.data == "change_currency")
async def change_currency(query: CallbackQuery):
    # Аналогічно до старту – запитуємо валюту
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="UAH", callback_data="set_currency_UAH")],
        [InlineKeyboardButton(text="USD", callback_data="set_currency_USD")],
        [InlineKeyboardButton(text="RUB", callback_data="set_currency_RUB")]
    ])
    await query.message.answer("Оберіть валюту:", reply_markup=keyboard)
