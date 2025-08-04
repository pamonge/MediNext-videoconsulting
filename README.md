# 🩺 Plataforma Integral de Videoconsultas Médicas

Bienvenido a una plataforma moderna, escalable y segura para gestionar videoconsultas médicas en tiempo real. Este proyecto usa una arquitectura de microservicios en Python (FastAPI), frontend en React con Vite y despliegue mediante Docker Compose.

---

## 📦 Estructura del Proyecto
```
├── backend
│   ├── affiliation_service
│   ├── authorization_service
│   ├── document_service
│   ├── gateway_service
│   ├── medical_history_service
│   ├── payment_service
│   ├── plan_service
│   ├── profile_service
│   └── user_service
├── docker-compose.yml
├── frontend
│   └── vite-app
├── README.md
└── venv
    ├── bin
    ├── include
    ├── lib
    ├── lib64 -> lib
    └── pyvenv.cfg
```
## 🚀 Tecnologías Usadas

### Backend
- ⚙️ Python 3.11+
- ⚡ FastAPI
- 🧪 Pydantic
- 🐘 PostgreSQL
- 🐳 Docker + Docker Compose

### Frontend
- ⚛️ React + Vite + 
- 🔄 Redux
- 🎨 Tailwind CSS
- 📦 Axios (para consumo de APIs)

#### Levantar la app

sudo docker-compose up --build

#### Corroborar que los servicios esten activos

sudo docker-compose ps

#### Acceder a Swagger por microservicio

http://localhost:800[x]/docs