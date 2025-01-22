from fastapi import APIRouter, Depends, HTTPException, status
from models.user import User
from sqlalchemy import insert, update, delete, select
from sqlalchemy.orm import Session
from backend.depends import get_db
from schemas import CreateUser
from typing import Annotated


router = APIRouter(tags=['админка'], prefix='/admin')

@router.get('/users')
async def check_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users

@router.post('/add_user')
async def add_user(db: Annotated[Session, Depends(get_db)], add_user: CreateUser):
    db.execute(insert(User).values(
        username=add_user.username,
        email=add_user.email,
        number=add_user.number,
        city=add_user.city,
    ))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 
            'transaction': 'user was successfuly created'}
    
@router.put('/update_balance/{user_id}')
async def update_balance(db: Annotated[Session, Depends(get_db)], 
                         user_id: int, new_balance: int):
    user = db.scalar(select(User).where(User.id == user_id))
    
    if user is None:
        return HTTPException(status.HTTP_404_NOT_FOUND, detail='user was not found')
    
    # user.balance += new_balance
    db.execute(update(User).values(balance=new_balance).where(User.id == user_id))
    db.commit()
    return {'status_code': status.HTTP_202_ACCEPTED,
            'transaction': 'balance for this user updated'}