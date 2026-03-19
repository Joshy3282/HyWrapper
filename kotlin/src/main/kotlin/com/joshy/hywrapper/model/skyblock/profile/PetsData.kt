package com.joshy.hywrapper.model.skyblock.profile

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
data class PetsData(
    @SerialName("pet_care")
    val petCare: PetCare? = null,
    val autopet: Autopet? = null,
    val pets: List<PetData> = emptyList(),
)

@Serializable
data class PetCare(
    @SerialName("coins_spent")
    val coinsSpent: Double = 0.0,
    // TODO enum
    @SerialName("pet_types_sacrificed")
    val petTypesSacrificed: List<String> = emptyList(),
)

@Serializable
data class Autopet(
    @SerialName("rules_limit")
    val rulesLimit: Int = 0,
    val rules: List<AutopetRule> = emptyList(),
    val migrated: Boolean? = null,
    @SerialName("migrated_2")
    val migrated2: Boolean? = null,
)

@Serializable
data class AutopetRule(
    val uuid: String = "",
    // TODO enum
    val id: String = "",
    val name: String = "",
    val uniqueId: String = "",
    val exceptions: List<AutopetException> = emptyList(),
    val disabled: Boolean = false,
    // TODO enums
    val data: Map<String, String> = emptyMap(),
)

@Serializable
data class AutopetException(
    val id: String = "",
    // TODO enums
    val data: Map<String, String> = emptyMap(),
)

@Serializable
data class PetData(
    val uuid: String = "",
    val uniqueId: String = "",
    // TODO enum
    val type: String = "",
    val exp: Double = 0.0,
    val active: Boolean? = null,
    // TODO enum
    val tier: String = "",
    // TODO enum
    val heldItem: String = "",
    val candyUsed: Int = 0,
    val petSoulbound: Boolean? = null,
    // TODO enum
    val skin: String = "",
    // TODO enum
    val extra: Map<String, Int> = emptyMap(),
)
