from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

import Basemodels, Modules, database
router=APIRouter(tags=["HomePage"])

@router.get("/products",response_model=List[Basemodels.products_resp])
def get_Products(limit:int=10,offset:int=0,db:Session=Depends(database.get_ab)):
    products=db.query(Modules.Products).limit(limit).offset(offset).all()
    return products

@router.get("/Search")
def get_Products(id:int | None =None,Name:str | None =None,db:Session=Depends(database.get_ab)):
    if id !=None:
        product=db.query(Modules.Products).filter(Modules.Products.product_id==id).all()
        if product is None:
            raise HTTPException(404,detail="No Product with this ID found")
        return product
    elif Name!=None and id==None:
        product=db.query(Modules.Products).filter(Modules.Products.product==Name).all()
        if product is None:
            raise HTTPException(404,detail="No Product with this Name found")
        return product
    else:
        raise HTTPException(401,detail="Provide ID or Name of product to be searched")
    