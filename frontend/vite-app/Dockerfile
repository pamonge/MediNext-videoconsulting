# Imagen base con Node.js
FROM node:20-alpine3.19

# Actualiza npm primero
RUN npm install -g npm@latest

# Crear directorio de trabajo
WORKDIR /app

# Copiar package.json y package-lock.json
COPY package*.json ./

# Instalar dependencias
RUN npm install

# Copiar el resto de la app
COPY . .

RUN npm run build 

# Exponer el puerto que usa Vite por defecto
EXPOSE 3000

# Comando para iniciar la app en modo desarrollo
CMD ["npm", "run", "dev", "--", "--host"]