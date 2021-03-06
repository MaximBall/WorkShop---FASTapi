from fastapi import FastAPI
from . import tables
from database import engine
from .api import router

tables.Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(router)