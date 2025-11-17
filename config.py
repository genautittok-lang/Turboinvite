import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS", "").split(",") if x]

LANGUAGES = {"uk": "Українська", "en": "English", "ru": "Русский"}
CURRENCY_CHOICES = ["UAH", "USD", "RUB"]

DATABASE_URL = os.getenv("DATABASE_URL")

# Додаємо цю змінну, щоб не було помилки
BOT_USERNAME = os.getenv("BOT_USERNAME", None)
