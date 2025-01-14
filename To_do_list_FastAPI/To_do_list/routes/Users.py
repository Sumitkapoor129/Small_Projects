
from fastapi import APIRouter, Depends, Form, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import Module, db,util
import Basemodel
from fastapi.responses import FileResponse, HTMLResponse


router=APIRouter(tags=["Users"])
@router.post("/Register",response_model=Basemodel.user_d_resp)
def register(details:Basemodel.user_details,db:Session=Depends(db.get_db)):
    details.password=util.hash_pass(details.password)
    newuser=Module.users(**details.dict())
    db.add(newuser)
    db.commit()
    db.refresh(newuser)
    return newuser

@router.post("/Login")
def login(creds:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(db.get_db)):
    user= db.query(Module.users).filter(Module.users.username==creds.username).first()
    if user is None:
        raise HTTPException(404,detail="Invalid credentials")
    if util.verify(creds.password,user.password):
        data2={"user_id":user.user_id}
        token=util.get_access_token(data=data2)
        return {"access_token":token,"token_type":"bearer"}