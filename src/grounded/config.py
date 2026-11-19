from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "grounded"
    environment: str = "local"  # can be local| test | prod
    log_level: str = "INFO"
    database_url: str = "postgres+asyncpg://grounded:grounded@localhost:5432/grounded"


@lru_cache
def get_settings() -> Settings:
    return Settings()
