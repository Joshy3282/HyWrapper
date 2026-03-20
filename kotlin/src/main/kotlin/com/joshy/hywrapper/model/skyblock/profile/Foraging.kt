package com.joshy.hywrapper.model.skyblock.profile

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
data class Foraging(
    val starlyn: Starlyn? = null,
    @SerialName("fish_family")
    val fishFamily: List<String> = emptyList(), // TODO enum
    val hina: Hina? = null,
    @SerialName("tree_gifts")
    val treeGifts: TreeGifts? = null,
    val songs: Songs? = null,
)

@Serializable
data class Starlyn(
    @SerialName("personal_bests")
    val personalBests: Map<String, Int> = emptyMap(), // TODO enum
)

@Serializable
data class Hina(
    val tasks: HinaTasks? = null,
)

@Serializable
data class HinaTasks(
    @SerialName("completed_tasks")
    val completedTasks: List<String> = emptyList(), // TODO enum
    @SerialName("task_progress")
    val taskProgress: Map<String, Int> = emptyMap(), // TODO enum
    @SerialName("claimed_rewards")
    val claimedRewards: List<String> = emptyList(), // TODO enum
    @SerialName("tier_claimed")
    val tierClaimed: Int = 0,
)

@Serializable
data class TreeGifts(
    @SerialName("FIG")
    val fig: Int = 0,
    @SerialName("milestone_tier_claimed")
    val milestoneTierClaimed: Map<String, Int> = emptyMap(), // TODO enum
    @SerialName("MANGROVE")
    val mangrovei: Int = 0,
)

@Serializable
data class Songs(
    val harp: Harp? = null
)

@Serializable
data class Harp(
    @SerialName("claimed_talisman") val claimedTalisman: Boolean? = null,
    @SerialName("selected_song") val selectedSong: String? = null,
    @SerialName("selected_song_epoch") val selectedSongEpoch: Long? = null,

    // Joy to the World
    @SerialName("song_joy_world_completions") val songJoyWorldCompletions: Int? = null,
    @SerialName("song_joy_world_perfect_completions") val songJoyWorldPerfectCompletions: Int? = null,
    @SerialName("song_joy_world_best_completion") val songJoyWorldBestCompletion: Double? = null,

    // Jeopardy
    @SerialName("song_jeopardy_completions") val songJeopardyCompletions: Int? = null,
    @SerialName("song_jeopardy_perfect_completions") val songJeopardyPerfectCompletions: Int? = null,
    @SerialName("song_jeopardy_best_completion") val songJeopardyBestCompletion: Double? = null,

    // Pure Imagination
    @SerialName("song_pure_imagination_completions") val songPureImaginationCompletions: Int? = null,
    @SerialName("song_pure_imagination_perfect_completions") val songPureImaginationPerfectCompletions: Int? = null,
    @SerialName("song_pure_imagination_best_completion") val songPureImaginationBestCompletion: Double? = null,

    // Through the Campfire (Fire and Flames)
    @SerialName("song_fire_and_flames_completions") val songFireAndFlamesCompletions: Int? = null,
    @SerialName("song_fire_and_flames_perfect_completions") val songFireAndFlamesPerfectCompletions: Int? = null,
    @SerialName("song_fire_and_flames_best_completion") val songFireAndFlamesBestCompletion: Double? = null,

    // Happy Birthday
    @SerialName("song_happy_birthday_completions") val songHappyBirthdayCompletions: Int? = null,
    @SerialName("song_happy_birthday_perfect_completions") val songHappyBirthdayPerfectCompletions: Int? = null,
    @SerialName("song_happy_birthday_best_completion") val songHappyBirthdayBestCompletion: Double? = null,

    // Minuet
    @SerialName("song_minuet_completions") val songMinuetCompletions: Int? = null,
    @SerialName("song_minuet_perfect_completions") val songMinuetPerfectCompletions: Int? = null,
    @SerialName("song_minuet_best_completion") val songMinuetBestCompletion: Double? = null,

    // Amazing Grace
    @SerialName("song_amazing_grace_completions") val songAmazingGraceCompletions: Int? = null,
    @SerialName("song_amazing_grace_perfect_completions") val songAmazingGracePerfectCompletions: Int? = null,
    @SerialName("song_amazing_grace_best_completion") val songAmazingGraceBestCompletion: Double? = null,

    // Greensleeves
    @SerialName("song_greensleeves_completions") val songGreensleevesCompletions: Int? = null,
    @SerialName("song_greensleeves_perfect_completions") val songGreensleevesPerfectCompletions: Int? = null,
    @SerialName("song_greensleeves_best_completion") val songGreensleevesBestCompletion: Double? = null,

    // La Vie en Rose
    @SerialName("song_vie_en_rose_completions") val songVieEnRoseCompletions: Int? = null,
    @SerialName("song_vie_en_rose_perfect_completions") val songVieEnRosePerfectCompletions: Int? = null,
    @SerialName("song_vie_en_rose_best_completion") val songVieEnRoseBestCompletion: Double? = null,

    // Brahms' Lullaby
    @SerialName("song_brahms_completions") val songBrahmsCompletions: Int? = null,
    @SerialName("song_brahms_perfect_completions") val songBrahmsPerfectCompletions: Int? = null,
    @SerialName("song_brahms_best_completion") val songBrahmsBestCompletion: Double? = null,

    // Frere Jacques
    @SerialName("song_frere_jacques_completions") val songFrereJacquesCompletions: Int? = null,
    @SerialName("song_frere_jacques_perfect_completions") val songFrereJacquesPerfectCompletions: Int? = null,
    @SerialName("song_frere_jacques_best_completion") val songFrereJacquesBestCompletion: Double? = null,

    // Pachelbel
    @SerialName("song_pachelbel_completions") val songPachelbelCompletions: Int? = null,
    @SerialName("song_pachelbel_perfect_completions") val songPachelbelPerfectCompletions: Int? = null,
    @SerialName("song_pachelbel_best_completion") val songPachelbelBestCompletion: Double? = null,

    // Ode to Joy
    @SerialName("song_hymn_joy_completions") val songHymnJoyCompletions: Int? = null,
    @SerialName("song_hymn_joy_perfect_completions") val songHymnJoyPerfectCompletions: Int? = null,
    @SerialName("song_hymn_joy_best_completion") val songHymnJoyBestCompletion: Double? = null
)