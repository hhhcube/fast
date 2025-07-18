# FASTAPI/Tiangolo Codex ready starter.

# FastAPI Codex Template

This is a production-ready FastAPI application template designed for use with OpenAI Codex in Code Mode. It follows the Tiangolo project structure and supports scalable, modular development with CI-ready tooling.

---

## 🚀 Features

- ✅ FastAPI app factory via `create_app()`
- ✅ Modular Tiangolo-style layout
- ✅ `.env`-based config using `pydantic-settings`
- ✅ `setup.sh` for Poetry and dev tools
- ✅ Linting: `black`, `isort`, `pyright`
- ✅ Testing: `pytest`
- ✅ Codex support via `AGENTS.md` and `prompts/`
- ✅ Placeholder folders for future modules: `models`, `schemas`, `crud`, `db`

---

## 📁 Project Structure

app/
├── api/v1/ # Routers (e.g. example.py)
├── core/ # Settings and config
├── crud/ # Business/data logic
├── db/ # DB connection/session
├── models/ # ORM models
├── schemas/ # Pydantic schemas
├── services/ # External logic (e.g. LLMs)
├── app.py # create_app()
└── main.py # Uvicorn entrypoint

tests/
├── test_ping.py # Sample test

yaml
Copy
Edit

---

## ⚙️ Setup

```bash
poetry install
cp .env.example .env
poetry run uvicorn app.main:app --reload
🧠 Codex Integration
This repo is optimized for OpenAI Codex (Code Mode).

Task prompts live in /prompts/

Agent behavior defined in AGENTS.md

Run setup.sh to install dev tools for Codex execution

📦 Included Prompts
See prompts/init_app_codex.md for an example Codex task to scaffold a new module (model, schema, CRUD, router, tests).

🛠 Dev Scripts
bash
Copy
Edit
# Format code
black app/
isort app/

# Run tests
pytest

# Type check
pyright app/
📜 License
MIT
