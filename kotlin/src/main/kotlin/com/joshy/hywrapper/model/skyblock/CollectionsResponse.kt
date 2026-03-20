package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.data.skyblock.SkillType
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class CollectionsResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val lastUpdated: Long? = null,
    val version: String? = null,
    val collections: Map<String, Collection>? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null

    fun getCollection(skill: SkillType): Collection? {
        return collections?.get(skill.name)
    }
}

@Serializable
data class Collection(
    val name: String? = null,
    val items: Map<String, CollectionItem>? = null,
)

@Serializable
data class CollectionItem(
    val name: String? = null,
    val maxTiers: Int? = null,
    val tiers: List<CollectionTier>? = null,
)

@Serializable
data class CollectionTier(
    val tier: Int? = null,
    val amountRequired: Int? = null,
    val unlocks: List<String>? = null,
)
