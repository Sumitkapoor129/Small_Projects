from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import jwt,JWTError

import Basemodels


hasher=CryptContext(schemes=["bcrypt"],deprecated="auto")
def hash_pass(password):
    return hasher.hash(password)
def verify(plain_pass:str,hashed_pass:str):
    return hasher.verify(plain_pass,hashed_pass) 


Secret_Key="sy38erugvbn"
Algorithm="HS256"
times:int=10

def get_access_token(data:dict):
    data_to_encode=data.copy()
    expiration=datetime.utcnow()+timedelta(minutes=times)
    data_to_encode.update({"exp":expiration})
    token=jwt.encode(data_to_encode,Secret_Key,algorithm=Algorithm)
    return token

token_retriver=OAuth2PasswordBearer(tokenUrl="/Login")
#FAULT HERE 
def verify_access(token:str=Depends(token_retriver)):
    try:
        data=jwt.decode(token,Secret_Key,algorithms=[Algorithm])
        user_id=data.get("user_id")
        if user_id is None:
            raise HTTPException(404,detail="Invalid token")
        role=data.get("Role")
        token_data=Basemodels.token_data(user_id=user_id,role=role)
        return token_data
    except JWTError:
        raise HTTPException(401,detail="Authorization failed")
