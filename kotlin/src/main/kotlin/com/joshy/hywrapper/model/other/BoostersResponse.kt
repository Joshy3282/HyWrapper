package com.joshy.hywrapper.model.other

import com.joshy.hywrapper.data.GameType
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class BoostersResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val boosters: List<Booster>? = null,
    val boosterState: BoosterState? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class Booster(
    @SerialName("_id")
    val id: String? = null,
    val purchaserUuid: String? = null,
    val amount: Double? = null,
    val originalLength: Int? = null,
    val length: Int? = null,
    val gameType: GameType? = null,
    val dateActivated: Long? = null,
    val stacked: List<String>? = null,
)

@Serializable
data class BoosterState(
    val decrementing: Boolean? = null,
)
