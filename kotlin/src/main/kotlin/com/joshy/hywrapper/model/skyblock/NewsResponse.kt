package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

/**
 * Lists all current news entires. These are viewable through Jerry on the island.
 *
 * @property success Whether the request was successful.
 * @property cause The cause of the error, if the request failed.
 * @property news The list of current news' information.
 * */
@Serializable
data class NewsResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    @SerialName("items")
    val news: List<NewsItem>? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

/**
 * Information about a news entry
 *
 * @property title Title of the entry, ususally a version.
 * @property text Description of the entry.
 * @property link The link that opens when clicked.
 * @property item The item in the menu.
 * */
@Serializable
data class NewsItem(
    val title: String? = null,
    val text: String? = null,
    val link: String? = null,
    val item: NewsMaterial? = null,
)

/**
 * Material of the item.
 *
 * @property material The material of the item.
 * */
@Serializable
data class NewsMaterial(
    val material: String? = null,
)
