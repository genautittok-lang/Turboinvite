# database.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL
from models import Base  # Мета-дані моделей

# Створюємо асинхронний двигун SQLAlchemy (для PostgreSQL буде asyncpg)
engine = create_async_engine(
    DATABASE_URL, echo=False, future=True
)
# Сесійний локатор (для отримання AsyncSession)
SessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def init_db():
    """Створює таблиці в БД, якщо їх ще немає."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
