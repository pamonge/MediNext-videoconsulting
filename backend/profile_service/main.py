from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from upload import router as profile_router
import os

app = FastAPI(
    title="Profile Service",
    description="Gestión de perfiles y subida de imágenes",
    version="1.0.0",
    docs_url="/docs",  # Habilita la documentación en /docs
    redoc_url="/redoc"  # Habilita documentación alternativa
)

# Endpoint raíz obligatorio
@app.get("/")
async def root():
    return {"service": "Profile Service", "status": "running"}

# Endpoint de salud
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Montar carpeta de imágenes como recurso estático
UPLOAD_DIR = "uploads/profile_pics"
os.makedirs(UPLOAD_DIR, exist_ok=True)
app.mount("/image", StaticFiles(directory=UPLOAD_DIR), name="profile_image")

# Incluir rutas SIN prefijo adicional
app.include_router(profile_router, tags=["Profile"])