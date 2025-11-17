from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# --- Меню головне ---
def main_menu(lang="EN"):
    texts = {
        "UA": ["💰 Баланс", "💸 Вивід", "🎯 Заробляти", "🚀 Розкрутка", "⭐ Telegram Stars", "⚙️ Налаштування", "📞 Підтримка"],
        "EN": ["💰 Balance", "💸 Withdraw", "🎯 Earn", "🚀 Promotion", "⭐ Telegram Stars", "⚙️ Settings", "📞 Support"],
        "RU": ["💰 Баланс", "💸 Вывод", "🎯 Заработать", "🚀 Продвижение", "⭐ Telegram Stars", "⚙️ Настройки", "📞 Поддержка"]
    }
    btns = texts.get(lang, texts["EN"])
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=btns[0], callback_data="balance")],
            [InlineKeyboardButton(text=btns[1], callback_data="withdraw")],
            [InlineKeyboardButton(text=btns[2], callback_data="earn")],
            [InlineKeyboardButton(text=btns[3], callback_data="promo")],
            [InlineKeyboardButton(text=btns[4], callback_data="stars")],
            [InlineKeyboardButton(text=btns[5], callback_data="settings")],
            [InlineKeyboardButton(text=btns[6], callback_data="support")]
        ]
    )
    return kb

# --- Меню вибору мови ---
def language_menu():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🇺🇦 Українська", callback_data="lang_ua")],
            [InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en")],
            [InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru")]
        ]
    )
    return kb

# --- Приклади інших клавіатур (для розкрутки, виводу, Stars) ---
def withdraw_menu():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💳 Банківська карта", callback_data="withdraw_card")],
            [InlineKeyboardButton(text="💰 Крипта TRC20 USDT", callback_data="withdraw_crypto")],
            [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_main")]
        ]
    )
    return kb

def promotion_menu():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📤 Скопіювати реф. посилання", callback_data="copy_ref")],
            [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_main")]
        ]
    )
    return kb

def stars_menu():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💎 Купити 100 Stars", callback_data="buy_100_stars")],
            [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_main")]
        ]
    )
    return kb
