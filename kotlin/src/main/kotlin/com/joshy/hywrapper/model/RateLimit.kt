package com.joshy.hywrapper.model

import kotlinx.serialization.Serializable
import okhttp3.Headers

@Serializable
data class RateLimit(
    val limit: Int,
    val remaining: Int,
    val reset: Int,
)

fun parseRateLimit(headers: Headers): RateLimit? {
    val limit = headers["RateLimit-Limit"]?.toIntOrNull() ?: return null
    val remaining = headers["RateLimit-Remaining"]?.toIntOrNull() ?: return null
    val reset = headers["RateLimit-Reset"]?.toIntOrNull() ?: return null
    return RateLimit(limit, remaining, reset)
}
