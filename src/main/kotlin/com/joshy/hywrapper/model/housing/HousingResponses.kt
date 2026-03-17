package com.joshy.hywrapper.model.housing

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class HousingActiveResponse(
    override val success: Boolean = false,
    override val cause: String? = null,
    val houses: List<House> = emptyList(),
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class HousingHouseResponse(
    override val success: Boolean = false,
    override val cause: String? = null,
    val house: House? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class House(
    val uuid: String = "",
    val owner: String = "",
    val name: String = "",
    val createdAt: Long = 0L,
    val players: Int = 0,
    val cookies: Cookies? = null,
)

@Serializable
data class Cookies(
    val current: Int = 0,
)
