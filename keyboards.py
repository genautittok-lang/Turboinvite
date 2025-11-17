from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu(lang="EN"):
    texts = {
        "UA": ["💰 Баланс", "💸 Вивід", "🎯 Заробляти", "🚀 Розкрутка", "⭐ Telegram Stars", "⚙️ Налаштування", "📞 Підтримка"],
        "EN": ["💰 Balance", "💸 Withdraw", "🎯 Earn", "🚀 Promotion", "⭐ Telegram Stars", "⚙️ Settings", "📞 Support"],
        "RU": ["💰 Баланс", "💸 Вывод", "🎯 Заработать", "🚀 Продвижение", "⭐ Telegram Stars", "⚙️ Настройки", "📞 Поддержка"]
    }
    btns = texts.get(lang, texts["EN"])
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=btns[0], callback_data="balance")],
        [InlineKeyboardButton(text=btns[1], callback_data="withdraw")],
        [InlineKeyboardButton(text=btns[2], callback_data="earn")],
        [InlineKeyboardButton(text=btns[3], callback_data="promo")],
        [InlineKeyboardButton(text=btns[4], callback_data="stars")],
        [InlineKeyboardButton(text=btns[5], callback_data="settings")],
        [InlineKeyboardButton(text=btns[6], callback_data="support")]
    ])
    return kb

def language_menu():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🇺🇦 Українська", callback_data="lang_UA")],
        [InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_EN")],
        [InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_RU")]
    ])
    return kb

def back_to_menu(lang="EN"):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Back", callback_data="back")],
        [InlineKeyboardButton(text="🏠 Menu", callback_data="menu")]
    ])
