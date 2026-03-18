package com.joshy.hywrapper.data.skyblock

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
enum class StatType(val cleanName: String) {
    @SerialName("ABILITY_DAMAGE_PERCENT")
    ABILITY_DAMAGE_PERCENT("Ability Damage Percent"),

    @SerialName("ALCHEMY_WISDOM")
    ALCHEMY_WISDOM("Alchemy Wisdom"),

    @SerialName("ATTACK_SPEED")
    ATTACK_SPEED("Attack Speed"),

    @SerialName("BLOCK_FORTUNE")
    BLOCK_FORTUNE("Block Fortune"),

    @SerialName("BONUS_PEST_CHANCE")
    BONUS_PEST_CHANCE("Bonus Pest Chance"),

    @SerialName("BREAKING_POWER")
    BREAKING_POWER("Breaking Power"),

    @SerialName("CACTUS_FORTUNE")
    CACTUS_FORTUNE("Cactus Fortune"),

    @SerialName("CARROT_FORTUNE")
    CARROT_FORTUNE("Carrot Fortune"),

    @SerialName("COCOA_BEANS_FORTUNE")
    COCOA_BEANS_FORTUNE("Cocoa Beans Fortune"),

    @SerialName("COLD_RESISTANCE")
    COLD_RESISTANCE("Cold Resistance"),

    @SerialName("COMBAT_WISDOM")
    COMBAT_WISDOM("Combat Wisdom"),

    @SerialName("CRITICAL_CHANCE")
    CRITICAL_CHANCE("Critical Chance"),

    @SerialName("CRITICAL_DAMAGE")
    CRITICAL_DAMAGE("Critical Damage"),

    @SerialName("DAMAGE")
    DAMAGE("Damage"),

    @SerialName("DEFENSE")
    DEFENSE("Defense"),

    @SerialName("DOUBLE_HOOK_CHANCE")
    DOUBLE_HOOK_CHANCE("Double Hook Chance"),

    @SerialName("DWARVEN_METAL_FORTUNE")
    DWARVEN_METAL_FORTUNE("Dwarven Metal Fortune"),

    @SerialName("FARMING_FORTUNE")
    FARMING_FORTUNE("Farming Fortune"),

    @SerialName("FARMING_WISDOM")
    FARMING_WISDOM("Farming Wisdom"),

    @SerialName("FEAR")
    FEAR("Fear"),

    @SerialName("FEROCITY")
    FEROCITY("Ferocity"),

    @SerialName("FIG_FORTUNE")
    FIG_FORTUNE("Fig Fortune"),

    @SerialName("FISHING_SPEED")
    FISHING_SPEED("Fishing Speed"),

    @SerialName("FISHING_WISDOM")
    FISHING_WISDOM("Fishing Wisdom"),

    @SerialName("FORAGING_FORTUNE")
    FORAGING_FORTUNE("Foraging Fortune"),

    @SerialName("FORAGING_WISDOM")
    FORAGING_WISDOM("Foraging Wisdom"),

    @SerialName("GEMSTONE_FORTUNE")
    GEMSTONE_FORTUNE("Gemstone Fortune"),

    @SerialName("HEALTH")
    HEALTH("Health"),

    @SerialName("HEALTH_REGENERATION")
    HEALTH_REGENERATION("Health Regeneration"),

    @SerialName("HEAT_RESISTANCE")
    HEAT_RESISTANCE("Heat Resistance"),

    @SerialName("INTELLIGENCE")
    INTELLIGENCE("Intelligence"),

    @SerialName("MAGIC_FIND")
    MAGIC_FIND("Magic Find"),

    @SerialName("MANGROVE_FORTUNE")
    MANGROVE_FORTUNE("Mangrove Fortune"),

    @SerialName("MELON_FORTUNE")
    MELON_FORTUNE("Melon Fortune"),

    @SerialName("MENDING")
    MENDING("Mending"),

    @SerialName("MINING_FORTUNE")
    MINING_FORTUNE("Mining Fortune"),

    @SerialName("MINING_SPEED")
    MINING_SPEED("Mining Speed"),

    @SerialName("MUSHROOM_FORTUNE")
    MUSHROOM_FORTUNE("Mushroom Fortune"),

    @SerialName("NETHER_STALK_FORTUNE")
    NETHER_STALK_FORTUNE("Nether Stalk Fortune"),

    @SerialName("ORE_FORTUNE")
    ORE_FORTUNE("Ore Fortune"),

    @SerialName("PET_LUCK")
    PET_LUCK("Pet Luck"),

    @SerialName("POTATO_FORTUNE")
    POTATO_FORTUNE("Potato Fortune"),

    @SerialName("PRESSURE_RESISTANCE")
    PRESSURE_RESISTANCE("Pressure Resistance"),

    @SerialName("PRISTINE")
    PRISTINE("Pristine"),

    @SerialName("PULL")
    PULL("Pull"),

    @SerialName("PUMPKIN_FORTUNE")
    PUMPKIN_FORTUNE("Pumpkin Fortune"),

    @SerialName("RESPIRATION")
    RESPIRATION("Respiration"),

    @SerialName("RIFT_DAMAGE")
    RIFT_DAMAGE("Rift Damage"),

    @SerialName("RIFT_HEALTH")
    RIFT_HEALTH("Rift Health"),

    @SerialName("RIFT_INTELLIGENCE")
    RIFT_INTELLIGENCE("Rift Intelligence"),

    @SerialName("RIFT_MANA_REGEN")
    RIFT_MANA_REGEN("Rift Mana Regen"),

    @SerialName("RIFT_TIME")
    RIFT_TIME("Rift Time"),

    @SerialName("RIFT_WALK_SPEED")
    RIFT_WALK_SPEED("Rift Walk Speed"),

    @SerialName("SEA_CREATURE_CHANCE")
    SEA_CREATURE_CHANCE("Sea Creature Chance"),

    @SerialName("STRENGTH")
    STRENGTH("Strength"),

    @SerialName("SUGAR_CANE_FORTUNE")
    SUGAR_CANE_FORTUNE("Sugar Cane Fortune"),

    @SerialName("SWEEP")
    SWEEP("Sweep"),

    @SerialName("SWING_RANGE")
    SWING_RANGE("Swing Range"),

    @SerialName("TRACKING")
    TRACKING("Tracking"),

    @SerialName("TREASURE_CHANCE")
    TREASURE_CHANCE("Treasure Chance"),

    @SerialName("TROPHY_FISH_CHANCE")
    TROPHY_FISH_CHANCE("Trophy Fish Chance"),

    @SerialName("TRUE_DEFENSE")
    TRUE_DEFENSE("True Defense"),

    @SerialName("VITALITY")
    VITALITY("Vitality"),

    @SerialName("WALK_SPEED")
    WALK_SPEED("Walk Speed"),

    @SerialName("WEAPON_ABILITY_DAMAGE")
    WEAPON_ABILITY_DAMAGE("Weapon Ability Damage"),

    @SerialName("WHEAT_FORTUNE")
    WHEAT_FORTUNE("Wheat Fortune"),
}
