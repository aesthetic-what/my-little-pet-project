from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select, update, insert
from backend.depends import get_db
from typing import Annotated
from models.user import User
from models.catalog import Catalog
from models.cart import Cart
from models.cart_items import CartItem
from schemas import CreateOrder
from datetime import datetime

router = APIRouter(prefix='/shop', tags=['Магазин'])

@router.get('/')
async def manage_shop(db: Annotated[Session, Depends(get_db)]):
    products = db.scalars(select(Catalog)).all()
    return products

@router.post('/buy_product/{product_id}')
async def buy_product(db: Annotated[Session, Depends(get_db)], 
                      product_id: int, count: int, user_id:int):
    product = db.scalar(select(Catalog).where(Catalog.id == product_id))
    if product is None:
        return HTTPException(status.HTTP_404_NOT_FOUND, detail="product was not found")
    
    if product.count == 0:
        return HTTPException(status.HTTP_502_BAD_GATEWAY, detail='product is empty')
    
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        return HTTPException(status.HTTP_404_NOT_FOUND, detail='user was not found')
    
    # Проверяем, есть ли у пользователя корзина
    cart = db.scalar(select(Cart).where(Cart.user_id == user_id, Cart.status == 'awaiting payment'))
    
    if not cart:
        # Если корзины нет, создаем новую
        cart = Cart(user_id=user_id, status='awaiting payment', created_at=datetime.now())
        db.add(cart)
        db.commit()
        db.refresh(cart)
        
    # Проверяем, есть ли уже товар в корзине
    cart_item = db.scalar(select(CartItem).where(CartItem.cart_id == cart.cart_id, CartItem.product_id == product_id))
    
    
    # db.execute(update(Catalog).where(Catalog.id == product_id).values(count=Catalog.count - 1))
    if cart_item:
        # Если товар уже есть, обновляем количество и сумму
        cart_item.product_count += count
        cart_item.summary = cart_item.product_count * product.price
    else:
        # Если товара нет в корзине, добавляем его
        cart_item = CartItem(
            cart_id=cart.cart_id,
            product_id=product_id,
            product_count=count,
            summary=product.price * count
        )
        db.add(cart_item)
    db.commit()
    product.count -= count
    return {'status_code': status.HTTP_202_ACCEPTED,
            'transaction': 'товар добавлен в корзину'}
    
@router.get('/search_product/{product_name}')
async def search_product(db: Annotated[Session, Depends(get_db)], product_name: str):
    product = db.scalar(select(Catalog).where(Catalog.name == product_name))
    if product is None:
        return HTTPException(status.HTTP_404_NOT_FOUND, detail='product was not found')
    return product