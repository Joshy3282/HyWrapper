package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.data.skyblock.SkillType
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class CollectionsResponse(
    override val success: Boolean = false,
    override val cause: String? = null,
    val lastUpdated: Long = 0L,
    val version: String = "",
    val collections: Map<String, Collection> = emptyMap(),
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null

    fun getCollection(skill: SkillType): Collection? {
        return collections[skill.name]
    }
}

@Serializable
data class Collection(
    val name: String = "",
    val items: Map<String, CollectionItem> = emptyMap(),
)

@Serializable
data class CollectionItem(
    val name: String = "",
    val maxTiers: Int = 0,
    val tiers: List<CollectionTier> = emptyList(),
)

@Serializable
data class CollectionTier(
    val tier: Int = 0,
    val amountRequired: Int = 0,
    val unlocks: List<String> = emptyList(),
)
