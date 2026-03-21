package com.joshy.hywrapper.model.housing

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

/**
 * List of all active Houses.
 *
 * @property success Whether the request was successful.
 * @property cause The cause of the error, if the request failed.
 * @property houses A list of [House].
 */
@Serializable
data class HousingActiveResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val houses: List<House>? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

/**
 * Information about a House.
 *
 * @property success Whether the request was successful.
 * @property cause The cause of the error, if the request failed.
 * @property house The [House] details.
 */
@Serializable
data class HousingHouseResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val house: House? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

/**
 * House information
 *
 * @property uuid The UUID of the house.
 * @property owner The UUID of the player who owns the house.
 * @property name The display name of the house.
 * @property createdAt The timestamp when the house was created.
 * @property players The current number of players in the house.
 * @property cookies The [Cookies] statistics for the house.
 */
@Serializable
data class House(
    val uuid: String? = null,
    val owner: String? = null,
    val name: String? = null,
    val createdAt: Long? = null,
    val players: Int? = null,
    val cookies: Cookies? = null,
)

/**
 * Cookie information.
 *
 * @property current The current number of cookies the house has received.
 */
@Serializable
data class Cookies(
    val current: Int? = null,
)

/**
 * List of a player's houses.
 *
 * @property success Whether the request was successful.
 * @property cause The cause of the error, if the request failed.
 * @property houses A list of [House] belonging to the player.
 */
@Serializable
data class HousingHousesResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val houses: List<House>? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}
