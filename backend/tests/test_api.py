import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_health_check(client: AsyncClient):
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

@pytest.mark.asyncio
async def test_get_auction_formats_unauthorized(client: AsyncClient):
    # Should fail without JWT
    response = await client.get("/api/v1/auction-formats/")
    assert response.status_code == 403
