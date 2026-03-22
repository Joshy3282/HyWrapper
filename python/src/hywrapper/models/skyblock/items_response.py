from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.data.skyblock.museum_item import MuseumItem
from hywrapper.data.skyblock.stat_type import StatType
from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class ItemsResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    last_updated: Optional[int] = Field(default=None, alias="lastUpdated")
    items: Optional[List[Item]] = Field(default=None)
    rate_limit: Optional[RateLimit] = Field(default=None, exclude=True)


class Item(BaseModel):
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
    model_config = ConfigDict(populate_by_name=True)
    value: Optional[str] = None
    signature: Optional[str] = None


class Salvage(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: Optional[str] = None
    essence_type: Optional[str] = Field(default=None, alias="essence_type")
    amount: Optional[int] = None


class SalvageData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    item_id: Optional[str] = Field(default=None, alias="item_id")
    amount: Optional[int] = Field(default=None)


class DungeonItemConversionCost(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    essence_type: Optional[str] = Field(default=None, alias="essence_type")
    amount: Optional[int] = Field(default=None)


class UpgradeCost(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: Optional[str] = Field(default=None)
    essence_type: Optional[str] = Field(default=None, alias="essence_type")
    amount: Optional[int] = Field(default=None)
    item_id: Optional[str] = Field(default=None, alias="item_id")


class MuseumData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    category: Optional[str] = Field(default=None)
    parent: Optional[Dict[MuseumItem, MuseumItem]] = Field(default=None)
    armor_set_donation_xp: Optional[Dict[MuseumItem, int]] = Field(
        default=None, alias="armor_set_donation_xp"
    )
    game_stage: Optional[str] = Field(default=None, alias="game_stage")


class CatacombsRequirement(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: Optional[str] = Field(default=None)
    dungeon_type: Optional[str] = Field(default=None, alias="dungeon_type")
    level: Optional[int] = Field(default=None)


class Requirement(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: Optional[str] = Field(default=None)
    skill: Optional[str] = Field(default=None)
    slayer_boss_type: Optional[str] = Field(default=None, alias="slayer_boss_type")
    level: Optional[int] = Field(default=None)
    dungeon_type: Optional[str] = Field(default=None, alias="dungeon_type")


class GemstoneSlot(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    slot_type: Optional[str] = Field(default=None, alias="slot_type")
    costs: Optional[List[GemstoneCost]] = Field(default=None)
    requirements: Optional[List[GemstoneRequirement]] = Field(default=None)


class GemstoneCost(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: Optional[str] = Field(default=None)
    item_id: Optional[str] = Field(default=None, alias="item_id")
    amount: Optional[int] = Field(default=None)
    coins: Optional[int] = Field(default=None)
    essence_type: Optional[str] = Field(default=None, alias="essence_type")


class GemstoneRequirement(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: Optional[str] = Field(default=None)
    data_key: Optional[str] = Field(default=None, alias="data_key")
    value: Optional[str] = Field(default=None)
    operator: Optional[str] = Field(default=None)


class Recipe(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    output: Optional[RecipeOutput] = Field(default=None)
    ingredient_symbols: Optional[Dict[str, str]] = Field(default=None, alias="ingredient_symbols")
    matrix: Optional[List[Optional[str]]] = Field(default=None)


class RecipeOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    item_id: Optional[str] = Field(default=None, alias="item_id")


class Prestige(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    item_id: Optional[str] = Field(default=None, alias="item_id")
    costs: Optional[List[GemstoneCost]] = Field(default=None)
