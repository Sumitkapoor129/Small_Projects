from typing import Annotated, List
from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy.orm import Session

import Basemodels, Modules
import utils
from database import get_ab


router=APIRouter(tags=["Admins Only"])

@router.get("/users",response_model=List[Basemodels.register_resp])
def get_users(db:Session=Depends(get_ab),current_user:Basemodels.cu=Depends(utils.verify_access)):
    if current_user.role!="admin":
        print(current_user.role)
        raise HTTPException(409,detail="Unauthorized")
    users=db.query(Modules.users).all()
    return users
    
@router.post("/Add_product")
def add_product(product:Basemodels.addproduct,db:Session=Depends(get_ab),current_user:dict=Depends(utils.verify_access)):
    if current_user.role!="admin":
        print(current_user.role)
        raise HTTPException(409,detail="Unauthorized")
    new_product=Modules.Products(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return {"Added product":{new_product}}
    
@router.post("/block/{id}")
def block_user(id:int,db:Session=Depends(get_ab),current_user:dict=Depends(utils.verify_access)):
    if current_user.role!="admin":
        print(current_user["role"])
        raise HTTPException(409,detail="Unauthorized")   
    db.query(Modules.users).filter(Modules.users.user_id==id).update({"Role":"Blocked"})
    db.commit()
    return {"Status":"Successfull"}