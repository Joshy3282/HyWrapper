package com.joshy.hywrapper.data.skyblock

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
enum class EssenceType(val cleanName: String) {
    @SerialName("CRIMSON")
    CRIMSON("Crimson"),

    @SerialName("DIAMOND")
    DIAMOND("Diamond"),

    @SerialName("DRAGON")
    DRAGON("Dragon"),

    @SerialName("FOREST")
    FOREST("Forest"),

    @SerialName("GOLD")
    GOLD("Gold"),

    @SerialName("ICE")
    ICE("Ice"),

    @SerialName("SPIDER")
    SPIDER("Spider"),

    @SerialName("UNDEAD")
    UNDEAD("Undead"),

    @SerialName("WITHER")
    WITHER("Wither"),
}
