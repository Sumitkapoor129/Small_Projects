from fastapi.background import P
from sqlalchemy import ARRAY, Boolean, Column, ForeignKey, Integer, LargeBinary, String
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class users(Base):
    __tablename__="users"
    user_id=Column(Integer,primary_key=True,autoincrement=True)
    username=Column(String,unique=True,nullable=False)
    Email=Column(String,unique=True,nullable=False)
    password=Column(String,nullable=False)
    
class tasks(Base):
    __tablename__="tasks"
    task_id=Column(Integer,primary_key=True,autoincrement=True)
    task=Column(String,unique=True,nullable=False)    
    user_id=Column(Integer,ForeignKey("users.user_id",ondelete="CASCADE"),nullable=False)
    status=Column(Boolean,default=True)