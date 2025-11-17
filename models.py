# models.py
from sqlalchemy import Column, Integer, BigInteger, Float, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, unique=True, index=True)  # Telegram ID
    name = Column(String, nullable=False)
    language = Column(String, default='uk')
    currency = Column(String, default='UAH')
    balance = Column(Float, default=0.0)
    invited = Column(Integer, default=0)    # Кількість запрошених
    level = Column(String, default='Newbie')
    is_banned = Column(Boolean, default=False)
    referrer_id = Column(Integer, ForeignKey('users.user_id'), nullable=True)
    # Зв'язок до користувача-реферера (якщо потрібно)
    referrer = relationship("User", remote_side=[user_id], backref="referrals")

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    type = Column(String)           # Наприклад: 'deposit', 'withdraw', 'referral_bonus'
    amount = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
    description = Column(String)
