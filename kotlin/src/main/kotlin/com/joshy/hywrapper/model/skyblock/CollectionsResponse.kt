package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.data.skyblock.SkillType
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

/**
 * Information about collections.
 *
 * @property success Whether the request was successful.
 * @property cause The cause of the error, if the request failed.
 * @property lastUpdated Timestamp when collections were last modified.
 * @property version Skyblock version.
 * @property collections The list of [Collection] information.
 * */
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

/**
 * List of all collections.
 *
 * @property name Skill name of the collection.
 * @property items List of collection items for the skill.
 * */
@Serializable
data class Collection(
    val name: String? = null, // TODO change this to skill enum
    val items: Map<String, CollectionItem>? = null,
)

/**
 * Information about a collection.
 *
 * @property name Name of the collection.
 * @property maxTiers Max amount of tiers in the collection.
 * @property tiers List of tiers information.
 * */
@Serializable
data class CollectionItem(
    val name: String? = null,
    val maxTiers: Int? = null,
    val tiers: List<CollectionTier>? = null,
)

/**
 * Information about a collection item tier.
 *
 * @property tier What tier it is.
 * @property amountRequired The collected amount required for the tier.
 * @property unlocks A list of what the tier unlocks once reached.
 * */
@Serializable
data class CollectionTier(
    val tier: Int? = null,
    val amountRequired: Int? = null,
    val unlocks: List<String>? = null,
)
