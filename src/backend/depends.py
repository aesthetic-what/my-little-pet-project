from sqlalchemy.orm import SessionEvents, sessionmaker
# from sqlalchemy.ext.asyncio import AsyncSession
from .db import engine

Sessionlocal = sessionmaker(bind=engine)
# AsyncSessionLocal = sessionmaker(bind=async_engine, class_=AsyncSession)


def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()