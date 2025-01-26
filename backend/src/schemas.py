from pydantic import BaseModel
from datetime import datetime

class CreateProduct(BaseModel):
    name: str
    count: int
    price: int
    descrpition: str
    order: str
    
class CreateOrder(BaseModel):
    # product_name: str
    product_id: int
    product_count: int
    user_id: int
    created_at: datetime
    
class CreateUser(BaseModel):
    username: str
    email: str
    number: int
    city: str
    
class EditProduct(BaseModel):
    name: str
    count: int
    description: str