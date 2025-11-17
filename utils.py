import sqlite3
from database import get_connection
from datetime import datetime
from config import REF_BONUS

def add_user(user_id: int, username: str = None, lang: str = "EN"):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO users(user_id, username, language, join_date) VALUES (?, ?, ?, ?)",
                (user_id, username, lang, datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()

def set_language(user_id: int, lang: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE users SET language = ? WHERE user_id = ?", (lang, user_id))
    conn.commit()
    conn.close()

def get_user(user_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    row = cur.fetchone()
    conn.close()
    return row

def update_balance(user_id: int, amount: float, currency: str = "USD", tx_type: str = "bonus"):
    conn = get_connection()
    cur = conn.cursor()
    # ensure user exists
    cur.execute("SELECT balance FROM users WHERE user_id = ?", (user_id,))
    r = cur.fetchone()
    if not r:
        cur.execute("INSERT INTO users(user_id, balance, currency, join_date) VALUES (?, ?, ?, ?)",
                    (user_id, amount, currency, datetime.utcnow().isoformat()))
    else:
        new_balance = r["balance"] + amount
        cur.execute("UPDATE users SET balance = ? WHERE user_id = ?", (new_balance, user_id))
    cur.execute("INSERT INTO transactions(user_id, type, amount, currency, date) VALUES (?, ?, ?, ?, ?)",
                (user_id, tx_type, amount, currency, datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()

def add_referral(inviter_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE users SET referrals_count = referrals_count + 1 WHERE user_id = ?", (inviter_id,))
    conn.commit()
    conn.close()

def create_withdraw_request(user_id:int, amount:float, currency:str, method:str, details:str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO withdraw_requests(user_id, amount, currency, method, details, status, date) VALUES (?, ?, ?, ?, ?, 'pending', ?)",
                (user_id, amount, currency, method, details, datetime.utcnow().isoformat()))
    conn.commit()
    req_id = cur.lastrowid
    conn.close()
    return req_id
