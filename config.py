# config.py
import os
from dotenv import load_dotenv

# Завантажуємо змінні з .env
load_dotenv()

# Токен бота та юзернейм
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME")

# Перевірка, чи задані обов'язкові змінні
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не заданий у змінних оточення")
if not BOT_USERNAME:
    raise ValueError("BOT_USERNAME не заданий у змінних оточення")

# Список адмінів
ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS", "").split(",") if x]

# Підтримувані мови та валюти
LANGUAGES = {"uk": "Українська", "en": "English", "ru": "Русский"}
CURRENCY_CHOICES = ["UAH", "USD", "RUB"]

# URL бази даних (SQLite для тесту)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./bot.db")

# Перевірка DATABASE_URL
if not DATABASE_URL:
    raise ValueError("DATABASE_URL не заданий!")
