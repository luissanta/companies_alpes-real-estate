import os
from dotenv import load_dotenv

load_dotenv()


class Setting:
    PROJECT_NAME: str = "Alpes Real Estate"
    PROJECT_VERSION: str = "1.0.0"
    DB_ENGINE: str = "postgresql"

    SECRET_KEY: str = os.getenv("SECRET_KEY", "secret")
    ENV: str = os.getenv("ENV", "local")

    READ_DB_USER: str = os.getenv("READ_DB_USER")
    READ_DB_PASSWORD: str = os.getenv("READ_DB_PASSWORD")
    READ_DB_HOST: str = os.getenv("READ_DB_HOST", "localhost")
    READ_DB_PORT: str = os.getenv("READ_DB_PORT", 5432)
    READ_DB_NAME: str = os.getenv("READ_DB_NAME")
    READ_DATABASE_URL = f"{DB_ENGINE}://{READ_DB_USER}:{READ_DB_PASSWORD}@{READ_DB_HOST}:" \
                        f"{READ_DB_PORT}/{READ_DB_NAME}"

    WRITE_DB_USER: str = os.getenv("WRITE_DB_USER")
    WRITE_DB_PASSWORD = os.getenv("WRITE_DB_PASSWORD")
    WRITE_DB_HOST: str = os.getenv("WRITE_DB_HOST", "localhost")
    WRITE_DB_PORT: str = os.getenv("WRITE_DB_PORT", 5432)
    WRITE_DB_NAME: str = os.getenv("WRITE_DB_NAME")
    WRITE_DATABASE_URL = f"{DB_ENGINE}://{WRITE_DB_USER}:{WRITE_DB_PASSWORD}@{WRITE_DB_HOST}:" \
                         f"{WRITE_DB_PORT}/{WRITE_DB_NAME}"


settings = Setting
