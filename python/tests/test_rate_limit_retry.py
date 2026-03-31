import asyncio

import pytest

from hywrapper.client import HypixelClient, RateLimitException


@pytest.mark.asyncio
async def test_auto_retry_on_429(httpx_mock):
    client = HypixelClient(
        api_key="test-api-key",
        base_url="https://api.hypixel.net/v2",
        auto_retry=True,
        max_retries=2,
    )

    httpx_mock.add_response(
        url="https://api.hypixel.net/v2/skyblock/bingo",
        status_code=429,
        json={"success": False, "cause": "Rate limit reached"},
        headers={"RateLimit-Limit": "300", "RateLimit-Remaining": "0", "RateLimit-Reset": "1"},
    )

    httpx_mock.add_response(
        url="https://api.hypixel.net/v2/skyblock/bingo",
        status_code=200,
        json={"success": True, "name": "Bingo"},
    )

    import hywrapper.client

    original_sleep = asyncio.sleep
    hywrapper.client.asyncio.sleep = lambda x: original_sleep(0)

    try:
        response = await client.get_bingo()
        assert response.success is True
        assert response.name == "Bingo"
        assert len(httpx_mock.get_requests()) == 2
    finally:
        hywrapper.client.asyncio.sleep = original_sleep
        await client.close()


@pytest.mark.asyncio
async def test_auto_retry_with_retry_after(httpx_mock):
    client = HypixelClient(
        api_key="test-api-key",
        base_url="https://api.hypixel.net/v2",
        auto_retry=True,
        max_retries=2,
    )

    httpx_mock.add_response(
        url="https://api.hypixel.net/v2/skyblock/bingo",
        status_code=429,
        json={"success": False, "cause": "Rate limit reached"},
        headers={"Retry-After": "1"},
    )

    httpx_mock.add_response(
        url="https://api.hypixel.net/v2/skyblock/bingo",
        status_code=200,
        json={"success": True, "name": "Bingo"},
    )

    import hywrapper.client

    original_sleep = asyncio.sleep
    hywrapper.client.asyncio.sleep = lambda x: original_sleep(0)

    try:
        response = await client.get_bingo()
        assert response.success is True
        assert len(httpx_mock.get_requests()) == 2
    finally:
        hywrapper.client.asyncio.sleep = original_sleep
        await client.close()


@pytest.mark.asyncio
async def test_max_retries_exceeded(httpx_mock):
    client = HypixelClient(
        api_key="test-api-key",
        base_url="https://api.hypixel.net/v2",
        auto_retry=True,
        max_retries=1,
    )

    for _ in range(2):
        httpx_mock.add_response(
            url="https://api.hypixel.net/v2/skyblock/bingo",
            status_code=429,
            json={"success": False, "cause": "Rate limit reached"},
            headers={"RateLimit-Reset": "1"},
        )

    import hywrapper.client

    original_sleep = asyncio.sleep
    hywrapper.client.asyncio.sleep = lambda x: original_sleep(0)

    try:
        with pytest.raises(RateLimitException):
            await client.get_bingo()
        assert len(httpx_mock.get_requests()) == 2
    finally:
        hywrapper.client.asyncio.sleep = original_sleep
        await client.close()


@pytest.mark.asyncio
async def test_no_retry_when_disabled(httpx_mock):
    client = HypixelClient(
        api_key="test-api-key", base_url="https://api.hypixel.net/v2", auto_retry=False
    )

    httpx_mock.add_response(
        url="https://api.hypixel.net/v2/skyblock/bingo",
        status_code=429,
        json={"success": False, "cause": "Rate limit reached"},
    )

    try:
        with pytest.raises(RateLimitException):
            await client.get_bingo()
        assert len(httpx_mock.get_requests()) == 1
    finally:
        await client.close()
