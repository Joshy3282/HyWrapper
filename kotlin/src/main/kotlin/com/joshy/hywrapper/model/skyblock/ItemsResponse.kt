package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.data.skyblock.MuseumItem
import com.joshy.hywrapper.data.skyblock.StatType
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class ItemsResponse(
    override val success: Boolean = false,
    override val cause: String? = null,
    val lastUpdated: Long? = 0,
    val items: List<Item> = emptyList(),
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class Item(
    val material: String = "",
    val durability: Int = 0,
    val skin: Skin? = null,
    val name: String? = null,
    val category: String? = null,
    val tier: String? = null,
    @SerialName("npc_sell_price")
    val npcSellPrice: Int? = null,
    val id: String? = null,
    val salvages: List<Salvage> = emptyList(),
    @SerialName("rarity_salvageable")
    val raritySalvageable: Boolean? = null,
    val description: String? = null,
    @SerialName("item_model")
    val itemModel: String? = null,
    val stats: Map<StatType, Int> = emptyMap(),
    val unstackable: Boolean? = null,
    @SerialName("dungeon_item_conversion_cost")
    val dungeonItemConversionCost: DungeonItemConversionCost? = null,
    @SerialName("upgrade_costs")
    val upgradeCosts: List<List<UpgradeCost>> = emptyList(),
    @SerialName("museum_data")
    val museumData: MuseumData? = null,
    // TODO requirements
    val color: String = "",
    val soulbound: String = "",
    @SerialName("has_uuid")
    val hasUuid: Boolean? = null,
    @SerialName("can_auction")
    val canAuction: Boolean? = null,
    // TODO gemstone_slots
    val glowing: Boolean? = null,
    @SerialName("can_trade")
    val canTrade: Boolean? = null,
    @SerialName("can_place")
    val canPlace: Boolean? = null,
    val museum: Boolean? = null,
    val generator: String = "",
    @SerialName("generator_tier")
    val generatorTier: Int = 0,
    val furniture: String = "",
    // TODO item_specific
    val editioned: Boolean? = null,
    @SerialName("gear_score")
    val gearScore: Int = 0,
    @SerialName("dungeon_item")
    val dungeonItem: Boolean? = null,
    @SerialName("catacombs_requirements")
    val catacombsRequirement: CatacombsRequirement? = null,
    @SerialName("can_have_booster")
    val canHaveBooster: Boolean? = null,
    @SerialName("hide_from_api")
    val hideFromApi: Boolean? = null,
    @SerialName("can_recombobulate")
    val canRecombobulate: Boolean? = null,
    @SerialName("salvageable_from_recipe")
    val salvageableFromRecipe: Boolean? = null,
    @SerialName("motes_sell_price")
    val motesSellPrice: Int? = 0,
    @SerialName("double_tap_to_drop")
    val doubleTapToDrop: Boolean? = null,
    // TODO enchantments. why are there only a few
    @SerialName("rift_transferrable")
    val riftTransferrable: Boolean? = null,
    val origin: String = "",
    @SerialName("hide_from_viewrecipe_command")
    val hideFromViewrecipeCommand: Boolean? = null,
    @SerialName("force_wipe_recomb")
    val forceWipeRecomb: Boolean? = null,
    @SerialName("ability_damage_scaling")
    val abilityDamageScaling: Int = 0,
    // TODO tiered_stats
    val crystal: String = "",
    @SerialName("can_burn_in_furnace")
    val canBurnInFurnace: Boolean? = null,
    // TODO salvage? only used once looks temp or mistake
    val serializable: Boolean? = null,
    @SerialName("can_have_attributes")
    val canHaveAttributes: Boolean? = null,
    @SerialName("can_interact")
    val canInteract: Boolean? = null,
    @SerialName("can_interact_right_click")
    val canInteractRightClick: Boolean? = null,
    @SerialName("private_island")
    val privateIsland: String? = null,
    @SerialName("can_have_power_scroll")
    val canHavePowerScroll: Boolean? = null,
    @SerialName("can_interact_entity")
    val canInteractEntity: Boolean? = null,
    @SerialName("MINING_FORTUNE")
    val miningFortune: Int? = null,
    val rarity: String? = null,
    @SerialName("sword_type")
    val swordType: String? = null,
    @SerialName("is_upgradeable_without_soulbinding")
    val isUpgradeableWithoutSoulbinding: Boolean? = null,
    // TODO recipes
    @SerialName("cannot_reforge")
    val cannotReforge: Boolean? = null,
    @SerialName("lose_motes_value_on_transfer")
    val loseMotesValueOnTransfer: Boolean? = null,
    // TODO prestige
)

@Serializable
data class Skin(
    val value: String? = null,
    val signature: String? = null,
)

@Serializable
data class Salvage(
    val type: String? = null,
    @SerialName("essence_type")
    val essenceType: String? = null,
    val amount: Int? = null,
)

@Serializable
data class DungeonItemConversionCost(
    @SerialName("essence_type")
    val essenceType: String = "",
    val amount: Int = 0,
)

@Serializable
data class UpgradeCost(
    val type: String = "",
    @SerialName("essence_type")
    val essenceType: String = "",
    val amount: Int = 0,
)

@Serializable
data class MuseumData(
    val category: String = "",
    val parent: Map<MuseumItem, MuseumItem> = emptyMap(),
    @SerialName("armor_set_donation_xp")
    val armorSetDonationXp: Map<MuseumItem, Int> = emptyMap(),
    @SerialName("game_stage")
    val gameStage: String = "",
)

@Serializable
data class CatacombsRequirement(
    val type: String = "",
    @SerialName("dungeon_type")
    val dungeonType: String = "",
    val level: Int = 0,
)
