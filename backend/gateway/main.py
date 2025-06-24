from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute
from fastapi.security import OAuth2PasswordBearer
import httpx
import os

app = FastAPI()

# Configuración de CORS (para conectar con el frontend más adelante)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # cambiar por dominios reales en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Microservicios destino
SERVICES = {
    "auth": "http://auth_service:8000",
    "users": "http://user_service:8000",
    "appointments": "http://appointment_service:8000"
}

# Cliente HTTP para redirección
client = httpx.AsyncClient()

@app.api_route("/{service}/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def gateway(service: str, path: str, request: Request):
    if service not in SERVICES:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")

    # Construye la URL de destino
    target_url = f"{SERVICES[service]}/{path}"

    # Construye la petición con headers, body y método
    method = request.method
    headers = dict(request.headers)
    body = await request.body()

    try:
        response = await client.request(method, target_url, headers=headers, content=body)
        return JSONResponse(
            content=response.json(),
            status_code=response.status_code,
            headers=dict(response.headers),
        )
    except httpx.RequestError:
        raise HTTPException(status_code=503, detail="Microservicio no disponible")
