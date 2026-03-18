package com.joshy.hywrapper.data.skyblock

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
enum class GardenResource(val cleanName: String) {
    @SerialName("WHEAT")
    WHEAT("Wheat"),

    @SerialName("CARROT_ITEM")
    CARROT("Carrot"),

    @SerialName("POTATO_ITEM")
    POTATO("Potato"),

    @SerialName("PUMPKIN")
    PUMPKIN("Pumpkin"),

    @SerialName("MELON")
    MELON("Melon"),

    @SerialName("INK_SACK:3")
    COCOA_BEANS("Cocoa Beans"),

    @SerialName("DOUBLE_PLANT")
    SUNFLOWER("Sunflower"),

    @SerialName("SUGAR_CANE")
    SUGAR_CANE("Sugar Cane"),

    @SerialName("MUSHROOM_COLLECTION")
    MUSHROOM("Mushroom"),

    @SerialName("CACTUS")
    CACTUS("Cactus"),

    @SerialName("NETHER_STALK")
    NETHER_WART("Nether Wart"),

    @SerialName("MOONFLOWER")
    MOONFLOWER("Moonflower"),

    @SerialName("WILD_ROSE")
    WILD_ROSE("Wild Rose")
}