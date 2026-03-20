package com.joshy.hywrapper.model.playerdata

import com.joshy.hywrapper.data.GameType
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class RecentGamesResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val uuid: String? = null,
    val games: List<RecentGame>? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class RecentGame(
    val date: Long? = null,
    val gameType: String? = null,
    val mode: String? = null,
    val map: String? = null,
    val ended: Long? = null,
) {
    val parsedGameType: GameType?
        get() = gameType?.let { gt -> runCatching { GameType.valueOf(gt) }.getOrNull() }
}
