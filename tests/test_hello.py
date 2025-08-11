import pytest
from httpx import AsyncClient
from main import app_main
from fastapi_cache import FastAPICache


@pytest.fixture(autouse=True)
def set_env(monkeypatch):
    monkeypatch.setenv(
        "APP_CONFIG__DB__URL", "postgresql+asyncpg://user:password@localhost/db"
    )
    monkeypatch.setenv(
        "APP_CONFIG__ACCESS_TOKEN__RESET_PASSWORD_TOKEN_SECRET", "secret1"
    )
    monkeypatch.setenv("APP_CONFIG__ACCESS_TOKEN__VERIFICATION_TOKEN_SECRET", "secret2")


@pytest.mark.asyncio
async def test_get_hello():
    async with AsyncClient(app=app_main, base_url="http://test") as client:
        response = await client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World"}
