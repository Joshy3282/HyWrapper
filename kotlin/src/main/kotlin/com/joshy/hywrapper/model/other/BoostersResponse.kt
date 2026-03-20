package com.joshy.hywrapper.model.other

import com.joshy.hywrapper.data.GameType
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class BoostersResponse(
    override val success: Boolean = false,
    override val cause: String? = null,
    val boosters: List<Booster>? = emptyList(),
    val boosterState: BoosterState? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class Booster(
    @SerialName("_id")
    val id: String = "",
    val purchaserUuid: String = "",
    val amount: Double = 0.0,
    val originalLength: Int = 0,
    val length: Int = 0,
    val gameType: GameType? = null,
    val dateActivated: Long = 0,
    val stacked: List<String>? = emptyList(),
)

@Serializable
data class BoosterState(
    val decrementing: Boolean? = null,
)
