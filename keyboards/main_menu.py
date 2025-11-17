# keyboards/main_menu.py
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="💰 Баланс", callback_data="balance")],
    [InlineKeyboardButton(text="💸 Вивід", callback_data="withdraw")],
    [InlineKeyboardButton(text="🎯 Заробляти", callback_data="earn")],
    [InlineKeyboardButton(text="🚀 Розкрутка", callback_data="promotion")],
    [InlineKeyboardButton(text="⭐ Telegram Stars", callback_data="stars")],
    [InlineKeyboardButton(text="⚙️ Налаштування", callback_data="settings")],
    [InlineKeyboardButton(text="👤 Профіль", callback_data="profile")],
    [InlineKeyboardButton(text="📞 Підтримка", callback_data="support")]
])
