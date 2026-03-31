from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.data.skyblock.essence_type import EssenceType
from hywrapper.data.skyblock.museum_item import MuseumItem
from hywrapper.data.skyblock.skill_type import SkillType
from hywrapper.data.skyblock.stat_type import StatType
from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class ItemsResponse(HypixelResponse):
    """
    Information about Skyblock's items.

    :param success: Whether the request was successful.
    :param cause: The cause of the error, if the request failed.
    :param last_updated: Timestamp of when items were last modified.
    :param items: A list of :class:`Item` information.
    """

    model_config = ConfigDict(populate_by_name=True)
    last_updated: Optional[int] = Field(default=None, alias="lastUpdated")
    items: Optional[List[Item]] = Field(default=None)
    rate_limit: Optional[RateLimit] = Field(default=None, exclude=True)


class Item(BaseModel):
    """
    Information about a Skyblock Item

    :param material: Vanilla material used for the item
    :param durability: Meta for the material
    :param skin: Information about a skull heads skin
    :param name: Name of the item
    :param category: Category of the item
    :param tier: The items rarity
    :param npc_sell_price: Sell price of the item to npcs
    :param id: Item ID of the item
    :param salvages: Rewards for salvaging the item
    :param rarity_salvageable:
    :param description: Item description
    :param item_model: Item used for 1.21+
    :param stats: Stats given by the item
    :param unstackable: If the item is stackable
    :param dungeon_item_conversion_cost: The cost to convert the item to a dungeon item
    :param upgrade_costs: A list of upgrade costs for dungeon items
    :param museum_data: Information about the items museum data
    :param requirements: Requirements to use the item
    :param color: Color of leather armor
    :param soulbound: Type of soulbound the item is
    :param has_uuid:
    :param can_auction: If the item can be auctioned
    :param gemstone_slots: A list of gemstone slots on the item
    :param glowing: Whether the item has glint
    :param can_trade: Whether the item can be traded
    :param can_place: Whether the item can be placed
    :param museum: If the item can be put into the special category of museum
    :param generator: The type of minion
    :param generator_tier: The tier of the minion
    :param furniture: The type of furniture
    :param item_specific: Specific information about the item
    :param editioned: Used for the Villager Doll to prevent editions
    :param gear_score: The gear score of the item
    :param dungeon_item: Whether the item is a dungeon item
    :param catacombs_requirement: Requirements to use the item in dungeons
    :param can_have_booster: Whether the item can have a foraging booster
    :param hide_from_api: Whether the item is hidden from the api
    :param can_recombobulate: Whether the item can be recombobulated
    :param salvageable_from_recipe: TODO unknown
    :param motes_sell_price: Motes sell price of the item
    :param double_tap_to_drop: Whether the item requires double tap to drop
    :param enchantments: Enchantments on the item
    :param rift_transferrable: Whether the item is rift transferrable
    :param origin: Used for Rift items that are obtained in the Rift
    :param hide_from_viewrecipe_command: Whether the item is hidden from the viewrecipe command
    :param force_wipe_recomb: Whether the item force wipes recombobulator
    :param ability_damage_scaling: Ability damage scaling of the item
    :param tiered_stats: Tiered stats for dungeon items
    :param crystal: Type of crystal
    :param can_burn_in_furnace: Whether the item can be burned in a furnace
    :param salvage: Salvage information for the item
    :param serializable: TODO unknown
    :param can_have_attributes: TODO unknown
    :param can_interact: Whether the item can interact with things
    :param can_interact_right_click: Whether the item can interact using right click with things
    :param private_island: Type of island spawned
    :param can_have_power_scroll: Whether the item can have a power scroll
    :param can_interact_entity: Whether the item can interact with an entity
    :param mining_fortune: Used for titanium belt? TODO why
    :param rarity: Used for Fishy Penguin Minion Skin and Polar Bear Minion Skin for Rarity
    :param sword_type: Type of sword
    :param is_upgradeable_without_soulbinding: TODO unknown
    :param recipes: Recipes for the item
    :param cannot_reforge: Whether the item cannot be reforged
    :param lose_motes_value_on_transfer: Whether the item loses motes value on transfer
    :param prestige: Upgrades for crimson isle armor
    """

    model_config = ConfigDict(populate_by_name=True)
    material: Optional[str] = Field(default=None)
    durability: Optional[int] = Field(default=None)
    skin: Optional[Skin] = None
    name: Optional[str] = None
    category: Optional[str] = None
    tier: Optional[str] = None
    npc_sell_price: Optional[int] = Field(default=None, alias="npc_sell_price")
    id: Optional[str] = None
    salvages: Optional[List[Salvage]] = Field(default=None)
    rarity_salvageable: Optional[bool] = Field(default=None, alias="rarity_salvageable")
    description: Optional[str] = None
    item_model: Optional[str] = Field(default=None, alias="item_model")
    stats: Optional[Dict[StatType, int]] = Field(default=None)
    unstackable: Optional[bool] = None
    dungeon_item_conversion_cost: Optional[DungeonItemConversionCost] = Field(
        default=None, alias="dungeon_item_conversion_cost"
    )
    upgrade_costs: Optional[List[List[UpgradeCost]]] = Field(default=None, alias="upgrade_costs")
    museum_data: Optional[MuseumData] = Field(default=None, alias="museum_data")
    requirements: Optional[List[Requirement]] = Field(default=None)
    color: Optional[str] = Field(default=None)
    soulbound: Optional[str] = Field(default=None)
    has_uuid: Optional[bool] = Field(default=None, alias="has_uuid")
    can_auction: Optional[bool] = Field(default=None, alias="can_auction")
    gemstone_slots: Optional[List[GemstoneSlot]] = Field(default=None, alias="gemstone_slots")
    glowing: Optional[bool] = None
    can_trade: Optional[bool] = Field(default=None, alias="can_trade")
    can_place: Optional[bool] = Field(default=None, alias="can_place")
    museum: Optional[bool] = None
    generator: Optional[str] = Field(default=None)
    generator_tier: Optional[int] = Field(default=None, alias="generator_tier")
    furniture: Optional[str] = Field(default=None)
    item_specific: Optional[Dict[str, Any]] = Field(default=None, alias="item_specific")
    editioned: Optional[bool] = None
    gear_score: Optional[int] = Field(default=None, alias="gear_score")
    dungeon_item: Optional[bool] = Field(default=None, alias="dungeon_item")
    catacombs_requirement: Optional[CatacombsRequirement] = Field(
        default=None, alias="catacombs_requirements"
    )
    can_have_booster: Optional[bool] = Field(default=None, alias="can_have_booster")
    hide_from_api: Optional[bool] = Field(default=None, alias="hide_from_api")
    can_recombobulate: Optional[bool] = Field(default=None, alias="can_recombobulate")
    salvageable_from_recipe: Optional[bool] = Field(default=None, alias="salvageable_from_recipe")
    motes_sell_price: Optional[int] = Field(default=None, alias="motes_sell_price")
    double_tap_to_drop: Optional[bool] = Field(default=None, alias="double_tap_to_drop")
    enchantments: Optional[Dict[str, int]] = Field(default=None)
    rift_transferrable: Optional[bool] = Field(default=None, alias="rift_transferrable")
    origin: Optional[str] = Field(default=None)
    hide_from_viewrecipe_command: Optional[bool] = Field(
        default=None, alias="hide_from_viewrecipe_command"
    )
    force_wipe_recomb: Optional[bool] = Field(default=None, alias="force_wipe_recomb")
    ability_damage_scaling: Optional[int] = Field(default=None, alias="ability_damage_scaling")
    tiered_stats: Optional[Dict[StatType, List[int]]] = Field(default=None, alias="tiered_stats")
    crystal: Optional[str] = Field(default=None)
    can_burn_in_furnace: Optional[bool] = Field(default=None, alias="can_burn_in_furnace")
    salvage: Optional[SalvageData] = None
    serializable: Optional[bool] = None
    can_have_attributes: Optional[bool] = Field(default=None, alias="can_have_attributes")
    can_interact: Optional[bool] = Field(default=None, alias="can_interact")
    can_interact_right_click: Optional[bool] = Field(default=None, alias="can_interact_right_click")
    private_island: Optional[str] = Field(default=None, alias="private_island")
    can_have_power_scroll: Optional[bool] = Field(default=None, alias="can_have_power_scroll")
    can_interact_entity: Optional[bool] = Field(default=None, alias="can_interact_entity")
    mining_fortune: Optional[int] = Field(default=None, alias="MINING_FORTUNE")
    rarity: Optional[str] = None
    sword_type: Optional[str] = Field(default=None, alias="sword_type")
    is_upgradeable_without_soulbinding: Optional[bool] = Field(
        default=None, alias="is_upgradeable_without_soulbinding"
    )
    recipes: Optional[List[Recipe]] = Field(default=None)
    cannot_reforge: Optional[bool] = Field(default=None, alias="cannot_reforge")
    lose_motes_value_on_transfer: Optional[bool] = Field(
        default=None, alias="lose_motes_value_on_transfer"
    )
    prestige: Optional[Prestige] = None


class Skin(BaseModel):
    """
    Information about a player head

    :param value: Base64 encoded JSON string for skin information
    :param signature: Mojang internal proof
    """

    model_config = ConfigDict(populate_by_name=True)
    value: Optional[str] = None
    signature: Optional[str] = None


class Salvage(BaseModel):
    """
    Rewards for salvaging the item

    :param reward_type: Type of reward, always `ESSENCE`.
    :param essence_type: Type of essence given.
    :param amount: Amount of essence given
    """

    model_config = ConfigDict(populate_by_name=True)
    reward_type: Optional[str] = Field(default=None, alias="type")
    essence_type: Optional[EssenceType] = Field(default=None, alias="essence_type")
    amount: Optional[int] = None


class SalvageData(BaseModel):
    """
    Unknown. Used one time for an item with ID "NETHERITE_HELMET"
    """

    model_config = ConfigDict(populate_by_name=True)
    item_id: Optional[str] = Field(default=None, alias="item_id")
    amount: Optional[int] = Field(default=None)


class DungeonItemConversionCost(BaseModel):
    """
    Information about to cost to convert an item to a dungeon item

    :param essence_type: The type of essence needed.
    :param amount: The amount of essence needed.
    """

    model_config = ConfigDict(populate_by_name=True)
    essence_type: Optional[EssenceType] = Field(default=None, alias="essence_type")
    amount: Optional[int] = Field(default=None)


class UpgradeCost(BaseModel):
    """
    Information about an upgrade for a dungeon item

    :param type: Upgrade type (ITEM or ESSENCE)
    :param essence_type: Type of essence needed.
    :param amount: Amount of essence or item needed
    :param item_id: Item ID needed.
    """

    model_config = ConfigDict(populate_by_name=True)
    type: Optional[str] = Field(default=None)
    essence_type: Optional[EssenceType] = Field(default=None, alias="essence_type")
    amount: Optional[int] = Field(default=None)
    item_id: Optional[str] = Field(default=None, alias="item_id")


class MuseumData(BaseModel):
    """
    Information about an items museum donation

    :param category: The museum category the item belongs to
    :param parent: Parent items TODO better explanation
    :param armor_set_donation_xp: Amount of XP given for the armor set
    :param game_stage: The level gamestage for the item
    :param donation_xp: Amount of XP given for the item
    """

    model_config = ConfigDict(populate_by_name=True)
    category: Optional[str] = Field(default=None)
    parent: Optional[Dict[MuseumItem, MuseumItem]] = Field(default=None)
    armor_set_donation_xp: Optional[Dict[MuseumItem, int]] = Field(
        default=None, alias="armor_set_donation_xp"
    )
    game_stage: Optional[str] = Field(default=None, alias="game_stage")
    donation_xp: Optional[int] = Field(default=None, alias="donation_xp")


class CatacombsRequirement(BaseModel):
    """
    Information about the catacombs requirements for an item

    :param type: Type of requirement (DUNGEON_SKILL)
    :param dungeon_type: Always CATACOMBS
    :param level: Level for the requirement needed
    """

    model_config = ConfigDict(populate_by_name=True)
    type: Optional[str] = Field(default=None)
    dungeon_type: Optional[str] = Field(default=None, alias="dungeon_type")
    level: Optional[int] = Field(default=None)


class Requirement(BaseModel):
    """
    Information about item requirements

    :param type: Type of requirement
    :param skill: Which skill is required
    :param slayer_boss_type: Which slayer is required
    :param level: Level of slayer/skill/dungeons required
    :param dungeon_type: Which dungeons are required
    """

    model_config = ConfigDict(populate_by_name=True)
    type: Optional[str] = Field(default=None)
    skill: Optional[SkillType] = Field(default=None)
    slayer_boss_type: Optional[str] = Field(default=None, alias="slayer_boss_type")
    level: Optional[int] = Field(default=None)
    dungeon_type: Optional[str] = Field(default=None, alias="dungeon_type")


class GemstoneSlot(BaseModel):
    """
    Information about the items gemstone slots

    :param slot_type: Which gemstone is allowed in the slot
    :param costs: The costs to unlock the gemstone slot
    :param requirements: Requirements for gemstones on farming tools
    """

    model_config = ConfigDict(populate_by_name=True)
    slot_type: Optional[str] = Field(default=None, alias="slot_type")
    costs: Optional[List[GemstoneCost]] = Field(default=None)
    requirements: Optional[List[GemstoneRequirement]] = Field(default=None)


class GemstoneCost(BaseModel):
    """
    Information about the cost for a gemstone slot

    :param type: Type of cost (ITEM, COINS)
    :param item_id: Item ID of the item required
    :param amount: Amount of the item/essence required
    :param coins: Amount of coins required
    :param essence_type: Type of essence required
    """

    model_config = ConfigDict(populate_by_name=True)
    type: Optional[str] = Field(default=None)
    item_id: Optional[str] = Field(default=None, alias="item_id")
    amount: Optional[int] = Field(default=None)
    coins: Optional[int] = Field(default=None)
    essence_type: Optional[EssenceType] = Field(default=None, alias="essence_type")


class GemstoneRequirement(BaseModel):
    """
    Information about requirements to unlock a gemstone slot

    :param type: Type of requirement (always ITEM_DATA)
    :param data_key: TODO
    :param value: TODO
    :param operator: TODO
    """

    model_config = ConfigDict(populate_by_name=True)
    type: Optional[str] = Field(default=None)
    data_key: Optional[str] = Field(default=None, alias="data_key")
    value: Optional[str] = Field(default=None)
    operator: Optional[str] = Field(default=None)


class Recipe(BaseModel):
    """
    Information about a recipe to create the item

    :param output: Item output by the recipe (usually the same as the item id)
    :param ingredient_symbols: Ingredient symbols used for the matrix
    :param matrix: Ingredient matrix used to determine cost
    """

    model_config = ConfigDict(populate_by_name=True)
    output: Optional[RecipeOutput] = Field(default=None)
    ingredient_symbols: Optional[Dict[str, str]] = Field(default=None, alias="ingredient_symbols")
    matrix: Optional[List[Optional[str]]] = Field(default=None)


class RecipeOutput(BaseModel):
    """
    Information about the item output

    :param item_id: Item ID of the created item
    """

    model_config = ConfigDict(populate_by_name=True)
    item_id: Optional[str] = Field(default=None, alias="item_id")


class Prestige(BaseModel):
    """
    Information about Crimson Isle set upgrades

    :param item_id: Item ID of the created item
    :param costs: Costs for the upgrades
    """

    model_config = ConfigDict(populate_by_name=True)
    item_id: Optional[str] = Field(default=None, alias="item_id")
    costs: Optional[List[GemstoneCost]] = Field(default=None)
