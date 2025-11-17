# config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Завантажує змінні з .env (локально) при потребі

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Токен Telegram-бота
ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS", "").split(",") if x]  # ID адміністраторів

# Підтримувані мови та валюти
LANGUAGES = {"uk": "Українська", "en": "English", "ru": "Русский"}
CURRENCY_CHOICES = ["UAH", "USD", "RUB"]

# URL бази даних (для PostgreSQL можна використовувати DATABASE_URL з Railway)
DATABASE_URL = os.getenv("DATABASE_URL")
