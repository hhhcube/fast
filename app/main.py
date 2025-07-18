from fastapi import FastAPI
from dotenv import load_dotenv

from app.core.config import get_settings
from app.api.v1 import example

load_dotenv()
settings = get_settings()

app = FastAPI(title=settings.project_name, debug=settings.debug)

app.include_router(example.router, prefix="/api/v1")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Welcome"}


