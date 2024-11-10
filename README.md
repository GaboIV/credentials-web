> **Note:** This README is in Spanish. For the English version of the documentation, visit: [English Version](README_EN.md)

# Credenciales Web

Este proyecto es una aplicación web de credenciales que permite almacenar y copiar credenciales de acceso de forma segura para distintas páginas, sin necesidad de tenerlas visibles. La aplicación está protegida para que solo el administrador pueda acceder. El proyecto utiliza Python (Flask) para el backend, Angular para el frontend y MySQL como base de datos, todos desplegados con Docker.

## Tecnologías

- **Backend**: Flask (Python)
- **Frontend**: Angular
- **Base de Datos**: MySQL
- **Contenerización**: Docker y Docker Compose

## Requisitos

- **Docker** y **Docker Compose** instalados en tu máquina.
- **Python** (si deseas ejecutar el backend sin Docker).
- **Node.js** y **Angular CLI** (si deseas ejecutar el frontend sin Docker).

## Configuración del Proyecto

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu-usuario/credenciales-app.git
   cd credenciales-app
   ```

2. Crea un archivo `.env` en la raíz del proyecto con las siguientes variables de entorno:

   ```dotenv
   # Claves de seguridad
   SECRET_KEY=h8fP3wLgG7tX9kVz0uWs5cJqB2mNvQd6
   JWT_SECRET_KEY=A8fP9vQc7KlG6tUe4X1yZs5B3jNrM0oWbL7hRg9HxWqYm2PtDfV

   # Configuración de la base de datos MySQL
   DB_HOST=db
   DB_USER=tu_usuario_db
   DB_PASS=tu_password_db
   DB_NAME=credenciales_db
   DB_ROOT_PASSWORD=tu_root_password
   ```

3. **Configura la Base de Datos**: En la carpeta `db`, hay un archivo `init.sql` que crea la base de datos y las tablas necesarias para la aplicación.

## Estructura del Proyecto

```plaintext
credenciales-app/
├── backend/               # Backend con Flask
│   ├── app/               # Lógica de la aplicación Flask
│   ├── Dockerfile         # Dockerfile para construir el contenedor del backend
│   └── requirements.txt   # Dependencias de Python
├── frontend/              # Frontend con Angular
│   ├── Dockerfile         # Dockerfile para construir el contenedor del frontend
├── db/                    # Inicialización de la base de datos
│   └── init.sql           # Script para crear la base de datos y tablas
├── docker-compose.yml     # Configuración para levantar la aplicación con Docker Compose
└── .env                   # Variables de entorno del proyecto
```

## Ejecución del Proyecto con Docker

Para construir y levantar la aplicación completa (backend, frontend y base de datos), ejecuta:

```bash
docker-compose up --build
```

Esto ejecutará los siguientes servicios:

- **Backend**: Disponible en [http://localhost:5000](http://localhost:5000)
- **Frontend**: Disponible en [http://localhost:4200](http://localhost:4200)
- **Base de Datos (MySQL)**: Corriendo en el puerto 3306, accesible solo dentro de los contenedores

### Servicios

- **Backend (Flask)**: Contiene la API que autentica al usuario y proporciona las credenciales almacenadas. Requiere un token JWT para todas las rutas protegidas.
- **Frontend (Angular)**: Interfaz que permite al usuario autenticarse y visualizar las credenciales protegidas.
- **Base de Datos (MySQL)**: Almacena las credenciales y la información de usuario de manera segura.

## Uso

1. Accede a [http://localhost:4200](http://localhost:4200) para ver la interfaz de usuario.
2. Inicia sesión con tus credenciales de administrador.
3. Una vez autenticado, podrás ver la lista de credenciales y copiar los datos en el portapapeles sin mostrar la contraseña en pantalla.

## Desarrollo y Pruebas

Para desarrollo, puedes levantar cada servicio individualmente:

### Backend (Flask)

1. Instala las dependencias:

   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. Ejecuta el servidor de Flask:

   ```bash
   flask run
   ```

### Frontend (Angular)

1. Instala las dependencias:

   ```bash
   cd frontend
   npm install
   ```

2. Ejecuta la aplicación de Angular:

   ```bash
   ng serve
   ```

### Base de Datos (MySQL)

Para iniciar solo la base de datos:

```bash
docker-compose up db
```

## Variables de Entorno

Las variables de entorno principales para este proyecto se encuentran en el archivo `.env` y son las siguientes:

- `SECRET_KEY`: Clave para la seguridad de la aplicación Flask.
- `JWT_SECRET_KEY`: Clave para firmar los tokens JWT.
- `DB_HOST`, `DB_USER`, `DB_PASS`, `DB_NAME`: Configuración de la conexión a MySQL.

## Seguridad

1. **JWT (JSON Web Tokens)**: La aplicación usa JWT para autenticar y autorizar al usuario. Asegúrate de cambiar `JWT_SECRET_KEY` a un valor seguro y único para cada despliegue.
2. **Credenciales encriptadas**: Las contraseñas de acceso almacenadas en la base de datos deben encriptarse antes de guardarse para una mayor seguridad.

## Despliegue

Para desplegar en producción, asegúrate de:

- Configurar correctamente las variables de entorno en el archivo `.env`.
- Usar una base de datos segura y protegida en producción.
- Configurar correctamente los puertos en el archivo `docker-compose.yml` o en el entorno de despliegue.

## Contribución

Si deseas contribuir, por favor abre un **issue** o envía un **pull request** en GitHub.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
