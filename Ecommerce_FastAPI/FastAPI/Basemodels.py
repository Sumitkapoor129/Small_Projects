
from typing import Annotated, List, Optional
from fastapi import File, Form
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import String

    
class register_resp(BaseModel):
    username:str
    user_id:int
    
class login(BaseModel):
    email:EmailStr
    password:str   

class login_resp(BaseModel):
    token:str    
    
class token_data(BaseModel):
    user_id:int
    role:str       
       
class addproduct(BaseModel):
    product:str
    price:int
    quantity:int
    description:Optional[str]  
    
class filter_product(BaseModel):
    limit:int=Field(10,le=20,gt=0)
    offset: int = Field(0, ge=0)     
    
class products_resp(BaseModel):
    product:str
    price:int
    product_id:int
    
     
class cu(BaseModel):
    user_id:int
    role:str
    
class OrderSchema(BaseModel):
    user_id: int
    Total: float
    status:str

    class Config:
        orm_mode = True    