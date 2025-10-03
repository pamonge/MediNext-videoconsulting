# ./backend/Dockerfile
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    gdal-bin \
    libgdal-dev \
    python3-dev \
    postgresql-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el proyecto
COPY . .

# Crear script para esperar la base de datos
RUN echo '#!/bin/bash\n\
until pg_isready -h db -p 5432; do\n\
  echo "Esperando a que la base de datos esté lista..."\n\
  sleep 2\n\
done\n\
echo "Base de datos lista!"\n\
exec "$@"' > /usr/local/bin/wait_for_db.sh

RUN chmod +x /usr/local/bin/wait_for_db.sh

# Crear comando manage.py personalizado para esperar DB
RUN echo '#!/usr/bin/env python\n\
import os\n\
import sys\n\
import time\n\
import psycopg2\n\
from django.core.management import execute_from_command_line\n\
\n\
def wait_for_db():\n\
    """Esperar a que la base de datos esté disponible"""\n\
    max_retries = 30\n\
    retry_count = 0\n\
    \n\
    while retry_count < max_retries:\n\
        try:\n\
            conn = psycopg2.connect(\n\
                dbname=os.environ.get("DB_NAME", "medinext_db"),\n\
                user=os.environ.get("DB_USER", "admin"),\n\
                password=os.environ.get("DB_PASSWORD", "12345"),\n\
                host=os.environ.get("DB_HOST", "db"),\n\
                port=os.environ.get("DB_PORT", "5432")\n\
            )\n\
            conn.close()\n\
            print("✅ Base de datos conectada exitosamente!")\n\
            return True\n\
        except psycopg2.OperationalError as e:\n\
            retry_count += 1\n\
            print(f"⚠️  Intento {retry_count}/{max_retries}: Base de datos no disponible, reintentando en 2 segundos...")\n\
            time.sleep(2)\n\
    \n\
    print("❌ No se pudo conectar a la base de datos después de varios intentos")\n\
    return False\n\
\n\
if __name__ == "__main__":\n\
    if len(sys.argv) > 1 and sys.argv[1] == "wait_for_db":\n\
        if wait_for_db():\n\
            sys.exit(0)\n\
        else:\n\
            sys.exit(1)\n\
    else:\n\
        execute_from_command_line(sys.argv)' > wait_for_db.py

RUN chmod +x wait_for_db.py
RUN mv wait_for_db.py /usr/local/bin/manage.py

# Crear usuario no root para seguridad
RUN useradd -m -r django && chown -R django /app
USER django

# Exponer puerto
EXPOSE 8000

# Comando por defecto
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]