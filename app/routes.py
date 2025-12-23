from fastapi import APIRouter
from app.models import User

#para organizar las rutas, se creo una instacia.
router = APIRouter()

#definir ruta
@router.get("/health")

#endpoint check
def health_check():
    return {"status" : "ok"}

@router.get("/users/me", response_model = User)

#endpoint usuarios
def read_current_user():
    return User (
        id = 1,
        email = "erikestrella73@gmail.com",
        full_name = "Erik Estrella Ojeda",
        is_active = True
        )