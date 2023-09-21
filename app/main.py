from fastapi import FastAPI

from app.db import models
from app.db.database import Base, engine
from app.routers import post


app = FastAPI()
app.include_router(post.router)

@app.get('/hello')
def hello():
    return "Hello!"

models.Base.metadata.create_all(engine)

# @app.on_event("startup")
# def startup_event():
#     models.Base.metadata.drop_all(engine)
#     models.Base.metadata.create_all(engine)