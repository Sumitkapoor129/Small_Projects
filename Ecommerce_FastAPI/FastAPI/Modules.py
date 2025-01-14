
from sqlalchemy import Column, ForeignKey, Integer, LargeBinary, String
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()




class users(Base):
    __tablename__="users"
    user_id=Column(Integer,primary_key=True,autoincrement=True)
    username=Column(String,unique=True,nullable=False)
    Email=Column(String,unique=True,nullable=False)
    password=Column(String,nullable=False)
    Role=Column(String,server_default="Customer")
    

class Products(Base):
    __tablename__="Products"
    product_id=Column(Integer,primary_key=True,autoincrement=True)
    product=Column(String,unique=True,nullable=False)
    price=Column(Integer,nullable=False)
    quantity=Column(Integer,nullable=False)
    image=Column(LargeBinary(length=(16 * 1024 * 1024)),nullable=True)
    description=Column(String,server_default="No description Available")  
    
class Cart(Base):
    __tablename__="Cart"
    user_id=Column(Integer,ForeignKey("users.user_id",ondelete="CASCADE"),nullable=False)
    products_id=Column(Integer,ForeignKey("Products.product_id",ondelete="CASCADE"),nullable=False)
    product=Column(String,nullable=False,primary_key=True)  
    
class Order(Base):
    __tablename__="Orders"
    Order_id=Column(Integer,primary_key=True,autoincrement=True)
    user_id=Column(Integer,ForeignKey("users.user_id",ondelete="CASCADE"),nullable=False,)
    product=Column(String,nullable=False)
    Total=Column(Integer,nullable=False)
    status=Column(String,nullable=False,server_default="Placed")
        
    

   