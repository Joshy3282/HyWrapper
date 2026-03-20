package com.joshy.hywrapper.model.playerdata

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class OnlineResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val uuid: String? = null,
    val session: Session? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class Session(
    val online: Boolean? = null,
)
