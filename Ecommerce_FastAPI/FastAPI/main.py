from fastapi import FastAPI
from routes import users,admin,homepage,cart

app=FastAPI()
app.include_router(users.router)
app.include_router(admin.router)
app.include_router(homepage.router)
app.include_router(cart.router)