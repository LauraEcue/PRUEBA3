"""
FastAPI desde cero (sin base de datos)
----------------------------------------------
Una mini API de usuarios guardados en una lista en memoria.
Sirve para ver cómo FastAPI recibe, valida y responde.

Requisitos:
    pip install fastapi uvicorn

Ejecutar:
    uvicorn fastapi_simple:app --reload
    ó
    python -m uvicorn fastapi_simple:app --reload

Probar sin escribir ningún cliente:
    http://localhost:8000/docs
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# PASO 1: crear la aplicación
app = FastAPI(title="Mini API CHATUNINTEP")

# "Base de datos prueba" : una lista de diccionarios
usuarios = [
    {"id": 1, "nombre": "Ana Torres", "email": "ana@x.com", "password": "123"},
]


# PASO 2: definir la forma de los datos que esperamos recibir
class UsuarioIn(BaseModel):
    nombre: str
    email: str
    password: str


class LoginIn(BaseModel):
    email: str
    password: str


# PASO 3: el endpoint más simple posible (GET, sin datos de entrada)
@app.get("/")
def inicio():
    return {"mensaje": "Hola, la API está funcionando"}


# PASO 4: un GET con un parámetro en la dirección
@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"mensaje": f"Hola, {nombre}"}


# PASO 5: un POST que recibe datos en el cuerpo (JSON)
@app.post("/registro", status_code=201)
def registrar(datos: UsuarioIn):
    # Regla de negocio: el correo no puede repetirse
    for u in usuarios:
        if u["email"] == datos.email:
            raise HTTPException(status_code=400, detail="Ese correo ya está registrado")

    nuevo = {
        "id": len(usuarios) + 1,
        "nombre": datos.nombre,
        "email": datos.email,
        "password": datos.password,
    }
    usuarios.append(nuevo)

    # Nunca devolvemos la contraseña
    return {"id": nuevo["id"], "nombre": nuevo["nombre"], "email": nuevo["email"]}


# PASO 6: un POST que puede responder con error 401
@app.post("/login")
def login(datos: LoginIn):
    for u in usuarios:
        if u["email"] == datos.email and u["password"] == datos.password:
            return {"mensaje": f"Bienvenido, {u['nombre']}"}
    raise HTTPException(status_code=401, detail="Correo o contraseña incorrectos")


# PASO 7: un GET que devuelve una lista, con un filtro opcional (?buscar=...)
@app.get("/usuarios")
def listar(buscar: str = ""):
    resultado = [u for u in usuarios if buscar.lower() in u["nombre"].lower()]
    return [
        {"id": u["id"], "nombre": u["nombre"], "email": u["email"]} for u in resultado
    ]
