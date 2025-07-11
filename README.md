# 🩺 Plataforma Integral de Videoconsultas Médicas

Bienvenido a una plataforma moderna, escalable y segura para gestionar videoconsultas médicas en tiempo real. Este proyecto usa una arquitectura de microservicios en Python (FastAPI), frontend en React con Vite y despliegue mediante Docker Compose.

---

## 📦 Estructura del Proyecto
```
├── backend
│ ├── appointment_service # Gestión de turnos
│ ├── auth_service # Servicio de autenticación
│ ├── gateway # Puerta de enlace (API Gateway)
│ └── user_service # Gestión de usuarios
├── docker-compose.yml # Orquestador de servicios
└── frontend
└── vite-app # Aplicación React con Vite
```
## 🚀 Tecnologías Usadas

### Backend
- ⚙️ Python 3.11+
- ⚡ FastAPI
- 🧪 Pydantic
- 🐘 PostgreSQL
- 🐳 Docker + Docker Compose

### Frontend
- ⚛️ React + Vite
- 🎨 Tailwind CSS
- 📦 Axios (para consumo de APIs)

#### Levantar la app

sudo docker-compose up --build

#### Corroborar que los servicios esten activos

sudo docker-compose ps

#### Acceder a Swagger por microservicio

http://localhost:800[x]/docs