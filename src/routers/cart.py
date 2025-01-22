from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy import select, update, insert
from sqlalchemy.orm import Session
from backend.depends import get_db
from typing import Annotated
from models.cart import Cart
from models.cart_items import CartItem
from models.user import User


router = APIRouter(tags=['корзина'], prefix='/cart')

@router.get('/cart_list')
async def check_carts(db: Annotated[Session, Depends(get_db)]):
    carts = db.scalars(select(Cart)).all()
    return carts

@router.post('/pay_cart/{cart_id}')
async def pay_order(db: Annotated[Session, Depends(get_db)], cart_id: int):
    # Получаем корзину
    cart = db.scalar(select(Cart).where(Cart.cart_id == cart_id))
    
    if cart is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Cart not found')

    # Получаем пользователя, которому принадлежит корзина
    user = db.scalar(select(User).where(User.id == cart.user_id))
    
    if user is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='User not found')

    # Получаем все товары в корзине
    cart_items = db.scalars(select(CartItem).where(CartItem.cart_id == cart.cart_id)).all()

    # Рассчитываем общую сумму всех товаров в корзине
    total_summary = sum(item.summary for item in cart_items)

    # Проверка на достаточность средств у пользователя
    if user.balance == 0 or user.balance < total_summary:
        raise HTTPException(status.HTTP_406_NOT_ACCEPTABLE, detail='Not enough funds')

    # Обновляем статус корзины на "paid"
    db.execute(update(Cart).values(status='paid').where(Cart.cart_id == cart_id))

    # Вычитаем стоимость товаров из баланса пользователя
    db.execute(update(User).values(balance=user.balance - total_summary).where(User.id == user.id))

    # Сохраняем изменения
    db.commit()

    return {'status_code': status.HTTP_202_ACCEPTED,
            'transaction': 'Successful payment'}

    
    
@router.get('/cart_items')
async def cartitems(db: Annotated[Session, Depends(get_db)]):
    cart_items = db.scalars(select(CartItem)).all()
    return cart_items