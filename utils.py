from database import get_connection
from datetime import datetime

# Додає нового користувача в БД, якщо його ще немає
def add_user(user_id, username, currency="USD"):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    if cursor.fetchone() is None:
        cursor.execute(
            "INSERT INTO users (user_id, username, currency, join_date) VALUES (?, ?, ?, ?)",
            (user_id, username, currency, datetime.utcnow().isoformat())
        )
        conn.commit()
    conn.close()

# Отримує дані користувача
def get_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

# Оновлює баланс користувача (можна додати або відняти)
def update_balance(user_id, amount):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET balance = balance + ? WHERE user_id = ?", (amount, user_id))
    conn.commit()
    conn.close()

# Збільшує кількість рефералів у користувача
def add_referral(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET referrals_count = referrals_count + 1 WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()

# Створює запис про транзакцію
def add_transaction(user_id, type_, amount, currency="USD"):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO transactions (user_id, type, amount, currency, date) VALUES (?, ?, ?, ?, ?)",
        (user_id, type_, amount, currency, datetime.utcnow().isoformat())
    )
    conn.commit()
    conn.close()
