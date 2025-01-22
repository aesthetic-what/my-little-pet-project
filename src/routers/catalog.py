from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select, insert, delete, update
from backend.depends import get_db
from typing import Annotated
from models.catalog import Catalog
from schemas import CreateProduct
from datetime import datetime


router = APIRouter(prefix='/catalog', tags=['Каталог'])

@router.get('/')
async def manage_shop(db: Annotated[Session, Depends(get_db)]):
    products = db.scalars(select(Catalog)).all()
    return products

@router.get('/{product_id}')
async def take_product(db: Annotated[Session, Depends(get_db)], product_id: int):
    product = db.scalar(select(Catalog).where(Catalog.id == product_id))
    if product is None:
        return HTTPException(status.HTTP_404_NOT_FOUND, detail='product was not found')
    
    return product
    
@router.post('/add_product')
async def add_product_list(db: Annotated[Session, Depends(get_db)], add_product: CreateProduct):
    db.execute(insert(Catalog).values(
        name=add_product.name,
        count=add_product.count,
        price=add_product.price,
        description=add_product.descrpition,
        order=add_product.order,
        added_at=datetime.now()
    ))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED,
            'transaction': 'product was added in list'}
    
@router.put('/update_price/{product_id}')
async def update_price(db: Annotated[Session, Depends(get_db)], 
                       product_id: int, price: int):
    product = db.scalar(select(Catalog).where(Catalog.id == product_id))
    
    if product is None:
        return HTTPException(status.HTTP_404_NOT_FOUND, detail='product was not found')
    
    db.execute(update(Catalog).values(price=price).where(Catalog.id == product_id))
    db.commit()
    return {'status_code': status.HTTP_202_ACCEPTED,
            'transaction': 'price updated successful'}