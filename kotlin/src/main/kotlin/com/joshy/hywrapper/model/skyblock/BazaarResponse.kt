package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.data.skyblock.BazaarItem
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class BazaarResponse(
    override val success: Boolean = false,
    override val cause: String? = null,
    val lastUpdated: Long = 0L,
    val products: Map<String, Product> = emptyMap(),
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null

    fun getProduct(item: BazaarItem): Product? {
        return products[item.id]
    }
}

@Serializable
data class Product(
    @SerialName("product_id")
    val productId: String = "",
    @SerialName("sell_summary")
    val sellSummary: List<Summary> = emptyList(),
    @SerialName("buy_summary")
    val buySummary: List<Summary> = emptyList(),
    @SerialName("quick_status")
    val quickStatus: QuickStatus? = null,
)

@Serializable
data class Summary(
    val amount: Int = 0,
    val pricePerUnit: Double = 0.0,
    val orders: Int = 0,
)

@Serializable
data class QuickStatus(
    val productId: String = "",
    val sellPrice: Double = 0.0,
    val sellVolume: Long = 0L,
    val sellMovingWeek: Long = 0L,
    val sellOrder: Int = 0,
    val buyPrice: Double = 0.0,
    val buyVolume: Long = 0L,
    val buyMovingWeek: Long = 0L,
    val buyOrders: Int = 0,
)
