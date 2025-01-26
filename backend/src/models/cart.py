from src.backend.db import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Cart(Base):
    __tablename__ = 'cart'
    cart_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    # product_id = Column(Integer, index=True)
    # product_name = Column(String, index=True)
    # product_count = Column(Integer,)
    # summary = Column(Integer, index=True)
    status = Column(String, default='awaiting payment')
    created_at = Column(DateTime, index=True)
    
    items = relationship("CartItem", back_populates="cart")