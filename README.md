
# HyWrapper - Hypixel API Wrapper

[![Python CI](https://github.com/Joshy3282/HyWrapper/actions/workflows/python-ci.yml/badge.svg)](https://github.com/Joshy3282/HyWrapper/actions/workflows/python-ci.yml)[![TypeScript CI](https://github.com/Joshy3282/HyWrapper/actions/workflows/typescript-ci.yml/badge.svg)](https://github.com/Joshy3282/HyWrapper/actions/workflows/typescript-ci.yml) [![Kotlin CI](https://github.com/Joshy3282/HyWrapper/actions/workflows/kotlin-ci.yml/badge.svg)](https://github.com/Joshy3282/HyWrapper/actions/workflows/kotlin-ci.yml) <br>
[![PyPI version](https://badge.fury.io/py/hywrapper.svg)](https://badge.fury.io/py/hywrapper) [![npm version](https://badge.fury.io/js/hywrapper-ts.svg)](https://www.npmjs.com/package/hywrapper-ts) [![JitPack](https://jitpack.io/v/Joshy3282/HyWrapper.svg)](https://jitpack.io/#Joshy3282/HyWrapper) <br>
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Discord](https://img.shields.io/discord/843473054423318568?color=7289da&label=discord)](https://discord.com/invite/serenity-843473054423318568) <br>

An asynchronous and multi-platform Hypixel API wrapper for Python, Kotlin, and Java.

## Features

- **Language Parity**: Consistent models and helper methods across Python, TypeScript, and Kotlin.
- **Asynchronous**: Fully non-blocking requests using Coroutines (Kotlin), `asyncio/httpx` (Python), and Promises (TypeScript).
- **Type Safety**: Rich, strongly-typed models with validation (Pydantic, Kotlin Serialization, TypeScript Interfaces).
- **Comprehensive Coverage**: Support for all major endpoints including SkyBlock (Bazaar, Auctions, Garden), Players, Guilds, and Resources.
- **Automatic Rate Limiting**: Built-in handling for Hypixel API rate limits to ensure reliable data fetching.

## Documentation

Full documentation is available at [https://joshy3282.github.io/HyWrapper/](https://joshy3282.github.io/HyWrapper/).

## Installation

### Python
```
pip install hywrapper
```

### Kotlin / Java
Add the JitPack repository and the dependency to your `build.gradle.kts`:
```kotlin
repositories {
    maven { url = uri("https://jitpack.io") }
}

dependencies {
    implementation("com.github.joshy3282:hywrapper:1.0.0")
}
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
