from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    database_url: str  # PostgresDsn
