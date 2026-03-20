package com.joshy.hywrapper.model.skyblock.profile

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

// TODO bunch of enums

@Serializable
data class Dungeons(
    @SerialName("dungeon_types")
    val dungeonType: DungeonType? = null,
    @SerialName("player_classes")
    val playerClasses: Map<String, Map<String, Double>> = emptyMap(),
    @SerialName("dungeon_journal")
    val dungeonJournal: DungeonJournal? = null,
    @SerialName("dungeons_blah_blah")
    val dungeonsBlahBlah: List<String> = emptyList(), // TODO enum
    @SerialName("selected_dungeon_class")
    val selectedDungeonClass: String = "",
    @SerialName("daily_runs")
    val dailyRuns: DailyRuns? = null,
    // TODO treasures
    @SerialName("dungeon_hub_race_settings")
    val dungeonHubRaceSettings: DungeonHubRaceSettings? = null,
    @SerialName("last_dungeon_run")
    val lastDungeonRun: String = "",
    val secrets: Int = 0,
)

@Serializable
data class DungeonType(
    val catacombs: Catacombs? = null,
    @SerialName("master_catacombs")
    val masterCatacombs: MasterCatacombs? = null
)

@Serializable
data class Catacombs(
    @SerialName("times_played")
    val timesPlayed: Map<String, Int> = emptyMap(),
    val experience: Double = 0.0,
    @SerialName("tier_completions")
    val tierCompletions: Map<String, Int> = emptyMap(),
    @SerialName("fastest_time")
    val fastestTime: Map<String, Int> = emptyMap(),
    @SerialName("best_runs")
    val bestRuns: Map<String, BestRun> = emptyMap(),
    @SerialName("best_score")
    val bestScore: Map<String, Int> = emptyMap(),
    @SerialName("mobs_killed")
    val mobsKilled: Map<String, Int> = emptyMap(),
    @SerialName("most_mobs_killed")
    val mostMobsKilled: Map<String, Int> = emptyMap(),
    @SerialName("most_damage_tank")
    val mostDamageTank: Map<String, Double> = emptyMap(),
    @SerialName("most_healing")
    val mostHealing: Map<String, Double> = emptyMap(),
    @SerialName("watcher_kills")
    val watcherKills: Map<String, Int> = emptyMap(),
    @SerialName("highest_tier_completed")
    val highestTierCompleted: Int = 0,
    @SerialName("fastest_time_s")
    val fastestTimeS: Map<String, Double> = emptyMap(),
    @SerialName("fastest_time_s_plus")
    val fastestTimeSPlus: Map<String, Double> = emptyMap(),
    @SerialName("most_damage_berserk")
    val mostDamageBerserk: Map<String, Double> = emptyMap(),
    @SerialName("most_damage_healer")
    val mostDamageHealer: Map<String, Double> = emptyMap(),
    @SerialName("most_damage_mage")
    val mostDamageMage: Map<String, Double> = emptyMap(),
    @SerialName("milestone_completions")
    val milestoneCompletions: Map<String, Double> = emptyMap(),
    @SerialName("most_damage_archer")
    val mostDamageArcher: Map<String, Double> = emptyMap(),
)

@Serializable
data class MasterCatacombs(
    @SerialName("times_played")
    val timesPlayed: Map<String, Int> = emptyMap(),
    @SerialName("tier_completions")
    val tierCompletions: Map<String, Int> = emptyMap(),
    @SerialName("fastest_time")
    val fastestTime: Map<String, Int> = emptyMap(),
    @SerialName("best_runs")
    val bestRuns: Map<String, BestRun> = emptyMap(),
    @SerialName("best_score")
    val bestScore: Map<String, Int> = emptyMap(),
    @SerialName("mobs_killed")
    val mobsKilled: Map<String, Int> = emptyMap(),
    @SerialName("most_mobs_killed")
    val mostMobsKilled: Map<String, Int> = emptyMap(),
    @SerialName("most_damage_tank")
    val mostDamageTank: Map<String, Double> = emptyMap(),
    @SerialName("most_healing")
    val mostHealing: Map<String, Double> = emptyMap(),
    @SerialName("watcher_kills")
    val watcherKills: Map<String, Int> = emptyMap(),
    @SerialName("highest_tier_completed")
    val highestTierCompleted: Int = 0,
    @SerialName("fastest_time_s")
    val fastestTimeS: Map<String, Double> = emptyMap(),
    @SerialName("fastest_time_s_plus")
    val fastestTimeSPlus: Map<String, Double> = emptyMap(),
    @SerialName("most_damage_berserk")
    val mostDamageBerserk: Map<String, Double> = emptyMap(),
    @SerialName("most_damage_healer")
    val mostDamageHealer: Map<String, Double> = emptyMap(),
    @SerialName("most_damage_mage")
    val mostDamageMage: Map<String, Double> = emptyMap(),
    @SerialName("milestone_completions")
    val milestoneCompletions: Map<String, Double> = emptyMap(),
    @SerialName("most_damage_archer")
    val mostDamageArcher: Map<String, Double> = emptyMap(),
)

@Serializable
data class BestRun(
    val timestamp: Long = 0L,
    @SerialName("score_exploration")
    val scoreExploration: Int = 1,
    @SerialName("score_speed")
    val scoreSpeed: Int = 1,
    @SerialName("score_skill")
    val scoreSkill: Int = 1,
    @SerialName("score_bonus")
    val scoreBonus: Int = 1,
    @SerialName("dungeon_class")
    val dungeonClass: String = "",
    val teammates: List<String> = emptyList(),
    @SerialName("elapsed_time")
    val elapsedTime: Long = 0L,
    @SerialName("damage_dealt")
    val damageDealt: Double = 0.0,
    val deaths: Int = 1,
    @SerialName("mobs_killed")
    val mobsKilled: Int = 0,
    @SerialName("secrets_found")
    val secretsFound: Int = 0,
    @SerialName("damage_mitigated")
    val damageMitigated: Double = 0.0,
    @SerialName("ally_healing")
    val allyHealing: Double = 0.0
)

@Serializable
data class DungeonJournal(
    @SerialName("unlocked_journals")
    val unlockedJournals: List<String> = emptyList(), // TODO enum
)

@Serializable
data class DailyRuns(
    @SerialName("current_day_stamp")
    val currentDayStamp: Int = 0,
    @SerialName("completed_runs_count")
    val completedRunsCount: Int = 0,
)

@Serializable
data class DungeonHubRaceSettings(
    @SerialName("selected_race")
    val selectedRace: String = "",
    @SerialName("selected_setting")
    val selectedSetting: String = "",
    val runback: Boolean? = null,
)