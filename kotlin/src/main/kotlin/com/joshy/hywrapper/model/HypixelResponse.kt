package com.joshy.hywrapper.model

interface HypixelResponse {
    val success: Boolean?
    val cause: String?
    var rateLimit: RateLimit?
}
