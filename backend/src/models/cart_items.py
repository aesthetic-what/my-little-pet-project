from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.backend.db import Base

class CartItem(Base):
    __tablename__ = 'cart_items'
    cart_item_id = Column(Integer, primary_key=True, index=True)
    cart_id = Column(Integer, ForeignKey('cart.cart_id'))
    product_id = Column(Integer, ForeignKey('products.id'))  # Связь с товарами
    product_count = Column(Integer)
    summary = Column(Integer)  # Общая цена для этого товара

    # Связи с другими таблицами
    cart = relationship("Cart", back_populates="items")
    product = relationship("Catalog")
