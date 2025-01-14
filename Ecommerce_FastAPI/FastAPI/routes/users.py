from fastapi import APIRouter, Depends, Form, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import Modules, database,utils
import Basemodels
from fastapi.responses import FileResponse, HTMLResponse


router=APIRouter(tags=["Users"])

@router.get("/")
def homepage():
    return FileResponse("C:\\Users\\91983\\Desktop\\WebDev\\AI\\Login.html")

@router.get("/signup")
def Signup():
    return FileResponse("C:\\Users\\91983\\Desktop\\WebDev\\AI\\signup.html")



@router.post("/Register",response_model=Basemodels.register_resp)
def register(    username: str = Form(...), 
    email: str = Form(...), 
    password: str = Form(...), 
    db: Session = Depends(database.get_ab)):
    password=utils.hash_pass(password)
    details = {
        "username": username,
        "Email": email,
        "password": password
    }
    
    new_user=Modules.users(**details)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return FileResponse("C:\\Users\\91983\\Desktop\\WebDev\\AI\\Login.html")

@router.post("/Login")
def login(creds:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_ab)):
    user= db.query(Modules.users).filter(Modules.users.Email==creds.username).first()
    if user is None:
        raise HTTPException(404,detail="Invalid credentials")
    if utils.verify(creds.password,user.password):
        data2={"user_id":user.user_id,"Role":user.Role}
        token=utils.get_access_token(data=data2)
        return {"access_token":token,"token_type":"bearer"}