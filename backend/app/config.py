from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = getenv("SECRET_KEY")
    JWT_SECRET_KEY = getenv("JWT_SECRET_KEY")
    DB_HOST = getenv("DB_HOST")
    DB_USER = getenv("DB_USER")
    DB_PASS = getenv("DB_PASS")
    DB_NAME = getenv("DB_NAME")