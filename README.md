# 🩺 Plataforma Integral de Videoconsultas Médicas

Bienvenido a una plataforma moderna, escalable y segura para gestionar videoconsultas médicas en tiempo real. Este proyecto usa una arquitectura de API REST en Python (Django REST), frontend en React con Vite y despliegue mediante Docker Compose.

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
- ⚡ Django REST
- 🧪 Pydantic
- 🐘 PostgreSQL
- 🐳 Docker + Docker Compose

### Frontend
- ⚛️ React + Vite + 
- 🔄 Redux
- 🎨 Tailwind CSS
- 📦 Axios (para consumo de APIs)

#### Levantar la app

##### Desde el directorio raíz de tu proyecto
docker-compose up --build

##### Ejecutar en segundo plano
docker-compose up -d

##### Ver logs específicos
docker-compose logs -f backend
docker-compose logs -f frontend

##### Ejecutar comandos Django
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py createsuperuser

##### Parar todo
docker-compose down

##### Parar y eliminar volúmenes (cuidado: elimina datos)
docker-compose down -v