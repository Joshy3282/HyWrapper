package com.joshy.hywrapper.model.other

import com.joshy.hywrapper.data.GameType
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class CountsResponse(
    override val success: Boolean = false,
    override val cause: String? = null,
    val games: Map<String, GameCount> = emptyMap(),
    val playerCount: Int = 0,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null

    fun getCountFor(game: GameType): GameCount? {
        return games[game.databaseName] ?: games[game.name]
    }
}

@Serializable
data class GameCount(
    val players: Int = 0,
    val modes: Map<String, Int> = emptyMap(),
)
