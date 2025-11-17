import os

# === Основні налаштування бота ===
# Токен бота з @BotFather
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

# Username бота без @
BOT_USERNAME = os.getenv("BOT_USERNAME", "TurboInviteBot")

# ID адміністратора
ADMIN_ID = int(os.getenv("ADMIN_ID", 123456789))

# Валюта балансу за замовчуванням
DEFAULT_CURRENCY = "USD"

# Мінімальні суми на вивід
MIN_WITHDRAW = {
    "USD": 0.25,   # 0.25$
    "UAH": 10,     # 10 грн
    "RUB": 25      # 25 руб
}

# === Підтримувані валюти ===
CURRENCIES = ["USD", "UAH", "RUB"]

# === Текст мов ===
SUPPORTED_LANGUAGES = ["ua", "ru", "en"]

# === Комісії реферальної системи ===
REF_BONUS = {
    "USD": 0.25,
    "UAH": 10,
    "RUB": 25
}

# === Директория БД (SQLite) ===
DB_PATH = "database.db"
