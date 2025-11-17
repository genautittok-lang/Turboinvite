# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# URL бази даних. На Railway це може бути PostgreSQL, на локалі SQLite
# Наприклад, SQLite локально:
DATABASE_URL = "sqlite:///turbo.db"
# Якщо PostgreSQL на Railway, приклад:
# DATABASE_URL = "postgresql+asyncpg://username:password@host:port/dbname"

# Створюємо Base для моделей
Base = declarative_base()

# Створюємо движок та сесію
engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def init_db():
    """
    Ініціалізація бази даних:
    - Імпортуємо всі моделі всередині функції, щоб уникнути циклічного імпорту
    - Створюємо всі таблиці
    """
    import models  # тут імпорт моделей всередині функції
    Base.metadata.create_all(bind=engine)
