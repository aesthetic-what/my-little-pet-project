from src.backend.db import Base
from sqlalchemy import Column, String, Integer, DateTime, Float

class Catalog(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float,)
    count = Column(Integer, default=0)
    description = Column(String)
    order = Column(String)
    added_at = Column(DateTime)