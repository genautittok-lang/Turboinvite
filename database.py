import sqlite3
import os
from datetime import datetime

# Створюємо папку для бази, якщо її немає
DB_DIR = "data"
DB_PATH = os.path.join(DB_DIR, "turbo.db")

if not os.path.exists(DB_DIR):
    os.makedirs(DB_DIR)

def get_connection():
    """Повертає з'єднання з базою даних SQLite"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    """Створює всі таблиці, якщо вони ще не існують"""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Користувачі
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            balance REAL DEFAULT 0,
            currency TEXT DEFAULT 'USD',
            referrals_count INTEGER DEFAULT 0,
            level TEXT DEFAULT 'Newbie',
            join_date TEXT
        )
    """)
    
    # Запити на вивід
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS withdraw_requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            amount REAL,
            method TEXT,
            details TEXT,
            status TEXT DEFAULT 'pending',
            date TEXT
        )
    """)
    
    # Транзакції
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            type TEXT,
            amount REAL,
            currency TEXT,
            date TEXT
        )
    """)
    
    # Замовлення на канали
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS channel_orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            channel_link TEXT,
            subscribers INTEGER,
            price REAL,
            status TEXT DEFAULT 'pending',
            date TEXT
        )
    """)
    
    # Досягнення
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS achievements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            achievement_type TEXT,
            date TEXT
        )
    """)
    
    conn.commit()
    conn.close()

# Викликаємо створення таблиць при імпорті
create_tables()
