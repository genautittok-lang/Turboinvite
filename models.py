# models.py
from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    username = Column(String, nullable=True)
    balance = Column(Float, default=0)
    currency = Column(String, default="USD")
    referrals_count = Column(Integer, default=0)
    level = Column(String, default="Newbie")
    join_date = Column(DateTime(timezone=True), server_default=func.now())

class WithdrawRequest(Base):
    __tablename__ = "withdraw_requests"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    method = Column(String, nullable=False)
    details = Column(Text, nullable=True)
    status = Column(String, default="pending")
    date = Column(DateTime(timezone=True), server_default=func.now())

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    type = Column(String)  # "deposit", "withdraw", "referral_bonus"
    amount = Column(Float)
    currency = Column(String, default="USD")
    date = Column(DateTime(timezone=True), server_default=func.now())

class ChannelOrder(Base):
    __tablename__ = "channel_orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    channel_link = Column(String, nullable=False)
    subscribers = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    status = Column(String, default="pending")
    date = Column(DateTime(timezone=True), server_default=func.now())

class Achievement(Base):
    __tablename__ = "achievements"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    achievement_type = Column(String)
    date = Column(DateTime(timezone=True), server_default=func.now())
