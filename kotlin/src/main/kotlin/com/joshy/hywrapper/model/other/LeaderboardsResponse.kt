package com.joshy.hywrapper.model.other

import com.joshy.hywrapper.data.GameType
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class LeaderboardsResponse(
    override val success: Boolean = false,
    override val cause: String? = null,
    val leaderboards: Map<String, List<Leaderboard>> = emptyMap(),
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null

    fun getLeaderboardsFor(game: GameType): List<Leaderboard> {
        return leaderboards[game.databaseName] ?: leaderboards[game.name] ?: emptyList()
    }
}

@Serializable
data class Leaderboard(
    val path: String = "",
    val prefix: String = "",
    val title: String = "",
    val location: String = "",
    val count: Int = 0,
    val leaders: List<String> = emptyList(),
)
