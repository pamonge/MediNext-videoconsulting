# Imagen base con Node.js
FROM node:20-alpine

# Crear directorio de trabajo
WORKDIR /app

# Copiar package.json y package-lock.json
COPY package*.json ./

# Instalar dependencias
RUN npm install

# Copiar el resto de la app
COPY . .

# Exponer el puerto que usa Vite por defecto
EXPOSE 3000

# Comando para iniciar la app en modo desarrollo
CMD ["npm", "run", "dev", "--", "--host"]