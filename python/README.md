# hywrapper-python

An asynchronous, high-performance Python wrapper for the Hypixel API, powered by Pydantic.

## Features

- **Asynchronous**: Built on `httpx` for efficient network operations.
- **Type Safe**: Fully typed with `Pydantic v2` models synchronized from our Kotlin core.
- **Rate Limiting**: Automatic tracking and optional retries with smart waiting.
- **Developer Friendly**: Comprehensive IDE support with auto-completion for all API responses.
- **Professional Tooling**: Integrated with `Ruff` for linting/formatting and `Mypy` for strict type checking.

## Installation

```bash
pip install .
```

## Usage

```python
import asyncio
from hywrapper import HypixelClient

async def main():
    client = HypixelClient(api_key="YOUR_API_KEY")
    
    try:
        # Fully typed response
        response = await client.get_player("ac29411d0826412f98c0dd14b334c1fa")
        if response.player:
            print(f"Player: {response.player.displayname}")
            print(f"Rank: {response.player.newPackageRank}")
            
        # Access rate limit info
        if client.last_rate_limit:
            print(f"Remaining: {client.last_rate_limit.remaining}")
            
    finally:
        await client.close()

if __name__ == "__main__":
    asyncio.run(main())
```

## Development

### Setup

```bash
uv sync --extra dev
```

### Linting & Formatting

```bash
ruff check .
ruff format .
```

### Type Checking

```bash
mypy src
```

### Testing

```bash
pytest
```
