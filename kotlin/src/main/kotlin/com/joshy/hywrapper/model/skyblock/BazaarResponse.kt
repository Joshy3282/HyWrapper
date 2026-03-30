package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.data.skyblock.BazaarItem
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

/**
 * Information about the Bazaar
 *
 * @property success Whether the request was successful.
 * @property cause The cause of the error, if the request failed.
 * @property lastUpdated Timestamp of when the Bazaar was last updated.
 * @property products A list of [Product] in the Bazaar.
 * */
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

/**
 * Information about a bazaar product.
 *
 * @property productId The item ID of the item.
 * @property sellSummary A list of sell orders for the item.
 * @property buySummary A list of buy orders for the item.
 * @property quickStatus General information about the item.
 * */
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

/**
 * An order summary for a bazaar product
 *
 * @property amount The total amount of items being ordered.
 * @property pricePerUnit The price being paid per unit.
 * @property orders The amount of orders at this price.
 * */
@Serializable
data class Summary(
    val amount: Int? = null,
    val pricePerUnit: Double? = null,
    val orders: Int? = null,
)

/**
 * General information about an item
 *
 * @property productId The item ID of the item
 * @property sellPrice Current highest sell price
 * @property sellVolume Total amount of items in sell orders
 * @property sellMovingWeek Total items sold the past week
 * @property sellOrders Total amount of active sell orders
 * @property buyPrice Current highest buy price
 * @property buyVolume Total amount of items in buy orders
 * @property buyMovingWeek Total items bought the past week
 * @property buyOrders Total amount of active buy orders
 * */
@Serializable
data class QuickStatus(
    val productId: String? = null,
    val sellPrice: Double? = null,
    val sellVolume: Long? = null,
    val sellMovingWeek: Long? = null,
    val sellOrders: Int? = null,
    val buyPrice: Double? = null,
    val buyVolume: Long? = null,
    val buyMovingWeek: Long? = null,
    val buyOrders: Int? = null,
)
