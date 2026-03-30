import pytest
import httpx
from hywrapper.client import HypixelClient


@pytest.mark.asyncio
async def test_custom_http_client_injection():
    custom_client = httpx.AsyncClient()
    client = HypixelClient(api_key="test", http_client=custom_client)

    assert client.internal_http_client == custom_client
    assert client._own_client is False

    await client.close()
    assert not custom_client.is_closed

    await custom_client.aclose()


@pytest.mark.asyncio
async def test_default_http_client_lifecycle():
    client = HypixelClient(api_key="test")
    internal_client = client.internal_http_client

    assert client._own_client is True

    await client.close()
    assert internal_client.is_closed


@pytest.mark.asyncio
async def test_caching_parity(httpx_mock):
    client = HypixelClient(api_key="test", default_cache_duration_minutes=5)

    httpx_mock.add_response(
        url="https://api.hypixel.net/v2/skyblock/bingo",
        status_code=200,
        json={"success": True, "name": "Bingo"},
    )

    response = await client.get_bingo()

    await client.close()
