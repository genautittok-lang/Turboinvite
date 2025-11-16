# Turboinvite[README_Version2.md](https://github.com/user-attachments/files/23571591/README_Version2.md)
# TurboInviteBot

Повноцінний Telegram-бот для заробітку на рефералах, розкрутки каналів, купівлі Telegram Stars та управління балансом.

## Запуск на Railway

1. **Склонуйте проект:**
   ```
   git clone https://github.com/genautittok-lang/Turboinvite.git
   cd Turboinvite
   ```

2. **Встановіть залежності:**
   ```
   pip install -r requirements.txt
   ```

3. **Додайте у Railway Secrets/Variables:**
   - `BOT_TOKEN` — отримайте у @BotFather
   - `BOT_USERNAME` — без @ (наприклад TurboInviteBot)
   - `ADMIN_ID` — ваш Telegram ID для адмінки

4. **Створіть папку data/** (якщо ще немає)
   ```
   mkdir data
   ```

5. **Запуск:**
   ```
   python main.py
   ```

## Структура проекту

- `main.py` — запускає бота та реєструє всі хендлери
- `handlers/` — вся логіка роботи
- `database.py` — SQLite база даних
- `requirements.txt` — залежності
- `README.md` — інструкції

## Мови і дизайн

- UA / EN / RU
- Темна/світла тема, інлайн-кнопки з емодзі

---

## Розширення

- Додавайте свої функції у handlers/*.py
- Для розсилки, розкрутки, Stars, адмін-функцій — розширюйте логіку у відповідних файлах
