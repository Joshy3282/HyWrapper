package com.joshy.hywrapper.model.playerdata

import com.joshy.hywrapper.data.GameType
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class RecentGamesResponse(
    override val success: Boolean = false,
    override val cause: String? = null,
    val uuid: String = "",
    val games: List<RecentGame> = emptyList(),
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class RecentGame(
    val date: Long = 0L,
    val gameType: String = "",
    val mode: String? = null,
    val map: String? = null,
    val ended: Long? = null,
) {
    val parsedGameType: GameType?
        get() = runCatching { GameType.valueOf(gameType) }.getOrNull()
}
