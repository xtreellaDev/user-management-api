from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#URL de conexión a la base de datos SQLite.
#El archivo se creará automáticamente si no existe.
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

#Engine: gestiona la conexión física con la base de datos.
#'check_same_thread' es requerido por SQLite cuando se usa con FastApi
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

#SessionLocal: fábrica de sesiones para interactuar con la base de datos
#Cada request debe usar su propia sesión
SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind= engine
)

#Base: clase base para todos los modelos ORM
#SQLAlchemy la usa para generar las tablas
Base = declarative_base()