import { HypixelResponse } from "../../types";
import { MuseumItem } from "../../data/skyblock/MuseumItem";
import { StatType } from "../../data/skyblock/StatType";
import { EssenceType } from "../../data/skyblock/EssenceType";
import { SkillType } from "../../data/skyblock/SkillType";

/**
 * Information about Skyblock's items.
 *
 * @property success Whether the request was successful.
 * @property cause The cause of the error, if the request failed.
 * @property lastUpdated Timestamp of when items were last modified.
 * @property items A list of {@link Item} information.
 */
export interface ItemsResponse extends HypixelResponse {
    lastUpdated?: number;
    items?: Item[];
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
 * @property npc_sell_price Sell price of the item to npcs
 * @property id Item ID of the item
 * @property salvages Rewards for salvaging the item
 * @property rarity_salvageable
 * @property description Item description
 * @property item_model Item used for 1.21+
 * @property stats Stats given by the item
 * @property unstackable If the item is stackable
 * @property dungeon_item_conversion_cost The cost to convert the item to a dungeon item
 * @property upgrade_costs A list of upgrade costs for dungeon items
 * @property museum_data Information about the items museum data
 * @property requirements Requirements to use the item
 * @property color Color of leather armor
 * @property soulbound Type of soulbound the item is
 * @property has_uuid
 * @property can_auction If the item can be auctioned
 * @property gemstone_slots A list of gemstone slots on the item
 * @property glowing Whether the item has glint
 * @property can_trade Whether the item can be traded
 * @property can_place Whether the item can be placed
 * @property museum If the item can be put into the special category of museum
 * @property generator The type of minion
 * @property generator_tier The tier of the minion
 * @property furniture The type of furniture
 * @property item_specific Specific information about the item
 * @property editioned Used for the Villager Doll to prevent editions
 * @property gear_score The gear score of the item
 * @property dungeon_item Whether the item is a dungeon item
 * @property catacombs_requirements Requirements to use the item in dungeons
 * @property can_have_booster Whether the item can have a foraging booster
 * @property hide_from_api Whether the item is hidden from the api
 * @property can_recombobulate Whether the item can be recombobulated
 * @property salvageable_from_recipe TODO unknown
 * @property motes_sell_price Motes sell price of the item
 * @property double_tap_to_drop Whether the item requires double tap to drop
 * @property enchantments Enchantments on the item
 * @property rift_transferrable Whether the item is rift transferrable
 * @property origin Used for Rift items that are obtained in the Rift
 * @property hide_from_viewrecipe_command Whether the item is hidden from the viewrecipe command
 * @property force_wipe_recomb Whether the item force wipes recombobulator
 * @property ability_damage_scaling Ability damage scaling of the item
 * @property tiered_stats Tiered stats for dungeon items
 * @property crystal Type of crystal
 * @property can_burn_in_furnace Whether the item can be burned in a furnace
 * @property salvage Salvage information for the item
 * @property serializable TODO unknown
 * @property can_have_attributes TODO unknown
 * @property can_interact Whether the item can interact with things
 * @property can_interact_right_click Whether the item can interact using right click with things
 * @property private_island Type of island spawned
 * @property can_have_power_scroll Whether the item can have a power scroll
 * @property can_interact_entity Whether the item can interact with an entity
 * @property MINING_FORTUNE Used for titanium belt? TODO why
 * @property rarity Used for Fishy Penguin Minion Skin and Polar Bear Minion Skin for Rarity
 * @property sword_type Type of sword
 * @property is_upgradeable_without_soulbinding TODO unknown
 * @property recipes Recipes for the item
 * @property cannot_reforge Whether the item cannot be reforged
 * @property lose_motes_value_on_transfer Whether the item loses motes value on transfer
 * @property prestige Upgrades for crimson isle armor
 */
export interface Item {
    material?: string;
    durability?: number;
    skin?: Skin;
    name?: string;
    category?: string;
    tier?: string;
    npc_sell_price?: number;
    id?: string;
    salvages?: Salvage[];
    rarity_salvageable?: boolean;
    description?: string;
    item_model?: string;
    stats?: Record<StatType, number>;
    unstackable?: boolean;
    dungeon_item_conversion_cost?: DungeonItemConversionCost;
    upgrade_costs?: UpgradeCost[][];
    museum_data?: MuseumData;
    requirements?: Requirement[];
    color?: string;
    soulbound?: string;
    has_uuid?: boolean;
    can_auction?: boolean;
    gemstone_slots?: GemstoneSlot[];
    glowing?: boolean;
    can_trade?: boolean;
    can_place?: boolean;
    museum?: boolean;
    generator?: string;
    generator_tier?: number;
    furniture?: string;
    item_specific?: Record<string, any>;
    editioned?: boolean;
    gear_score?: number;
    dungeon_item?: boolean;
    catacombs_requirements?: CatacombsRequirement;
    can_have_booster?: boolean;
    hide_from_api?: boolean;
    can_recombobulate?: boolean;
    salvageable_from_recipe?: boolean;
    motes_sell_price?: number;
    double_tap_to_drop?: boolean;
    enchantments?: Record<string, number>;
    rift_transferrable?: boolean;
    origin?: string;
    hide_from_viewrecipe_command?: boolean;
    force_wipe_recomb?: boolean;
    ability_damage_scaling?: number;
    tiered_stats?: Record<StatType, number[]>;
    crystal?: string;
    can_burn_in_furnace?: boolean;
    salvage?: SalvageData;
    serializable?: boolean;
    can_have_attributes?: boolean;
    can_interact?: boolean;
    can_interact_right_click?: boolean;
    private_island?: string;
    can_have_power_scroll?: boolean;
    can_interact_entity?: boolean;
    MINING_FORTUNE?: number;
    rarity?: string;
    sword_type?: string;
    is_upgradeable_without_soulbinding?: boolean;
    recipes?: Recipe[];
    cannot_reforge?: boolean;
    lose_motes_value_on_transfer?: boolean;
    prestige?: Prestige;
}

/**
 * Information about a player head
 *
 * @property value Base64 encoded JSON string for skin information
 * @property signature Mojang internal proof
 */
export interface Skin {
    value?: string;
    signature?: string;
}

/**
 * Rewards for salvaging the item
 *
 * @property type Type of reward, always `ESSENCE`.
 * @property essence_type Type of essence given.
 * @property amount Amount of essence given
 */
export interface Salvage {
    type?: string;
    essence_type?: EssenceType;
    amount?: number;
}

/**
 * Unknown. Used one time for an item with ID "NETHERITE_HELMET"
 */
export interface SalvageData {
    item_id?: string;
    amount?: number;
}

/**
 * Information about to cost to convert an item to a dungeon item
 *
 * @property essence_type The type of essence needed.
 * @property amount The amount of essence needed.
 */
export interface DungeonItemConversionCost {
    essence_type?: EssenceType;
    amount?: number;
}

/**
 * Information about an upgrade for a dungeon item
 *
 * @property type Upgrade type (ITEM or ESSENCE)
 * @property essence_type Type of essence needed.
 * @property amount Amount of essence or item needed
 * @property item_id Item ID needed.
 */
export interface UpgradeCost {
    type?: string;
    essence_type?: EssenceType;
    amount?: number;
    item_id?: string;
}

/**
 * Information about an items museum donation
 *
 * @property category The museum category the item belongs to
 * @property parent Parent items TODO better explanation
 * @property armor_set_donation_xp Amount of XP given for the armor set
 * @property game_stage The level gamestage for the item
 * @property donation_xp Amount of XP given for the item
 */
export interface MuseumData {
    category?: string;
    parent?: Record<MuseumItem, MuseumItem>;
    armor_set_donation_xp?: Record<MuseumItem, number>;
    game_stage?: string;
    donation_xp?: number;
}

/**
 * Information about the catacombs requirements for an item
 *
 * @property type Type of requirement (DUNGEON_SKILL)
 * @property dungeon_type Always CATACOMBS
 * @property level Level for the requirement needed
 */
export interface CatacombsRequirement {
    type?: string;
    dungeon_type?: string;
    level?: number;
}

/**
 * Information about item requirements
 *
 * @property type Type of requirement
 * @property skill Which skill is required
 * @property slayer_boss_type Which slayer is required
 * @property level Level of slayer/skill/dungeons required
 * @property dungeon_type Which dungeons are required
 */
export interface Requirement {
    type?: string;
    skill?: SkillType;
    slayer_boss_type?: string;
    level?: number;
    dungeon_type?: string;
}

/**
 * Information about the items gemstone slots
 *
 * @property slot_type Which gemstone is allowed in the slot
 * @property costs The costs to unlock the gemstone slot
 * @property requirements Requirements for gemstones on farming tools
 */
export interface GemstoneSlot {
    slot_type?: string;
    costs?: GemstoneCost[];
    requirements?: GemstoneRequirement[];
}

/**
 * Information about the cost for a gemstone slot
 *
 * @property type Type of cost (ITEM, COINS)
 * @property item_id Item ID of the item required
 * @property amount Amount of the item/essence required
 * @property coins Amount of coins required
 * @property essence_type Type of essence required
 */
export interface GemstoneCost {
    type?: string;
    item_id?: string;
    amount?: number;
    coins?: number;
    essence_type?: EssenceType;
}

/**
 * Information about requirements to unlock a gemstone slot
 *
 * @property type Type of requirement (always ITEM_DATA)
 * @property data_key TODO
 * @property value TODO
 * @property operator TODO
 */
export interface GemstoneRequirement {
    type?: string;
    data_key?: string;
    value?: string;
    operator?: string;
}

/**
 * Information about a recipe to create the item
 *
 * @property output Item output by the recipe (usually the same as the item id)
 * @property ingredient_symbols Ingredient symbols used for the matrix
 * @property matrix Ingredient matrix used to determine cost
 */
export interface Recipe {
    output?: RecipeOutput;
    ingredient_symbols?: Record<string, string>;
    matrix?: (string | null)[];
}

/**
 * Information about the item output
 *
 * @property item_id Item ID of the created item
 */
export interface RecipeOutput {
    item_id?: string;
}

/**
 * Information about Crimson Isle set upgrades
 *
 * @property item_id Item ID of the created item
 * @property costs Costs for the upgrades
 */
export interface Prestige {
    item_id?: string;
    costs?: GemstoneCost[];
}
