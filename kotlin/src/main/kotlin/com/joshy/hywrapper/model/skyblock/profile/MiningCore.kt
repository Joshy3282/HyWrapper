package com.joshy.hywrapper.model.skyblock.profile

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonElement

@Serializable
data class MiningCore(
    @SerialName("received_free_tier")
    val receivedFreeTier: Boolean? = null,
    val tokens: Int? = null,
    @SerialName("powder_mithril")
    val powderMithril: Long? = null,
    @SerialName("powder_mithril_total")
    val powderMithrilTotal: Long? = null,
    @SerialName("powder_spent_mithril")
    val powderSpentMithril: Long? = null,
    @SerialName("retroactive_tier2_token")
    val retroactiveTier2Token: Boolean? = null,
    @SerialName("daily_ores_mined_day")
    val dailyOresMinedDay: Int? = null,
    @SerialName("daily_ores_mined")
    val dailyOresMined: Int? = null,
    val crystals: Map<String, Crystal>? = null,
    @SerialName("greater_mines_last_access")
    val greaterMinesLastAccess: Long? = null,
    val biomes: Biomes? = null,
    @SerialName("powder_gemstone")
    val powderGemstone: Long? = null,
    @SerialName("powder_gemstone_total")
    val powderGemstoneTotal: Long? = null,
    @SerialName("powder_spent_gemstone")
    val powderSpentGemstone: Long? = null,
    @SerialName("daily_ores_mined_day_gemstone")
    val dailyOresMinedDayGemstone: Int? = null,
    @SerialName("daily_ores_mined_gemstone")
    val dailyOresMinedGemstone: Int? = null,
    @SerialName("daily_ores_mined_day_mithril_ore")
    val dailyOresMinedDayMithrilOre: Int? = null,
    @SerialName("daily_ores_mined_mithril_ore")
    val dailyOresMinedMithrilOre: Int? = null,
    @SerialName("daily_ores_mined_day_glacite")
    val dailyOresMinedDayGlacite: Int? = null,
    @SerialName("daily_ores_mined_glacite")
    val dailyOresMinedGlacite: Int? = null,
    @SerialName("powder_glacite")
    val powderGlacite: Long? = null,
    @SerialName("powder_glacite_total")
    val powderGlaciteTotal: Long? = null,
    @SerialName("powder_spent_glacite")
    val powderSpentGlacite: Long? = null,
    @SerialName("current_daily_effect")
    val currentDailyEffect: String? = null, // TODO enum
    @SerialName("current_daily_effect_last_changed")
    val currentDailyEffectLastChanged: Int? = null,

    )

@Serializable
data class Crystal(
    val state: String? = null,
    @SerialName("total_placed")
    val totalPlaced: Int? = null,
    @SerialName("total_found")
    val totalFound: Int? = null,
)

@Serializable
data class Biomes(
    val precursor: Precursor? = null,
    val dwarven: Map<String, JsonElement>? = null,
    val goblin: Goblin? = null,
    val jungle: Jungle? = null,
)

@Serializable
data class Precursor(
    @SerialName("claiming_with_precursor_apparatus")
    val claimingWithPrecursorApparatus: Boolean? = null,
    @SerialName("talked_to_professor")
    val talkedToProfessor: Boolean? = null,
)

@Serializable
data class Goblin(
    @SerialName("king_quest_active")
    val kingQuestActive: Boolean? = null,
    @SerialName("king_quests_completed")
    val kingQuestsCompleted: Int? = null
)

@Serializable
data class Jungle(
    @SerialName("jungle_temple_open")
    val jungleTempleOpen: Boolean? = null,
    @SerialName("jungle_temple_chest_uses")
    val jungleTempleChestUses: Int? = null
)