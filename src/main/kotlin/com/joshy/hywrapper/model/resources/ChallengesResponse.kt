package com.joshy.hywrapper.model.resources

import com.joshy.hywrapper.data.GameType
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class ChallengesResponse(
    override val success: Boolean = false,
    override val cause: String? = null,
    val lastUpdated: Long = 0L,
    val challenges: Map<String, List<Challenge>> = emptyMap(),
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null

    fun getChallengesFor(game: GameType): List<Challenge> {
        return challenges[game.name.lowercase()]
            ?: challenges[game.databaseName.lowercase()]
            ?: emptyList()
    }
}

@Serializable
data class Challenge(
    val id: String = "",
    val name: String = "",
    val rewards: List<Reward> = emptyList(),
)

@Serializable
data class Reward(
    val type: String = "",
    val amount: Int = 0,
)
