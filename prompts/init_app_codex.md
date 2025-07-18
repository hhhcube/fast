## Task: Initialize New App from Base Template

Using the existing structure, create:

1. A new router in `app/api/v1/<module>.py`
2. A Pydantic schema in `app/schemas/<module>.py`
3. A model class in `app/models/<module>.py`
4. A CRUD service in `app/crud/<module>.py`
5. Add tests in `tests/test_<module>.py`

Ensure the module has:
- Async CRUD routes (GET, POST, PUT, DELETE)
- Dependency-injected DB session placeholder
- Schema validation using Pydantic
- Tests that pass with `pytest`

Update `app/app.py` to include the new router under `/api/v1/<module>`.
