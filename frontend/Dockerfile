# Usa una imagen base de Node.js 18
FROM node:18

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . /app

# Instala Angular CLI globalmente y las dependencias del proyecto
RUN npm install -g @angular/cli && npm install

# Expone el puerto que Angular usa por defecto (puerto 4200)
EXPOSE 4200

# Comando para iniciar la aplicación Angular
CMD ["ng", "serve", "--host", "0.0.0.0"]
