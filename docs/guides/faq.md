# Frequently Asked Questions

## What is HyWrapper?

HyWrapper is a multi-platform wrapper for the Hypixel API. It aims to provide consistent models and methods across Python, Kotlin, and Java.

## Does it support the full Hypixel API?

Yes, it supports player data, guild data, SkyBlock, and more! See the [Python Reference](../api/python/client.md) and [Kotlin Reference](../kotlin/index.html) for more details.

## How do I handle rate limits?

HyWrapper handles rate limits out of the box. Both the Python and Kotlin versions have built-in retry mechanisms and rate limit parsing.

### Python Example
```python
# The client automatically handles rate limits
response = await client.get_player(uuid)
print(f"Current Rate Limit: {client.rate_limit}")
```

### Kotlin Example
```kotlin
// The client automatically handles rate limits
val response = client.getPlayer(uuid)
println("Current Rate Limit: ${client.rateLimit}")
```
