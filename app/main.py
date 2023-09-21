from fastapi import FastAPI

from app.db import models
from app.db.database import Base, engine

app=FastAPI()

@app.get('/')
def hello():
    return "Hello!"


@app.on_event("startup")
def startup_event():
    models.Base.metadata.drop_all(engine)
    models.Base.metadata.create_all(engine)