# HyWrapper - Hypixel API Wrapper

An asynchronous and multi-platform Hypixel API wrapper for Python, Kotlin, and Java.

## Setup

TODO

## Usage

### Python
```python
import asyncio
from hywrapper import HypixelClient

async def main():
    client = HypixelClient(api_key="your-api-key")
    response = await client.get_player("ac29411d0826412f98c0dd14b334c1fa")
    if response.success:
        print("Player Found!")

asyncio.run(main())
```