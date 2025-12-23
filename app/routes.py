from fastapi import APIRouter

#para organizar las rutas, se creo una instacia.
router = APIRouter()

#definir ruta
@router.get("/health")

def health_check():
    return {"status" : "ok"}