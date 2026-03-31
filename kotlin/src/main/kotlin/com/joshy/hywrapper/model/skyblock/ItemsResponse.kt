package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.data.skyblock.EssenceType
import com.joshy.hywrapper.data.skyblock.MuseumItem
import com.joshy.hywrapper.data.skyblock.SkillType
import com.joshy.hywrapper.data.skyblock.StatType
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient
import kotlinx.serialization.json.JsonElement

/**
 * Information about Skyblock's items.
 *
 * @property success Whether the request was successful.
 * @property cause The cause of the error, if the request failed.
 * @property lastUpdated Timestamp of when items were last modified.
 * @property items A list of [Item] information.
 * */
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

/**
 * Information about a Skyblock Item
 *
 * @property material Vanilla material used for the item
 * @property durability Meta for the material
 * @property skin Information about a skull heads skin
 * @property name Name of the item
 * @property category Category of the item
 * @property tier The items rarity
 * @property npcSellPrice Sell price of the item to npcs
 * @property id Item ID of the item
 * @property salvages Rewards for salvaging the item
 * @property raritySalvageable
 * @property description Item description
 * @property itemModel Item used for 1.21+
 * @property stats Stats given by the item
 * @property unstackable If the item is stackable
 * @property dungeonItemConversionCost The cost to convert the item to a dungeon item
 * @property upgradeCosts A list of upgrade costs for dungeon items
 * @property museumData Information about the items museum data
 * @property requirements Requirements to use the item
 * @property color Color of leather armor
 * @property soulbound Type of soulbound the item is
 * @property hasUuid
 * @property canAuction If the item can be auctioned
 * @property gemstoneSlots A list of gemstone slots on the item
 * @property glowing Whether the item has glint
 * @property canTrade Whether the item can be traded
 * @property canPlace Whether the item can be placed
 * @property museum If the item can be put into the special category of museum
 * @property generator The type of minion
 * @property generatorTier The tier of the minion
 * @property furniture The type of furniture
 * @property itemSpecific Specific information about the item
 * @property editioned Used for the Villager Doll to prevent editions
 * @property gearScore The gear score of the item
 * @property dungeonItem Whether the item is a dungeon item
 * @property catacombsRequirement Requirements to use the item in dungeons
 * @property canHaveBooster Whether the item can have a foraging booster
 * @property hideFromApi Whether the item is hidden from the api
 * @property canRecombobulate Whether the item can be recombobulated
 * @property salvageableFromRecipe TODO unknown
 * @property motesSellPrice Motes sell price of the item
 * @property doubleTapToDrop Whether the item requires double tap to drop
 * @property enchantments Enchantments on the item
 * @property riftTransferrable Whether the item is rift transferrable
 * @property origin Used for Rift items that are obtained in the Rift
 * @property hideFromViewrecipeCommand Whether the item is hidden from the viewrecipe command
 * @property forceWipeRecomb Whether the item force wipes recombobulator
 * @property abilityDamageScaling Ability damage scaling of the item
 * @property tieredStats Tiered stats for dungeon items
 * @property crystal Type of crystal
 * @property canBurnInFurnace Whether the item can be burned in a furnace
 * @property salvage Salvage information for the item
 * @property serializable TODO unknown
 * @property canHaveAttributes TODO unknown
 * @property canInteract Whether the item can interact with things
 * @property canInteractRightClick Whether the item can interact using right click with things
 * @property privateIsland Type of island spawned
 * @property canHavePowerScroll Whether the item can have a power scroll
 * @property canInteractEntity Whether the item can interact with an entity
 * @property miningFortune Used for titanium belt? TODO why
 * @property rarity Used for Fishy Penguin Minion Skin and Polar Bear Minion Skin for Rarity
 * @property swordType Type of sword
 * @property isUpgradeableWithoutSoulbinding TODO unknown
 * @property recipes Recipes for the item
 * @property cannotReforge Whether the item cannot be reforged
 * @property loseMotesValueOnTransfer Whether the item loses motes value on transfer
 * @property prestige Upgrades for crimson isle armor
 * */
@Serializable
data class Item(
    val material: String? = null,
    val durability: Int? = null,
    val skin: Skin? = null,
    val name: String? = null,
    val category: String? = null,// TODO enum
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
    val soulbound: String? = null, // TODO enum
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
    val generator: String? = null, // TODO enum
    @SerialName("generator_tier")
    val generatorTier: Int? = null,
    val furniture: String? = null, // TODO enum
    @SerialName("item_specific")
    val itemSpecific: Map<String, JsonElement>? = null, // TODO literally what is the point of the endpoint
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

/**
 * Information about a player head
 *
 * @property value Base64 encoded JSON string for skin information
 * @property signature Mojang internal proof
 * */
@Serializable
data class Skin(
    val value: String? = null,
    val signature: String? = null,
)

/**
 * Rewards for salvaging the item
 *
 * @property rewardType Type of reward, always `ESSENCE`.
 * @property essenceType Type of essence given.
 * @property amount Amount of essence given
 * */
@Serializable
data class Salvage(
    @SerialName("type")
    val rewardType: String? = null,
    @SerialName("essence_type")
    val essenceType: EssenceType? = null,
    val amount: Int? = null,
)

/**
 * Unknown. Used one time for an item with ID "NETHERITE_HELMET"
 * */
@Serializable
data class SalvageData(
    @SerialName("item_id")
    val itemId: String? = null,
    val amount: Int? = null,
)

/**
 * Information about to cost to convert an item to a dungeon item
 *
 * @property essenceType The type of essence needed.
 * @property amount The amount of essence needed.
 * */
@Serializable
data class DungeonItemConversionCost(
    @SerialName("essence_type")
    val essenceType: EssenceType? = null,
    val amount: Int? = null,
)

/**
 * Information about an upgrade for a dungeon item
 *
 * @property type Upgrade type (ITEM or ESSENCE)
 * @property essenceType Type of essence needed.
 * @property amount Amount of essence or item needed
 * @property itemId Item ID needed.
 * */
@Serializable
data class UpgradeCost(
    val type: String? = null, // TODO enum
    @SerialName("essence_type")
    val essenceType: EssenceType? = null,
    val amount: Int? = null,
    @SerialName("item_id")
    val itemId: String? = null,
)

/**
 * Information about an items museum donation
 *
 * @property category The museum category the item belongs to
 * @property parent Parent items TODO better explanation
 * @property armorSetDonationXp Amount of XP given for the armor set
 * @property gameStage The level gamestage for the item
 * @property donationXp Amount of XP given for the item
 * */
@Serializable
data class MuseumData(
    val category: String? = null, // TODO enum
    val parent: Map<MuseumItem, MuseumItem>? = null,
    @SerialName("armor_set_donation_xp")
    val armorSetDonationXp: Map<MuseumItem, Int>? = null,
    @SerialName("game_stage")
    val gameStage: String? = null,
    @SerialName("donation_xp")
    val donationXp: Int? = null,
)

/**
 * Information about the catacombs requirements for an item
 *
 * @property type Type of requirement (DUNGEON_SKILL)
 * @property dungeonType Always CATACOMBS
 * @property level Level for the requirement needed
 * */
@Serializable
data class CatacombsRequirement(
    val type: String? = null, // TODO enum
    @SerialName("dungeon_type")
    val dungeonType: String? = null,
    val level: Int? = null,
)

/**
 * Information about item requirements
 *
 * @property type Type of requirement
 * @property skill Which skill is required
 * @property slayerBossType Which slayer is required
 * @property level Level of slayer/skill/dungeons required
 * @property dungeonType Which dungeons are required
 * */
@Serializable
data class Requirement(
    val type: String? = null, // TODO enum
    val skill: SkillType? = null,
    @SerialName("slayer_boss_type")
    val slayerBossType: String? = null,
    val level: Int? = null,
    @SerialName("dungeon_type")
    val dungeonType: String? = null,
)

/**
 * Information about the items gemstone slots
 *
 * @property slotType Which gemstone is allowed in the slot
 * @property costs The costs to unlock the gemstone slot
 * @property requirements Requirements for gemstones on farming tools
 * */
@Serializable
data class GemstoneSlot(
    @SerialName("slot_type")
    val slotType: String? = null, // TODO enum
    val costs: List<GemstoneCost>? = null,
    val requirements: List<GemstoneRequirement>? = null,
)

/**
 * Information about the cost for a gemstone slot
 *
 * @property type Type of cost (ITEM, COINS)
 * @property itemId Item ID of the item required
 * @property amount Amount of the item/essence required
 * @property coins Amount of coins required
 * @property essenceType Type of essence required
 * */
@Serializable
data class GemstoneCost(
    val type: String? = null, // TODO enum
    @SerialName("item_id")
    val itemId: String? = null,
    val amount: Int? = null,
    val coins: Int? = null,
    @SerialName("essence_type")
    val essenceType: EssenceType? = null,
)

/**
 * Information about requirements to unlock a gemstone slot
 *
 * @property type Type of requirement (always ITEM_DATA)
 * @property dataKey TODO
 * @property value TODO
 * @property operator TODO
 * */
@Serializable
data class GemstoneRequirement(
    val type: String? = null,
    @SerialName("data_key")
    val dataKey: String? = null,
    val value: String? = null,
    val operator: String? = null,
)

/**
 * Information about a recipe to create the item
 *
 * @property output Item output by the recipe (usually the same as the item id)
 * @property ingredientSymbols Ingredient symbols used for the matrix
 * @property matrix Ingredient matrix used to determine cost
 * */
@Serializable
data class Recipe(
    val output: RecipeOutput? = null,
    @SerialName("ingredient_symbols")
    val ingredientSymbols: Map<String, String>? = null,
    val matrix: List<String?>? = null,
)

/**
 * Information about the item output
 *
 * @property itemId Item ID of the created item
 * */
@Serializable
data class RecipeOutput(
    @SerialName("item_id")
    val itemId: String? = null,
)

/**
 * Information about Crimson Isle set upgrades
 *
 * @property itemId Item ID of the created item
 * @property costs Costs for the upgrades
 * */
@Serializable
data class Prestige(
    @SerialName("item_id")
    val itemId: String? = null,
    val costs: List<GemstoneCost>? = null,
)

