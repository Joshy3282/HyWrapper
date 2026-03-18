package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.data.skyblock.SkillType
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class SkillsResponse(
    override val success: Boolean = false,
    override val cause: String? = null,
    val lastUpdated: Long = 0L,
    val version: String = "",
    val skills: Map<String, Skill> = emptyMap(),
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null

    fun getSkill(skillType: SkillType): Skill? {
        return skills[skillType.name]
    }
}

@Serializable
data class Skill(
    val name: String = "",
    val description: String = "",
    val maxLevel: Int = 0,
    val levels: List<Level> = emptyList(),
)

@Serializable
data class Level(
    val level: Int,
    val totalExpRequired: Double = 0.0,
    val unlocks: List<String> = emptyList(),
)
