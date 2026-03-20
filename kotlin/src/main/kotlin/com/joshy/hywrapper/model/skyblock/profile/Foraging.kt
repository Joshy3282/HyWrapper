package com.joshy.hywrapper.model.skyblock.profile

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
data class Foraging(
    val starlyn: Starlyn? = null,
    @SerialName("fish_family")
    val fishFamily: List<String>? = null, // TODO enum
    val hina: Hina? = null,
    @SerialName("tree_gifts")
    val treeGifts: TreeGifts? = null,
    val songs: Songs? = null,
)

@Serializable
data class Starlyn(
    @SerialName("personal_bests")
    val personalBests: Map<String, Int>? = null, // TODO enum
)

@Serializable
data class Hina(
    val tasks: HinaTasks? = null,
)

@Serializable
data class HinaTasks(
    @SerialName("completed_tasks")
    val completedTasks: List<String>? = null, // TODO enum
    @SerialName("task_progress")
    val taskProgress: Map<String, Int>? = null, // TODO enum
    @SerialName("claimed_rewards")
    val claimedRewards: List<String>? = null, // TODO enum
    @SerialName("tier_claimed")
    val tierClaimed: Int? = null,
)

@Serializable
data class TreeGifts(
    @SerialName("FIG")
    val fig: Int? = null,
    @SerialName("milestone_tier_claimed")
    val milestoneTierClaimed: Map<String, Int>? = null, // TODO enum
    @SerialName("MANGROVE")
    val mangrovei: Int? = null,
)

@Serializable
data class Songs(
    val harp: Harp? = null
)

@Serializable
data class Harp(
    @SerialName("claimed_talisman") val claimed_talisman: Boolean? = null,
    @SerialName("selected_song") val selected_song: String? = null,
    @SerialName("selected_song_epoch") val selected_song_epoch: Long? = null,

    // Joy to the World
    @SerialName("song_joy_world_completions") val song_joy_world_completions: Int? = null,
    @SerialName("song_joy_world_perfect_completions") val song_joy_world_perfect_completions: Int? = null,
    @SerialName("song_joy_world_best_completion") val song_joy_world_best_completion: Double? = null,

    // Jeopardy
    @SerialName("song_jeopardy_completions") val song_jeopardy_completions: Int? = null,
    @SerialName("song_jeopardy_perfect_completions") val song_jeopardy_perfect_completions: Int? = null,
    @SerialName("song_jeopardy_best_completion") val song_jeopardy_best_completion: Double? = null,

    // Pure Imagination
    @SerialName("song_pure_imagination_completions") val song_pure_imagination_completions: Int? = null,
    @SerialName("song_pure_imagination_perfect_completions") val song_pure_imagination_perfect_completions: Int? = null,
    @SerialName("song_pure_imagination_best_completion") val song_pure_imagination_best_completion: Double? = null,

    // Through the Campfire (Fire and Flames)
    @SerialName("song_fire_and_flames_completions") val song_fire_and_flames_completions: Int? = null,
    @SerialName("song_fire_and_flames_perfect_completions") val song_fire_and_flames_perfect_completions: Int? = null,
    @SerialName("song_fire_and_flames_best_completion") val song_fire_and_flames_best_completion: Double? = null,

    // Happy Birthday
    @SerialName("song_happy_birthday_completions") val song_happy_birthday_completions: Int? = null,
    @SerialName("song_happy_birthday_perfect_completions") val song_happy_birthday_perfect_completions: Int? = null,
    @SerialName("song_happy_birthday_best_completion") val song_happy_birthday_best_completion: Double? = null,

    // Minuet
    @SerialName("song_minuet_completions") val song_minuet_completions: Int? = null,
    @SerialName("song_minuet_perfect_completions") val song_minuet_perfect_completions: Int? = null,
    @SerialName("song_minuet_best_completion") val song_minuet_best_completion: Double? = null,

    // Amazing Grace
    @SerialName("song_amazing_grace_completions") val song_amazing_grace_completions: Int? = null,
    @SerialName("song_amazing_grace_perfect_completions") val song_amazing_grace_perfect_completions: Int? = null,
    @SerialName("song_amazing_grace_best_completion") val song_amazing_grace_best_completion: Double? = null,

    // Greensleeves
    @SerialName("song_greensleeves_completions") val song_greensleeves_completions: Int? = null,
    @SerialName("song_greensleeves_perfect_completions") val song_greensleeves_perfect_completions: Int? = null,
    @SerialName("song_greensleeves_best_completion") val song_greensleeves_best_completion: Double? = null,

    // La Vie en Rose
    @SerialName("song_vie_en_rose_completions") val song_vie_en_rose_completions: Int? = null,
    @SerialName("song_vie_en_rose_perfect_completions") val song_vie_en_rose_perfect_completions: Int? = null,
    @SerialName("song_vie_en_rose_best_completion") val song_vie_en_rose_best_completion: Double? = null,

    // Brahms' Lullaby
    @SerialName("song_brahms_completions") val song_brahms_completions: Int? = null,
    @SerialName("song_brahms_perfect_completions") val song_brahms_perfect_completions: Int? = null,
    @SerialName("song_brahms_best_completion") val song_brahms_best_completion: Double? = null,

    // Frere Jacques
    @SerialName("song_frere_jacques_completions") val song_frere_jacques_completions: Int? = null,
    @SerialName("song_frere_jacques_perfect_completions") val song_frere_jacques_perfect_completions: Int? = null,
    @SerialName("song_frere_jacques_best_completion") val song_frere_jacques_best_completion: Double? = null,

    // Pachelbel
    @SerialName("song_pachelbel_completions") val song_pachelbel_completions: Int? = null,
    @SerialName("song_pachelbel_perfect_completions") val song_pachelbel_perfect_completions: Int? = null,
    @SerialName("song_pachelbel_best_completion") val song_pachelbel_best_completion: Double? = null,

    // Ode to Joy
    @SerialName("song_hymn_joy_completions") val song_hymn_joy_completions: Int? = null,
    @SerialName("song_hymn_joy_perfect_completions") val song_hymn_joy_perfect_completions: Int? = null,
    @SerialName("song_hymn_joy_best_completion") val song_hymn_joy_best_completion: Double? = null
)