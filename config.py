import os

BOT_TOKEN = os.getenv("BOT_TOKEN")  # встанови в середовищі (Railway -> Environment)
ADMIN_ID = int(os.getenv("ADMIN_ID", "123456789"))  # підстав свій Telegram ID
DB_PATH = os.getenv("DB_PATH", "data/turbo.db")

DEFAULT_CURRENCY = "USD"
MIN_WITHDRAW = {"USD": 50, "UAH": 500, "RUB": 1000}

# реферальні бонуси (у відповідних валютах)
REF_BONUS = {"USD": 0.25, "UAH": 10.0, "RUB": 25.0}
