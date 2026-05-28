from fastapi import FastAPI
from database import engine
import models
from routers import todos, users

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(todos.router)
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Todo API is running!"}