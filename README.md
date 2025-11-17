# Telegram Bot

This Telegram bot supports Ukrainian, English, Russian, multi-currency, referrals, withdrawals, and an admin panel.

## Setup

1. **Встановіть залежності**: `pip install -r requirements.txt`.
2. **Налаштуйте змінні оточення**:
   - `BOT_TOKEN` – токен вашого бота (заведений у BotFather).
   - `ADMIN_IDS` – (опціонально) список ID адмінів через кому.
   - `DATABASE_URL` – (для PostgreSQL) URL підключення до бази даних.
3. **Додайте PostgreSQL сервіс на Railway**. Railway автоматично створить `DATABASE_URL` для з’єднання:contentReference[oaicite:12]{index=12}.
4. **Procfile**: має містити рядок `worker: python main.py`, щоб Railway знало, як запускати бота:contentReference[oaicite:13]{index=13}.
5. **Запуск на Railway**:
   - Підключіть репозиторій до Railway (через GitHub або Railway CLI).
   - Деплой відбудеться автоматично після пушу в гілку. Бот запуститься з Long Polling.

## Використані ресурси

- Документація Aiogram 3.x (і приклади коду):contentReference[oaicite:14]{index=14}:contentReference[oaicite:15]{index=15}.
- Системи перекладу Aiogram (gettext, Babel):contentReference[oaicite:16]{index=16}.
- Railway: додавання PostgreSQL сервісу та змінних оточення:contentReference[oaicite:17]{index=17}:contentReference[oaicite:18]{index=18}.
- Інші бібліотеки: SQLAlchemy для ORM, python-dotenv для читання `.env`.
