package com.joshy.hywrapper.model.skyblock.profile

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
data class PlayerInventory(
    @SerialName("bag_contents")
    val bagContents: BagContents? = null,
    @SerialName("inv_contents")
    val invContents: InventoryObject? = null,
    @SerialName("ender_chest_contents")
    val enderChestContents: InventoryObject? = null,
    @SerialName("backpack_icons")
    val backpackIcons: Map<String, InventoryObject>? = null,
    @SerialName("inv_armor")
    val invArmor: InventoryObject? = null,
    @SerialName("equipment_contents")
    val equipmentContents: InventoryObject? = null,
    @SerialName("personal_vault_contents")
    val personalVaultContents: InventoryObject? = null,
    @SerialName("wardrobe_equipped_slot")
    val wardrobeEquippedSlot: Int? = null,
    @SerialName("backpack_contents")
    val backpackContents: Map<String, InventoryObject>? = null,
    @SerialName("sacks_counts")
    val sacksCounts: Map<String, Int>? = null, // TODO enum
    @SerialName("wardrobe_contents")
    val wardrobeContents: InventoryObject? = null,
)

@Serializable
data class BagContents(
    @SerialName("sacks_bag")
    val sacksBag: InventoryObject? = null,
    @SerialName("potion_bag")
    val potionBag: InventoryObject? = null,
    @SerialName("talisman_bag")
    val talismanBag: InventoryObject? = null,
    @SerialName("fishing_bag")
    val fishingBag: InventoryObject? = null,
    val quiver: InventoryObject? = null,
)

@Serializable
data class InventoryObject(
    val type: Int? = null,
    val data: String? = null,
)