package com.joshy.hywrapper.model.other

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class PunishmentStatsResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    @SerialName("watchdog_lastMinute")
    val watchdogLastMinute: Int? = null,
    @SerialName("staff_rollingDaily")
    val staffRollingDaily: Int? = null,
    @SerialName("watchdog_total")
    val watchdogTotal: Int? = null,
    @SerialName("watchdog_rollingDaily")
    val watchdogRollingDaily: Int? = null,
    @SerialName("staff_total")
    val staffTotal: Int? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}
