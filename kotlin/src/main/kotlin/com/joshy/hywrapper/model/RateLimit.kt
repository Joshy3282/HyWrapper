package com.joshy.hywrapper.model

import kotlinx.serialization.Serializable
import okhttp3.Headers

@Serializable
data class RateLimit(
    val limit: Int? = null,
    val remaining: Int? = null,
    val reset: Int? = null,
)

fun parseRateLimit(headers: Headers): RateLimit? {
    val limit = headers["RateLimit-Limit"]?.toIntOrNull() ?: return null
    val remaining = headers["RateLimit-Remaining"]?.toIntOrNull() ?: return null
    val reset = headers["RateLimit-Reset"]?.toIntOrNull() ?: return null
    return RateLimit(limit, remaining, reset)
}
