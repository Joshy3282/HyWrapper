package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class NewsResponse(
    override val success: Boolean = false,
    override val cause: String? = null,
    val items: List<NewsItem> = emptyList(),
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class NewsItem(
    val title: String = "",
    val text: String = "",
    val link: String = "",
    val item: NewsMaterial? = null,
)

@Serializable
data class NewsMaterial(
    val material: String = "",
)
