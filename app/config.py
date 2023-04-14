from decouple import config
from pydantic import BaseSettings


class Settings(BaseSettings):
    database_hostname: str = config("DATABASE_HOSTNAME")
    database_port: str = config("DATABASE_PORT")
    database_password: str = config("DATABASE_PASSWORD")
    database_name: str = config("DATABASE_NAME")
    database_username: str = config("DATABASE_USERNAME")
    secret_key: str = config("SECRET_KEY")
    algorithm: str = config("ALGORITHM")
    access_token_expire_minutes: int = config("ACCESS_TOKEN_EXPIRE_MINUTES")


settings = Settings()
