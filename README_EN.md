> **Note:** Este README está en inglés. Para ver la versión en español, visite: [Versión en español](README.md)

# Credentials Web

This project is a credentials web application that allows you to store and copy access credentials securely for different pages without having them visible. The application is protected so that only the administrator can access it. The project uses Python (Flask) for the backend, Angular for the frontend, and MySQL as the database, all deployed with Docker.

## Technologies

- **Backend**: Flask (Python)
- **Frontend**: Angular
- **Database**: MySQL
- **Containerization**: Docker and Docker Compose

## Requirements

- **Docker** and **Docker Compose** installed on your machine.
- **Python** (if you wish to run the backend without Docker).
- **Node.js** and **Angular CLI** (if you wish to run the frontend without Docker).

## Project Configuration

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/credentials-app.git
   cd credentials-app
   ```

2. Create a `.env` file in the project root with the following environment variables:

   ```dotenv
   # Security keys
   SECRET_KEY=h8fP3wLgG7tX9kVz0uWs5cJqB2mNvQd6
   JWT_SECRET_KEY=A8fP9vQc7KlG6tUe4X1yZs5B3jNrM0oWbL7hRg9HxWqYm2PtDfV

   # MySQL Database Configuration
   DB_HOST=db
   DB_USER=your_db_user
   DB_PASS=your_db_password
   DB_NAME=credentials_db
   DB_ROOT_PASSWORD=your_root_password
   ```

3. **Database Setup**: In the `db` folder, there is an `init.sql` file that creates the database and necessary tables for the application.

## Project Structure

```plaintext
credentials-app/
├── backend/               # Backend with Flask
│   ├── app/               # Flask application logic
│   ├── Dockerfile         # Dockerfile to build the backend container
│   └── requirements.txt   # Python dependencies
├── frontend/              # Frontend with Angular
│   ├── Dockerfile         # Dockerfile to build the frontend container
├── db/                    # Database initialization
│   └── init.sql           # Script to create the database and tables
├── docker-compose.yml     # Docker Compose configuration for the application
└── .env                   # Project environment variables
```

## Running the Project with Docker

To build and start the full application (backend, frontend, and database), run:

```bash
docker-compose up --build
```

This will start the following services:

- **Backend**: Available at [http://localhost:5000](http://localhost:5000)
- **Frontend**: Available at [http://localhost:4200](http://localhost:4200)
- **Database (MySQL)**: Running on port 3306, accessible only within the containers

### Services

- **Backend (Flask)**: Contains the API that authenticates the user and provides the stored credentials. Requires a JWT token for all protected routes.
- **Frontend (Angular)**: Interface that allows the user to authenticate and view protected credentials.
- **Database (MySQL)**: Stores credentials and user information securely.

## Usage

1. Go to [http://localhost:4200](http://localhost:4200) to see the user interface.
2. Log in with your admin credentials.
3. Once authenticated, you can view the list of credentials and copy the data to the clipboard without showing the password on screen.

## Development and Testing

For development, you can start each service individually:

### Backend (Flask)

1. Install dependencies:

   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. Run the Flask server:

   ```bash
   flask run
   ```

### Frontend (Angular)

1. Install dependencies:

   ```bash
   cd frontend
   npm install
   ```

2. Run the Angular application:

   ```bash
   ng serve
   ```

### Database (MySQL)

To start only the database:

```bash
docker-compose up db
```

## Environment Variables

The main environment variables for this project are in the `.env` file and include:

- `SECRET_KEY`: Key for Flask application security.
- `JWT_SECRET_KEY`: Key for signing JWT tokens.
- `DB_HOST`, `DB_USER`, `DB_PASS`, `DB_NAME`: MySQL connection settings.

## Security

1. **JWT (JSON Web Tokens)**: The application uses JWT to authenticate and authorize the user. Be sure to set `JWT_SECRET_KEY` to a secure and unique value for each deployment.
2. **Encrypted Credentials**: Access passwords stored in the database should be encrypted before saving for added security.

## Deployment

For production deployment, make sure to:

- Properly set environment variables in the `.env` file.
- Use a secure and protected database in production.
- Correctly configure ports in the `docker-compose.yml` file or in the deployment environment.

## Contribution

If you want to contribute, please open an **issue** or submit a **pull request** on GitHub.

## License

This project is under the MIT License. See the `LICENSE` file for more details.
