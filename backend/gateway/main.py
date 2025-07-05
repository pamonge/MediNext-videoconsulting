from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute
import httpx
import os

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Microservicios destino
SERVICES = {
    "auth": "http://auth_service:8000",
    "users": "http://user_service:8000",
    "appointments": "http://appointment_service:8000",
    "profiles": "http://profile_service:8000"
}

# Cliente HTTP para redirección
client = httpx.AsyncClient()

@app.get("/")
async def root():
    return {"message": "API Gateway - Servicios disponibles", "services": list(SERVICES.keys())}

@app.get("/docs", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs/")

@app.api_route("/{service}/{path:path}", 
              methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
              #operation_id="route_to_{service}")  # Operation ID único por servicio
async def gateway(service: str, path: str, request: Request):
    if service not in SERVICES:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")

    if path.strip("/") == "docs":
        target_url = f"{SERVICES[service]}/docs"
    else:
        clean_path = path.lstrip("/")
        target_url = f"{SERVICES[service]}/{clean_path}" if clean_path else SERVICES[service]

    # Limpiar path (remover slash inicial si existe)
    clean_path = path.lstrip("/")
    target_url = f"{SERVICES[service]}/{clean_path}" if clean_path else SERVICES[service]

    # Preparar headers (remover algunos que pueden causar problemas)
    headers = {
        k: v for k, v in request.headers.items() 
        if k.lower() not in ["host", "content-length"]
    }
    
    # Añadir header de autorización si existe
    if "authorization" in request.headers:
        headers["authorization"] = request.headers["authorization"]

    try:
        # Hacer la petición al microservicio
        response = await client.request(
            request.method,
            target_url,
            headers=headers,
            content=await request.body(),
            timeout=30.0
        )
        
        # Manejar respuesta
        if response.headers.get("content-type") == "application/json":
            content = response.json()
        else:
            content = response.text

        return JSONResponse(
            content=content,
            status_code=response.status_code,
            headers=dict(response.headers),
        )
    except httpx.ConnectError:
        raise HTTPException(
            status_code=503, 
            detail=f"Microservicio {service} no disponible"
        )
    except httpx.TimeoutException:
        raise HTTPException(
            status_code=504, 
            detail=f"Timeout al conectar con {service}"
        )