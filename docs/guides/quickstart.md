# Quick Start Guide

Welcome to HyWrapper! This guide will help you get started with the library in your preferred language.

## 1. Get an API Key

First, obtain an API key from [Hypixel's Developer Portal](https://developer.hypixel.net/).

## 2. Python Quick Start

### Installation
```bash
pip install hywrapper
```

### Basic Usage
```python
import asyncio
from hywrapper import HypixelClient

async def main():
    client = HypixelClient(api_key="your-api-key")
    response = await client.get_player("ac29411d-0826-412f-98c0-dd14b334c1fa")
    
    if response.success:
        print(f"Found player: {response.player.displayname}")

asyncio.run(main())
```

## 3. Kotlin Quick Start

### Dependency (Gradle)
```kotlin
implementation("com.joshy:hywrapper:0.1.2")
```

### Basic Usage
```kotlin
import com.joshy.hywrapper.HypixelClient
import kotlinx.coroutines.runBlocking

fun main() = runBlocking {
    val client = HypixelClient(apiKey = "your-api-key")
    val response = client.getPlayer("ac29411d-0826-412f-98c0-dd14b334c1fa")
    
    if (response.success) {
        println("Found player: ${response.player?.displayname}")
    }
}
```
