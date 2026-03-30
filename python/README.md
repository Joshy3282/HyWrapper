# HyWrapper - Python Hypixel API Wrapper

An asynchronous Python wrapper for the Hypixel API.

## Installation

```bash
pip install hywrapper
```

## Usage

```python
import asyncio
from hywrapper import HypixelClient

async def main():
    client = HypixelClient(api_key="your-api-key")
    response = await client.get_player("ac29411d0826412f98c0dd14b334c1fa")
    if response.success:
        print(f"Player Found: {response.player.displayname}")

if __name__ == "__main__":
    asyncio.run(main())
```

## Features

- Fully asynchronous using `httpx`
- Type hints and validation using `pydantic`
- Supports all major Hypixel API endpoints
