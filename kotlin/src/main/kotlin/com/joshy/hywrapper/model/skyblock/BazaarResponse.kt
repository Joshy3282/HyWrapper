package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.data.skyblock.BazaarItem
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class BazaarResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val lastUpdated: Long? = null,
    val products: Map<String, Product>? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null

    fun getProduct(item: BazaarItem): Product? {
        return products?.get(item.id)
    }
}

@Serializable
data class Product(
    @SerialName("product_id")
    val productId: String? = null,
    @SerialName("sell_summary")
    val sellSummary: List<Summary>? = null,
    @SerialName("buy_summary")
    val buySummary: List<Summary>? = null,
    @SerialName("quick_status")
    val quickStatus: QuickStatus? = null,
)

@Serializable
data class Summary(
    val amount: Int? = null,
    val pricePerUnit: Double? = null,
    val orders: Int? = null,
)

@Serializable
data class QuickStatus(
    val productId: String? = null,
    val sellPrice: Double? = null,
    val sellVolume: Long? = null,
    val sellMovingWeek: Long? = null,
    val sellOrder: Int? = null,
    val buyPrice: Double? = null,
    val buyVolume: Long? = null,
    val buyMovingWeek: Long? = null,
    val buyOrders: Int? = null,
)
