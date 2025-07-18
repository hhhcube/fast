from functools import lru_cache

from pydantic import BaseSettings, Field, SettingsConfigDict


class Settings(BaseSettings):
    project_name: str = Field("FastAPI Template", alias="PROJECT_NAME")
    debug: bool = Field(False, alias="DEBUG")

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", populate_by_name=True
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
