# keyboards/settings_menu.py
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

settings_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🗣 Змінити мову", callback_data="change_lang")],
    [InlineKeyboardButton(text="💱 Змінити валюту", callback_data="change_currency")]
])
