from fastapi import FastAPI
from app import routes

app= FastAPI()

#incluir rutas (routes.py)
app.include_router(routes.router)

#iniciar proyecto con uvicorn main:app --reload