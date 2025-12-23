# User Management API

## 📌 Descripción
Este proyecto es una API backend construida con **FastAPI**.  
Su propósito es servir como base inicial para un sistema de gestión de usuarios y demostrar buenas prácticas en la organización de proyectos Python.  

Actualmente incluye un endpoint de prueba `/health` que responde con el estado del servidor.

---

## 🚀 Cómo ejecutarlo

### 1. Clonar el repositorio
```bash
git clone https://github.com/tuusuario/user-management-api.git
cd user-management-api
```
### 2. Crear y activar entorno virtual
```bash
python -m venv venv 
source venv/bin/activate # Linux/Mac 
venv\Scripts\activate # Windows
```
### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```
### 4. Ejecutar el servidor
```bash
uvicorn main:app --reload
```
El servidor se levantara en:
```bash
http://127.0.0.1:8000
```
### Endpoint disponibles

GET/health
    respuesta:    
```bash
{ "status": "ok" }
```
### 🛠️ Tecnologías usadas

- Python 3.10+
-FastAPI → Framework para construir APIs rápidas y modernas.
-Uvicorn → Servidor ASGI para ejecutar la aplicación.
-Pydantic → Validación de datos (integrado en FastAPI).

### Estructura

```bash
user-management-api/
│
├── app/             # Código fuente de la aplicación
│   ├── __init__.py
│   └── routes.py    # Endpoints definidos
│
├── main.py          # Punto de entrada de la aplicación
├── requirements.txt # Dependencias del proyecto
└── README.md        # Documentación del proyecto

```
