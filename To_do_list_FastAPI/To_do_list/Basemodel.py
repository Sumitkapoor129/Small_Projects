
from typing import Annotated, List, Optional
from fastapi import File, Form
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import String



class token_data(BaseModel):
    user_id:int      

class user_details(BaseModel):
    username:str
    Email:EmailStr
    password:str
    
class user_d_resp(BaseModel):
    user_id:int
    username:str
      
class task(BaseModel):
    task:str       
       