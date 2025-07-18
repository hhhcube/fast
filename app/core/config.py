# app/core/config.py

from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    project_name: str = "FastAPI Codex Template"
    debug: bool = True

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()
