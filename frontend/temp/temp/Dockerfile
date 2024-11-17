# Usa una imagen base de Node.js 18
FROM node:18

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia solo package.json y package-lock.json para instalar dependencias
COPY package*.json ./

# Instala Angular CLI y las dependencias del proyecto
RUN npm install -g @angular/cli chokidar-cli && npm install

# Desactiva el análisis de Angular de forma global
RUN ng config -g cli.analytics false

# Copia el resto de los archivos del proyecto
COPY . .

# Expone el puerto que Angular usa por defecto (puerto 4200)
EXPOSE 4200

# Comando para iniciar la aplicación Angular
CMD ["ng", "serve", "--host", "0.0.0.0"]
