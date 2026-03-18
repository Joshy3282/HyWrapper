package com.joshy.hywrapper.model.other

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class PunishmentStatsResponse(
    override val success: Boolean = false,
    override val cause: String? = null,
    @SerialName("watchdog_lastMinute")
    val watchdogLastMinute: Int = 0,
    @SerialName("staff_rollingDaily")
    val staffRollingDaily: Int = 0,
    @SerialName("watchdog_total")
    val watchdogTotal: Int = 0,
    @SerialName("watchdog_rollingDaily")
    val watchdogRollingDaily: Int = 0,
    @SerialName("staff_total")
    val staffTotal: Int = 0,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

