package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.data.skyblock.MuseumItem
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class MuseumResponse(
    override val success: Boolean = false,
    override val cause: String? = null,
    val members: Map<String, Member> = emptyMap(),
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class Member(
    val value: Long? = 0,
    val appraisal: Boolean? = null,
    val items: Map<MuseumItem, MuseumItemInfo> = emptyMap(),
    val special: List<SpecialItemInfo> = emptyList(),
)

@Serializable
data class MuseumItemInfo(
    @SerialName("donated_time")
    val donatedTime: Long? = 0,
    @SerialName("featured_slot")
    val featuredSlot: String? = null,
    val borrowing: Boolean? = null,
    val items: MuseumItem? = null,
)

@Serializable
data class SpecialItemInfo(
    @SerialName("donated_time")
    val donatedTime: Long? = 0,
    val items: MuseumItem? = null,
)

@Serializable
data class MuseumItem(
    val type: Int = 0,
    val data: String = ""
)
