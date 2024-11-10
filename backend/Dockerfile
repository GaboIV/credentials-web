FROM python:3.9-slim

# Instalamos pkg-config, netcat-openbsd y las bibliotecas de desarrollo necesarias para MariaDB
RUN apt-get update && apt-get install -y \
    pkg-config \
    libmariadb-dev \
    build-essential \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo requirements.txt
COPY requirements.txt ./

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . ./

# Establecer el PYTHONPATH para incluir el directorio /app
ENV PYTHONPATH=/app

# Comando para ejecutar la aplicación
CMD ["python", "app/wsgi.py"]