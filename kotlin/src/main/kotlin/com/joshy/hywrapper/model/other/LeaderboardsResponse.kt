package com.joshy.hywrapper.model.other

import com.joshy.hywrapper.data.GameType
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class LeaderboardsResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val leaderboards: Map<String, List<Leaderboard>>? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null

    fun getLeaderboardsFor(game: GameType): List<Leaderboard> {
        return leaderboards?.get(game.databaseName) ?: leaderboards?.get(game.name) ?: emptyList()
    }
}

@Serializable
data class Leaderboard(
    val path: String? = null,
    val prefix: String? = null,
    val title: String? = null,
    val location: String? = null,
    val count: Int? = null,
    val leaders: List<String>? = null,
)
