package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.data.skyblock.MuseumItem
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class MuseumResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val members: Map<String, Member>? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class Member(
    val value: Long? = null,
    val appraisal: Boolean? = null,
    val items: Map<MuseumItem, MuseumItemInfo>? = null,
    val special: List<SpecialItemInfo>? = null,
)

@Serializable
data class MuseumItemInfo(
    @SerialName("donated_time")
    val donatedTime: Long? = null,
    @SerialName("featured_slot")
    val featuredSlot: String? = null,
    val borrowing: Boolean? = null,
    val items: MuseumItem? = null,
)

@Serializable
data class SpecialItemInfo(
    @SerialName("donated_time")
    val donatedTime: Long? = null,
    val items: MuseumItem? = null,
)

@Serializable
data class MuseumItem(
    val type: Int? = null,
    val data: String? = null,
)
