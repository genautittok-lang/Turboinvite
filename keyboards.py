from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu(lang="EN"):
    texts = {
        "UA": ["💰 Баланс", "💸 Вивід", "🎯 Заробляти", "🚀 Розкрутка", "⭐ Telegram Stars", "⚙️ Налаштування", "📞 Підтримка"],
        "EN": ["💰 Balance", "💸 Withdraw", "🎯 Earn", "🚀 Promotion", "⭐ Telegram Stars", "⚙️ Settings", "📞 Support"],
        "RU": ["💰 Баланс", "💸 Вывод", "🎯 Заработать", "🚀 Продвижение", "⭐ Telegram Stars", "⚙️ Настройки", "📞 Поддержка"]
    }
    btns = texts.get(lang, texts["EN"])
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(btns[0], callback_data="balance")],
        [InlineKeyboardButton(btns[1], callback_data="withdraw")],
        [InlineKeyboardButton(btns[2], callback_data="earn")],
        [InlineKeyboardButton(btns[3], callback_data="promo")],
        [InlineKeyboardButton(btns[4], callback_data="stars")],
        [InlineKeyboardButton(btns[5], callback_data="settings")],
        [InlineKeyboardButton(btns[6], callback_data="support")]
    ])
    return kb

def language_menu():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("🇺🇦 Українська", callback_data="lang_ua")],
        [InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")],
        [InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru")]
    ])
    return kb
