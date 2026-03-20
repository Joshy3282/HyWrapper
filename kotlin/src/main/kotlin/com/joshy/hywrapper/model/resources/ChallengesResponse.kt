package com.joshy.hywrapper.model.resources

import com.joshy.hywrapper.data.GameType
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class ChallengesResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val lastUpdated: Long? = null,
    val challenges: Map<String, List<Challenge>>? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null

    fun getChallengesFor(game: GameType): List<Challenge>? {
        return challenges?.get(game.name.lowercase())
            ?: challenges?.get(game.databaseName.lowercase())
    }
}

@Serializable
data class Challenge(
    val id: String? = null,
    val name: String? = null,
    val rewards: List<Reward>? = null,
)

@Serializable
data class Reward(
    val type: String? = null,
    val amount: Int? = null,
)
