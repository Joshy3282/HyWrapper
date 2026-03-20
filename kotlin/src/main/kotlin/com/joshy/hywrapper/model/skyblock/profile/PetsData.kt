package com.joshy.hywrapper.model.skyblock.profile

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
data class PetsData(
    @SerialName("pet_care")
    val petCare: PetCare? = null,
    val autopet: Autopet? = null,
    val pets: List<PetData>? = null,
)

@Serializable
data class PetCare(
    @SerialName("coins_spent")
    val coinsSpent: Double? = null,
    // TODO enum
    @SerialName("pet_types_sacrificed")
    val petTypesSacrificed: List<String>? = null,
)

@Serializable
data class Autopet(
    @SerialName("rules_limit")
    val rulesLimit: Int? = null,
    val rules: List<AutopetRule>? = null,
    val migrated: Boolean? = null,
    @SerialName("migrated_2")
    val migrated2: Boolean? = null,
)

@Serializable
data class AutopetRule(
    val uuid: String? = null,
    // TODO enum
    val id: String? = null,
    val name: String? = null,
    val uniqueId: String? = null,
    val exceptions: List<AutopetException>? = null,
    val disabled: Boolean? = null,
    // TODO enums
    val data: Map<String, String>? = null,
)

@Serializable
data class AutopetException(
    val id: String? = null,
    // TODO enums
    val data: Map<String, String>? = null,
)

@Serializable
data class PetData(
    val uuid: String? = null,
    val uniqueId: String? = null,
    // TODO enum
    val type: String? = null,
    val exp: Double? = null,
    val active: Boolean? = null,
    // TODO enum
    val tier: String? = null,
    // TODO enum
    val heldItem: String? = null,
    val candyUsed: Int? = null,
    val petSoulbound: Boolean? = null,
    // TODO enum
    val skin: String? = null,
    // TODO enum
    val extra: Map<String, Int>? = null,
)
