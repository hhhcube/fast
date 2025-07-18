# app/app.py

from fastapi import FastAPI
from app.api.v1 import example
from app.core.config import get_settings

def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.project_name,
        debug=settings.debug
    )

    app.include_router(example.router, prefix="/api/v1")

    @app.get("/")
    def root() -> dict[str, str]:
        return {"message": "Welcome"}

    return app
