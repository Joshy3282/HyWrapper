package com.joshy.hywrapper.data.skyblock

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
enum class GardenUpgrade(val cleanName: String) {
    @SerialName("GROWTH_SPEED")
    GROWTH_SPEED("Crop Growth Speed"),
    @SerialName("YIELD")
    CROP_UPGRADE("Crop Upgrade"),
    @SerialName("PLOT_LIMIT")
    PLOT_LIMIT("Plot Limit")
}