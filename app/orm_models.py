from sqlalchemy import Column, Integer, String, Boolean
from app.db import Base

#Modelo ORM que representa la tabla 'users' en la base de datos
class UserORM(Base):
    __tablename__ = "users"

    #Identificador unico de usuario
    id = Column(Integer, primary_key= True, index= True)
    #Correo electronico del usuario(unico)
    email = Column(String, unique= True, index= True)
    #Nombre completo del usuario
    full_name = Column(String)
    #Indica si el usuario esta activo
    is_active = Column(Boolean, default= True)