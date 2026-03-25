hywrapper-ts / [Exports](modules.md)

# HyWrapper - Hypixel API Wrapper

An asynchronous and multi-platform Hypixel API wrapper for Python, Kotlin, and Java.

## Installation

### Python
```
pip install hywrapper
```

## Usage

### Kotlin
```kotlin
// Initialize the client
val client = HypixelClient(apiKey = "your-api-key")

// Fetch a player's stats (suspend function)
val response = client.getPlayer("ac29411d0826412f98c0dd14b334c1fa")
if (response.success) {
    println("Player Found!")
}
```

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

## Examples

For more detailed examples in different languages, see the [examples/](./examples/) folder.

### Bazaar (Kotlin)
```kotlin
val bazaar = client.getBazaar()
val enchantedDiamond = bazaar.getProduct(BazaarItem.ENCHANTED_DIAMOND)
println("Sell Price: ${enchantedDiamond?.quickStatus?.sellPrice}")
```

### Guild Information (Kotlin)
```kotlin
val guild = client.getGuildByPlayer("ac29411d0826412f98c0dd14b334c1fa")
println("Guild Name: ${guild.guild?.name}")
```
