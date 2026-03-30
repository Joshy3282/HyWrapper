package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

/**
 * Information about a player's profiles
 *
 * @property success Whether the request was successful.
 * @property cause The cause of the error, if the request failed.
 * @property profiles A list of the player's profiles
 * */
@Serializable
data class ProfilesResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val profiles: List<Profile>? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}
