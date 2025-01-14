from fastapi import FastAPI,APIRouter
from routes import Users,Tasks
app=FastAPI()
app.include_router(Users.router)
app.include_router(Tasks.router)