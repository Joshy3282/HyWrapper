package com.joshy.hywrapper.data.skyblock

import kotlinx.serialization.Serializable

@Serializable
enum class SkillType(val cleanName: String) {
    FARMING("Farming"),
    MINING("Mining"),
    COMBAT("Combat"),
    FORAGING("Foraging"),
    FISHING("Fishing"),
    ENCHANTING("Enchanting"),
    ALCHEMY("Alchemy"),
    CARPENTRY("Carpentry"),
    RUNECRAFTING("Runecrafting"),
    SOCIAL("Social"),
    TAMING("Taming"),
    HUNTING("Hunting"),
}
