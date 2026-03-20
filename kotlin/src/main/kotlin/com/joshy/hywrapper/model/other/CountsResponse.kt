package com.joshy.hywrapper.model.other

import com.joshy.hywrapper.data.GameType
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class CountsResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val games: Map<String, GameCount>? = null,
    val playerCount: Int? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null

    fun getCountFor(game: GameType): GameCount? {
        return games?.get(game.databaseName) ?: games?.get(game.name)
    }
}

@Serializable
data class GameCount(
    val players: Int? = null,
    val modes: Map<String, Int>? = null,
)
