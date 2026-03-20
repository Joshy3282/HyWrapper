package com.joshy.hywrapper.model.skyblock.profile

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
data class CrimsonIslePlayerData(
    val quests: Quests? = null,
)

@Serializable
data class Quests(
    @SerialName("quest_data")
    val questData: QuestData? = null,
    // TODO miniboss_daily
    // TODO kuudra_boss_daily
    @SerialName("quest_rewards")
    val questRewards: QuestRewards? = null,
    @SerialName("alchemist_quest")
    val alchemistQuest: AlchemistQuest? = null,
    // TODO rulenor

)

@Serializable
data class QuestData(
    @SerialName("quest_list")
    val questList: List<String> = emptyList(), // TODO enum
    val quests: List<QuestDataData> = emptyList(), // TODO no way this is right
)

@Serializable
data class QuestDataData( // TODO name..
    val status: String = "",
    val progress: Int = 0,
    @SerialName("completed_at")
    val completedAt: Long = 0L,
)

@Serializable
data class QuestRewards(
    @SerialName("WITHER_SOUL")
    val witherSoul: Int? = null,
    @SerialName("BEZOS")
    val bezos: Int? = null,
    @SerialName("FLAMING_HEART")
    val flamingHeart: Int? = null,
    @SerialName("CORRUPTED_FRAGMENT")
    val corruptedFragment: Int? = null,
    @SerialName("LUMINO_FIBER")
    val luminoFiber: Int? = null,
    @SerialName("crimson_isle_dojo_test_of_mob_kb_drating_c")
    val crimsonIsleDojoTestOfMobKbDratingC: String? = null,
    @SerialName("crimson_isle_fetch_tentacle_meat_c")
    val crimsonIsleFetchTentacleMeatC: String? = null,
    @SerialName("crimson_isle_soulfish_b")
    val crimsonIsleSoulfishB: String? = null,
    @SerialName("crimson_isle_kill_ashfang_a")
    val crimsonIsleKillAshfangA: String? = null,
    @SerialName("crimson_isle_rescue_s")
    val crimsonIsleRescueS: String? = null
)

@Serializable
data class AlchemistQuest(
    @SerialName("alchemist_quest_start")
    val alchemistQuestStart: Boolean? = null,
    @SerialName("alchemist_quest_progress")
    val alchemistQuestProgress: Int = 0,
)