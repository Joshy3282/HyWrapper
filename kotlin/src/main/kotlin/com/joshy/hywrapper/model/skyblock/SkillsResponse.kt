package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.data.skyblock.SkillType
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient


/**
 * Lists information about skills.
 *
 * @property success Whether the request was successful.
 * @property cause The cause of the error, if the request failed.
 * @property lastUpdated The timestamp skills was last updated.
 * @property version SkyBlocks current version.
 * @property skills A list of [SkillType] containing information.
 * */
@Serializable
data class SkillsResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val lastUpdated: Long? = null,
    val version: String? = null,
    val skills: Map<SkillType, Skill>? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

/**
 * Information about a skill
 *
 * @property name The name of the skill (eg; Farming, Mining)
 * @property description The skills description
 * @property maxLevel Maximum level possible for the skill, including level cap increases.
 * @property levels A list of information and rewards about each level for a skill
 * */
@Serializable
data class Skill(
    val name: String? = null,
    val description: String? = null,
    val maxLevel: Int? = null,
    val levels: List<Level>? = null,
)

/**
 * Information and rewards about a level
 *
 * @property level The skill level
 * @property totalExpRequired The total amount of experience required for the level
 * @property unlocks A list of rewards for the level (eg; +250 Coins, +5 SkyBlock XP)
 * */
@Serializable
data class Level(
    val level: Int? = null,
    val totalExpRequired: Long? = null,
    val unlocks: List<String>? = null,
)
