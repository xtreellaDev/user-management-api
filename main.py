from fastapi import FastAPI
from app import routes
from app.orm_models import Base
from app.db import engine

app= FastAPI()

#incluir rutas (routes.py)
app.include_router(routes.router)

#iniciar proyecto con uvicorn main:app --reload

Base.metadata.create_all(bind=engine)
