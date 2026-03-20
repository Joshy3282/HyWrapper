package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.data.skyblock.SkillType
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class SkillsResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val lastUpdated: Long? = null,
    val version: String? = null,
    val skills: Map<String, Skill>? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null

    fun getSkill(skillType: SkillType): Skill? {
        return skills?.get(skillType.name)
    }
}

@Serializable
data class Skill(
    val name: String? = null,
    val description: String? = null,
    val maxLevel: Int? = null,
    val levels: List<Level>? = null,
)

@Serializable
data class Level(
    val level: Int? = null,
    val totalExpRequired: Double? = null,
    val unlocks: List<String>? = null,
)
