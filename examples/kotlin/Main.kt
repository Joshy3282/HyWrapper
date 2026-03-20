package com.joshy.hywrapper.example

import com.joshy.hywrapper.HypixelClient
import kotlinx.coroutines.runBlocking

fun main() = runBlocking {
    val apiKey = System.getenv("HYPIXEL_API_KEY") ?: "YOUR_API_KEY"
    val client = HypixelClient(apiKey)

    try {
        val playerResponse = client.getPlayer("f7c77398-6623-4a31-8c7a-bc0c56b9d28e")
        val player = playerResponse.player

        if (player != null) {
            println("Player Name: ${player.displayname}")
            println("Network Level: ${player.networkExp}")
            println("Karma: ${player.karma}")
        } else {
            println("Player not found.")
        }

        val bazaar = client.getBazaar()
        val productCount = bazaar.products?.size ?: 0
        println("Total Bazaar Products: $productCount")

        bazaar.products?.keys?.take(5)?.forEach { productId ->
            val product = bazaar.products?.get(productId)
            println("- $productId: Buy Price ${product?.quickStatus?.buyPrice}")
        }

    } catch (e: Exception) {
        System.err.println("Error: ${e.message}")
    }
}
