package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class ProfilesResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val profiles: List<Profile>? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}
