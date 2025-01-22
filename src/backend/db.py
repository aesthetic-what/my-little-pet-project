# from sqlalchemy import create_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

database_url = 'postgresql+psycopg2://timur:pass@176.124.202.220:5432/shop'
# engine = create_engine(database_url)
engine = create_engine(database_url)

# class Base(DeclarativeBase):
#     pass