import logging
import sys
from typing import List, Any

import boto3
from pydantic_settings import BaseSettings
from loguru import logger
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

from app.core.logging import InterceptHandler


class Settings(BaseSettings):
    config: Config = Config(".env")
    API_PREFIX: str = "/api/v1"
    JWT_TOKEN_PREFIX: str = "Token"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    VERSION: str = "1.0.0"

    DEBUG: bool = config("DEBUG", cast=bool, default=False)
    SECRET_KEY: str = config("SECRET_KEY", cast=str)
    MAX_CONNECTIONS_COUNT: int = config("MAX_CONNECTIONS_COUNT", cast=int, default=10)
    MIN_CONNECTIONS_COUNT: int = config("MIN_CONNECTIONS_COUNT", cast=int, default=10)
    MYSQL_HOST: str = config("MYSQL_HOST", cast=str, default="127.0.0.1")
    MYSQL_PORT: int = config("MYSQL_PORT", cast=int, default=3306)
    MYSQL_USER: str = config("MYSQL_USER", cast=str, default="root")
    MYSQL_PASSWORD: str = config("MYSQL_PASSWORD", cast=str, default="1234")
    DB_NAME: str = config("DB_NAME", cast=str, default="")
    DB_URL: str = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{DB_NAME}"
    DYNAMODB_TABLE_NAME: str = config("DYNAMODB_TABLE_NAME", cast=str, default="")

    PROJECT_NAME: str = config("PROJECT_NAME", default="KHU-Market")
    ALLOWED_HOSTS: List[str] = config(
        "ALLOWED_HOSTS", cast=CommaSeparatedStrings, default=""
    )
    BUCKET_NAME: str = config("BUCKET_NAME", cast=str)
    AWS_ACCESS_KEY: str = config("AWS_ACCESS_KEY", cast=str)
    AWS_SECRET_KEY: str = config("AWS_SECRET_KEY", cast=str)
    AWS_SESSION_TOKEN: str = config("AWS_SESSION_TOKEN", cast=str)

    GOOGLE_CLIENT_ID: str = config("GOOGLE_CLIENT_ID", cast=str)
    GOOGLE_CLIENT_SECRET: str = config("GOOGLE_CLIENT_SECRET", cast=str)
    GOOGLE_CALLBACK_URL: str = config("GOOGLE_CALLBACK_URL", cast=str)


settings = Settings()

# logging configuration
settings = Settings()
LOGGING_LEVEL = logging.DEBUG if settings.DEBUG else logging.INFO
logging.basicConfig(
    handlers=[InterceptHandler(level=LOGGING_LEVEL)], level=LOGGING_LEVEL
)
logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])
