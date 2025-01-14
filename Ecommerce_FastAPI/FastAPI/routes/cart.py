
from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

import Basemodels
import Modules, database, utils
router=APIRouter(tags=["Your Cart"])

@router.get("/Add_to_cart/{id}")
def add_to_cart(id:int,db:Session=Depends(database.get_ab),cu=Depends(utils.verify_access)):
    if cu.role=="Blocked":
        raise HTTPException(409,detail="You are Blocked from using this service")
    productN=db.query(Modules.Products).filter(Modules.Products.product_id==id).first()
    
    new=Modules.Cart(user_id=cu.user_id,products_id=id,product=productN.product)
    db.add(new)
    db.commit() 
    db.refresh(new)
    return new

@router.get("/show_cart")
def show_cart(db:Session=Depends(database.get_ab),cu=Depends(utils.verify_access)):
    products=db.query(Modules.Cart.product).filter(Modules.Cart.user_id==cu.user_id).all()
    product_list = [product for (product,) in products] 
    if product_list ==[]:
        return {"nothing in the cart right now"}
    return jsonable_encoder(product_list)
    
@router.delete("/cart/remove/{id}")
def remove_from_cart(id:int,db:Session=Depends(database.get_ab),cu=Depends(utils.verify_access)):
    product=db.query(Modules.Cart).filter(Modules.Cart.products_id==id)
    pro=product.all()
    for pr in pro:
        if pr is None:
            raise HTTPException(404,detail="Not found in your cart")
        if pr.user_id==cu.user_id:
            product.delete(synchronize_session=False)
            db.commit()
        else:
            raise HTTPException(404,detail="Not found in your cart")  
    return {"Status":"Successfull"}      
        
@router.get("/Checkout",response_model=Basemodels.OrderSchema)
def checkout(db:Session=Depends(database.get_ab),cu=Depends(utils.verify_access)):
    products_q=db.query(Modules.Cart).filter(Modules.Cart.user_id==cu.user_id)
    products=products_q.all()
    total_price=0
    products_list=[]
    final_order=Modules.Order(user_id=cu.user_id)
    for product in products:
        products_list.append(product.product)
        price=db.query(Modules.Products.price).filter(Modules.Products.product_id==product.products_id).first()
        total_price+=price[0]
    result = ', '.join(str(x) for x in products_list)    
    final_order.product=result    
    final_order.Total=total_price
    products_q.delete(synchronize_session=False)
    db.add(final_order)
    db.commit()
    db.refresh(final_order)    
    return final_order

@router.post("/cancel/{id}")
def cancel_order(id:int,db:Session=Depends(database.get_ab),cu=Depends(utils.verify_access)):
    order=db.query(Modules.Order).filter(Modules.Order.Order_id==id).first()
    order.status="Cancelled"
    db.commit()
    return {"Status":"Order Cancelled"}
    