from database import get_connection
from datetime import datetime

def add_user(user_id, username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,))
    if not cursor.fetchone():
        cursor.execute(
            "INSERT INTO users (user_id, username, join_date) VALUES (?, ?, ?)",
            (user_id, username, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        )
        conn.commit()
    conn.close()

def update_balance(user_id, amount):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET balance = balance + ? WHERE user_id = ?", (amount, user_id))
    conn.commit()
    conn.close()

