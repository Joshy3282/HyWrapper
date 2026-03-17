# Hypixel Kotlin API Client

## General Usage

```kotlin
// Initialize the client
val client = HypixelClient(apiKey = "your-api-key")

// Fetch a player's stats (suspend function)
val response = client.getPlayer("ac29411d0826412f98c0dd14b334c1fa")
if (response.success) {
    println("Player Found!")
}
```

## Examples

### Bazaar
```kotlin
val bazaar = client.getBazaar()
val enchantedDiamond = bazaar.getProduct(BazaarItem.ENCHANTED_DIAMOND)
println("Sell Price: ${enchantedDiamond?.quickStatus?.sellPrice}")
```

### Firesales
```kotlin
val firesales = client.getFiresales()
firesales.sales.forEach { sale ->
    println("Item: ${sale.itemId}, Price: ${sale.price}")
}
```

### Guild Information
```kotlin
val guild = client.getGuildByPlayer("ac29411d0826412f98c0dd14b334c1fa")
println("Guild Name: ${guild.guild?.name}")
```
