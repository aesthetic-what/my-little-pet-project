from backend.db import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, index=True)
    balance = Column(Integer, default=0, index=True)
    email = Column(String, nullable=True)
    number = Column(Integer, nullable=False)
    city = Column(String, nullable=False, index=True)
    
    # cart_id = Column(Integer, ForeignKey('cart.cart_id'))