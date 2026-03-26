package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.data.skyblock.MuseumItem
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

/**
 * Information about a player's museum.
 *
 * @property success Whether the request was successful.
 * @property cause The cause of the error, if the request failed.
 * @property members Information about each members museum in a coop.
 * */
@Serializable
data class MuseumResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val members: Map<String, MuseumMember>? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

/**
 * Information about a coop member's museum.
 *
 * @property value The museums valuation when apprased.
 * @property appraisal Whether or not the museum has been appraised.
 * @property items A list of information about each donatable item.
 * @property special A list of special items donated (eg; minion skins, the fishes').
 * */
@Serializable
data class MuseumMember(
    val value: Long? = null,
    val appraisal: Boolean? = null,
    val items: Map<MuseumItem, MuseumItemInfo>? = null,
    val special: List<SpecialItemInfo>? = null,
)

/**
 * Information about a specific donatable item
 *
 * @property timeDonated The timestamp the item was donated to museum.
 * @property featuredSlot Slot id of where the item is being featured.
 * @property borrowing Whether the item is donated to museum, but not currently in museum.
 * @property itemData Item data for the donated item.
 * */
@Serializable
data class MuseumItemInfo(
    @SerialName("donated_time")
    val timeDonated: Long? = null,
    @SerialName("featured_slot")
    val featuredSlot: String? = null, // TODO enum
    val borrowing: Boolean? = null,
    @SerialName("items")
    val itemData: MuseumItemData? = null,
)

/**
 * Information about an item donated to the special category
 *
 * @property timeDonated The timestamp the item was donated to museum.
 * @property itemData Item data for the donated item.
 * */
@Serializable
data class SpecialItemInfo(
    @SerialName("donated_time")
    val timeDonated: Long? = null,
    @SerialName("items")
    val itemData: MuseumItemData? = null,
)

/**
 * Item data for a donated item.
 *
 * @property type Unknown
 * @property data gzipped nbt data.
 * */
@Serializable
data class MuseumItemData(
    val type: Int? = null, // TODO what is this
    val data: String? = null,
)
