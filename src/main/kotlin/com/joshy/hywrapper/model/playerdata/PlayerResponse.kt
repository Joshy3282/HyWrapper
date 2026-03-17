package com.joshy.hywrapper.model.playerdata

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient
import kotlinx.serialization.json.JsonObject

@Serializable
data class PlayerResponse(
    override val success: Boolean = false,
    override val cause: String? = null,
    val player: JsonObject? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}
