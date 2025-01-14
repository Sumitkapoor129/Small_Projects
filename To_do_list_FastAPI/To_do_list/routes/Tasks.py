
from fastapi import APIRouter, Depends, Form, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import Module, db,util
import Basemodel
from fastapi.responses import FileResponse, HTMLResponse


router=APIRouter(tags=["Tasks"])
@router.post("/Add_task")
def addtask(task:Basemodel.task,db:Session=Depends(db.get_db),user=Depends(util.verify_access)):
    new_task=Module.tasks(**task.dict(),user_id=user.user_id)
    db.add(new_task)
    db.commit()
    return {"Status":"Task Added"}

@router.get("/myTasks")
def myTasks(db:Session=Depends(db.get_db),user=Depends(util.verify_access)):
    tasks=db.query(Module.tasks).filter(Module.tasks.user_id==user.user_id,Module.tasks.status=="On Going").all()
    task=[{t.task:t.task_id} for t in tasks]
    return task

@router.get("/MarkComplete/{task_id}")
def markcomplete(task_id,db:Session=Depends(db.get_db),user=Depends(util.verify_access)):
    task=db.query(Module.tasks).filter(Module.tasks.user_id==user.user_id,Module.tasks.task_id==task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.status="Completed"
    db.commit()
    return {"Status":"Updated"}
    
@router.get("/TaskHistory")
def history(db:Session=Depends(db.get_db),user=Depends(util.verify_access)):
    tasks=db.query(Module.tasks).filter(Module.tasks.user_id==user.user_id).order_by(-Module.tasks.task_id).all()
    if not tasks:
        raise HTTPException(detail="Add your First Task to get Started")
    return tasks
        