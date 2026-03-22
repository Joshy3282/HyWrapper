package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.data.skyblock.MuseumItem
import com.joshy.hywrapper.data.skyblock.StatType
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient
import kotlinx.serialization.json.JsonElement

@Serializable
data class ItemsResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val lastUpdated: Long? = null,
    val items: List<Item>? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class Item(
    val material: String? = null,
    val durability: Int? = null,
    val skin: Skin? = null,
    val name: String? = null,
    val category: String? = null,
    val tier: String? = null,
    @SerialName("npc_sell_price")
    val npcSellPrice: Int? = null,
    val id: String? = null,
    val salvages: List<Salvage>? = null,
    @SerialName("rarity_salvageable")
    val raritySalvageable: Boolean? = null,
    val description: String? = null,
    @SerialName("item_model")
    val itemModel: String? = null,
    val stats: Map<StatType, Int>? = null,
    val unstackable: Boolean? = null,
    @SerialName("dungeon_item_conversion_cost")
    val dungeonItemConversionCost: DungeonItemConversionCost? = null,
    @SerialName("upgrade_costs")
    val upgradeCosts: List<List<UpgradeCost>>? = null,
    @SerialName("museum_data")
    val museumData: MuseumData? = null,
    val requirements: List<Requirement>? = null,
    val color: String? = null,
    val soulbound: String? = null,
    @SerialName("has_uuid")
    val hasUuid: Boolean? = null,
    @SerialName("can_auction")
    val canAuction: Boolean? = null,
    @SerialName("gemstone_slots")
    val gemstoneSlots: List<GemstoneSlot>? = null,
    val glowing: Boolean? = null,
    @SerialName("can_trade")
    val canTrade: Boolean? = null,
    @SerialName("can_place")
    val canPlace: Boolean? = null,
    val museum: Boolean? = null,
    val generator: String? = null,
    @SerialName("generator_tier")
    val generatorTier: Int? = null,
    val furniture: String? = null,
    @SerialName("item_specific")
    val itemSpecific: Map<String, JsonElement>? = null,
    val editioned: Boolean? = null,
    @SerialName("gear_score")
    val gearScore: Int? = null,
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
    val motesSellPrice: Int? = null,
    @SerialName("double_tap_to_drop")
    val doubleTapToDrop: Boolean? = null,
    val enchantments: Map<String, Int>? = null,
    @SerialName("rift_transferrable")
    val riftTransferrable: Boolean? = null,
    val origin: String? = null,
    @SerialName("hide_from_viewrecipe_command")
    val hideFromViewrecipeCommand: Boolean? = null,
    @SerialName("force_wipe_recomb")
    val forceWipeRecomb: Boolean? = null,
    @SerialName("ability_damage_scaling")
    val abilityDamageScaling: Int? = null,
    @SerialName("tiered_stats")
    val tieredStats: Map<StatType, List<Int>>? = null,
    val crystal: String? = null,
    @SerialName("can_burn_in_furnace")
    val canBurnInFurnace: Boolean? = null,
    val salvage: SalvageData? = null,
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
    val recipes: List<Recipe>? = null,
    @SerialName("cannot_reforge")
    val cannotReforge: Boolean? = null,
    @SerialName("lose_motes_value_on_transfer")
    val loseMotesValueOnTransfer: Boolean? = null,
    val prestige: Prestige? = null,
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
data class SalvageData(
    @SerialName("item_id")
    val itemId: String? = null,
    val amount: Int? = null,
)

@Serializable
data class DungeonItemConversionCost(
    @SerialName("essence_type")
    val essenceType: String? = null,
    val amount: Int? = null,
)

@Serializable
data class UpgradeCost(
    val type: String? = null,
    @SerialName("essence_type")
    val essenceType: String? = null,
    val amount: Int? = null,
    @SerialName("item_id")
    val itemId: String? = null,
)

@Serializable
data class MuseumData(
    val category: String? = null,
    val parent: Map<MuseumItem, MuseumItem>? = null,
    @SerialName("armor_set_donation_xp")
    val armorSetDonationXp: Map<MuseumItem, Int>? = null,
    @SerialName("game_stage")
    val gameStage: String? = null,
)

@Serializable
data class CatacombsRequirement(
    val type: String? = null,
    @SerialName("dungeon_type")
    val dungeonType: String? = null,
    val level: Int? = null,
)

@Serializable
data class Requirement(
    val type: String? = null,
    val skill: String? = null,
    @SerialName("slayer_boss_type")
    val slayerBossType: String? = null,
    val level: Int? = null,
    @SerialName("dungeon_type")
    val dungeonType: String? = null,
)

@Serializable
data class GemstoneSlot(
    @SerialName("slot_type")
    val slotType: String? = null,
    val costs: List<GemstoneCost>? = null,
    val requirements: List<GemstoneRequirement>? = null,
)

@Serializable
data class GemstoneCost(
    val type: String? = null,
    @SerialName("item_id")
    val itemId: String? = null,
    val amount: Int? = null,
    val coins: Int? = null,
    @SerialName("essence_type")
    val essenceType: String? = null,
)

@Serializable
data class GemstoneRequirement(
    val type: String? = null,
    @SerialName("data_key")
    val dataKey: String? = null,
    val value: String? = null,
    val operator: String? = null,
)

@Serializable
data class Recipe(
    val output: RecipeOutput? = null,
    @SerialName("ingredient_symbols")
    val ingredientSymbols: Map<String, String>? = null,
    val matrix: List<String?>? = null,
)

@Serializable
data class RecipeOutput(
    @SerialName("item_id")
    val itemId: String? = null,
)

@Serializable
data class Prestige(
    @SerialName("item_id")
    val itemId: String? = null,
    val costs: List<GemstoneCost>? = null,
)
