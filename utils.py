# utils.py
from database import SessionLocal
from models import User

# Функція для отримання користувача за ID
def get_user(user_id: int):
    db = SessionLocal()
    try:
        user = db.query(User).filter_by(user_id=user_id).first()
        return user
    finally:
        db.close()
