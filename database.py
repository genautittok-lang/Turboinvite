import sqlite3
import os
from config import DB_PATH

def ensure_db_dir():
    d = os.path.dirname(DB_PATH)
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)

ensure_db_dir()

def get_connection():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            language TEXT DEFAULT 'EN',
            balance REAL DEFAULT 0,
            currency TEXT DEFAULT 'USD',
            referrals_count INTEGER DEFAULT 0,
            join_date TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS withdraw_requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            amount REAL,
            currency TEXT,
            method TEXT,
            details TEXT,
            status TEXT DEFAULT 'pending',
            date TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            type TEXT,
            amount REAL,
            currency TEXT,
            date TEXT
        )
    """)
    conn.commit()
    conn.close()

# створюємо таблиці під час імпорту
create_tables()
