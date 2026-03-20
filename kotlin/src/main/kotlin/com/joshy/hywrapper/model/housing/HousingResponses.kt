package com.joshy.hywrapper.model.housing

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class HousingActiveResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val houses: List<House>? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class HousingHouseResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val house: House? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class House(
    val uuid: String? = null,
    val owner: String? = null,
    val name: String? = null,
    val createdAt: Long? = null,
    val players: Int? = null,
    val cookies: Cookies? = null,
)

@Serializable
data class Cookies(
    val current: Int? = null,
)

@Serializable
data class HousingHousesResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val houses: List<House>? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}
