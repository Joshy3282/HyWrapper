import pytest

from hywrapper.client import (
    DataNotPopulatedException,
    HypixelClient,
    HypixelException,
    InvalidApiKeyException,
    MissingFieldException,
    RateLimitException,
    ResourceNotFoundException,
)
from hywrapper.models import (
    BazaarResponse,
    BingoResponse,
    FiresalesResponse,
    PlayerResponse,
)


@pytest.fixture
async def client():
    client = HypixelClient(api_key="test-api-key", base_url="https://api.hypixel.net/v2")
    yield client
    await client.close()


@pytest.mark.asyncio
async def test_get_bingo_success(client, httpx_mock):
    json_response = {
        "success": True,
        "lastUpdated": 1618214400000,
        "id": 1,
        "name": "Bingo",
        "start": 1618214400000,
        "end": 1618214400000,
        "modifier": "Modifier",
        "goals": [],
    }
    httpx_mock.add_response(url="https://api.hypixel.net/v2/skyblock/bingo", json=json_response)

    response = await client.get_bingo()
    assert response.success is True
    assert response.name == "Bingo"
    assert response.last_updated == 1618214400000
    assert isinstance(response, BingoResponse)

    request = httpx_mock.get_request()
    assert request.headers["API-Key"] == "test-api-key"


@pytest.mark.asyncio
async def test_get_player_success(client, httpx_mock):
    uuid = "ac29411d0826412f98c0dd14b334c1fa"
    json_response = {"success": True, "player": {"displayname": "PlayerName", "uuid": uuid}}
    httpx_mock.add_response(
        url=f"https://api.hypixel.net/v2/player?uuid={uuid}", json=json_response
    )

    response = await client.get_player(uuid)
    assert response.success is True
    assert response.player.displayname == "PlayerName"
    assert isinstance(response, PlayerResponse)


@pytest.mark.asyncio
async def test_get_firesales_success(client, httpx_mock):
    json_response = {
        "success": True,
        "sales": [
            {
                "item_id": "pet_skin_black_cat",
                "start": 1618214400000,
                "end": 1618214400000,
                "amount": 1000,
                "price": 500,
            }
        ],
    }
    httpx_mock.add_response(url="https://api.hypixel.net/v2/skyblock/firesales", json=json_response)

    response = await client.get_firesales()
    assert response.success is True
    assert len(response.sales) == 1
    assert response.sales[0].item_id == "pet_skin_black_cat"
    assert isinstance(response, FiresalesResponse)


@pytest.mark.asyncio
async def test_get_bazaar_success(client, httpx_mock):
    json_response = {
        "success": True,
        "lastUpdated": 1618214400000,
        "products": {
            "INK_SACK:3": {
                "product_id": "INK_SACK:3",
                "quick_status": {
                    "productId": "INK_SACK:3",
                    "sellPrice": 1.0,
                    "buyPrice": 2.0,
                    "sellVolume": 100,
                    "buyVolume": 100,
                    "sellOrders": 10,
                    "buyOrders": 10,
                },
                "sell_summary": [],
                "buy_summary": [],
            }
        },
    }
    httpx_mock.add_response(url="https://api.hypixel.net/v2/skyblock/bazaar", json=json_response)

    response = await client.get_bazaar()
    assert response.success is True
    assert "INK_SACK:3" in response.products
    assert isinstance(response, BazaarResponse)


@pytest.mark.asyncio
async def test_api_error(client, httpx_mock):
    json_response = {"success": False, "cause": "Invalid API Key"}
    httpx_mock.add_response(url="https://api.hypixel.net/v2/skyblock/bingo", json=json_response)

    with pytest.raises(HypixelException) as excinfo:
        await client.get_bingo()
    assert "API Error: Invalid API Key" in str(excinfo.value)


@pytest.mark.asyncio
async def test_403_invalid_api_key(client, httpx_mock):
    json_response = {"success": False, "cause": "Invalid API key"}
    httpx_mock.add_response(
        url="https://api.hypixel.net/v2/skyblock/bingo", json=json_response, status_code=403
    )

    with pytest.raises(InvalidApiKeyException):
        await client.get_bingo()


@pytest.mark.asyncio
async def test_404_not_found(client, httpx_mock):
    json_response = {"success": False, "cause": "Not Found"}
    httpx_mock.add_response(
        url="https://api.hypixel.net/v2/skyblock/bingo", json=json_response, status_code=404
    )

    with pytest.raises(ResourceNotFoundException):
        await client.get_bingo()


@pytest.mark.asyncio
async def test_400_missing_field(client, httpx_mock):
    json_response = {"success": False, "cause": "Missing one or more fields"}
    httpx_mock.add_response(
        url="https://api.hypixel.net/v2/skyblock/bingo", json=json_response, status_code=400
    )

    with pytest.raises(MissingFieldException):
        await client.get_bingo()


@pytest.mark.asyncio
async def test_429_rate_limit(client, httpx_mock):
    json_response = {"success": False, "cause": "Key throttle", "global": False}
    httpx_mock.add_response(
        url="https://api.hypixel.net/v2/skyblock/bingo", json=json_response, status_code=429
    )

    with pytest.raises(RateLimitException) as excinfo:
        await client.get_bingo()
    assert excinfo.value.is_global is False


@pytest.mark.asyncio
async def test_rate_limit_parsing(client, httpx_mock):
    json_response = {"success": True, "name": "Bingo"}
    headers = {"RateLimit-Limit": "300", "RateLimit-Remaining": "299", "RateLimit-Reset": "59"}
    httpx_mock.add_response(
        url="https://api.hypixel.net/v2/skyblock/bingo", json=json_response, headers=headers
    )

    response = await client.get_bingo()
    assert response.rate_limit.limit == 300
    assert response.rate_limit.remaining == 299
    assert response.rate_limit.reset == 59
    assert client.last_rate_limit.limit == 300


@pytest.mark.asyncio
async def test_503_data_not_populated(client, httpx_mock):
    json_response = {"success": False, "cause": "Data not populated"}
    httpx_mock.add_response(
        url="https://api.hypixel.net/v2/skyblock/auctions?page=1",
        json=json_response,
        status_code=503,
    )

    with pytest.raises(DataNotPopulatedException):
        await client.get_auctions(1)
