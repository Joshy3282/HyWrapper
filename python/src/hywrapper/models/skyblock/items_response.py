from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.data.skyblock.museum_item import MuseumItem
from hywrapper.data.skyblock.stat_type import StatType
from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class ItemsResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    lastUpdated: Optional[int] = Field(default=None)
    items: Optional[List[Item]] = Field(default=None)
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class Item(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    material: Optional[str] = Field(default=None)
    durability: Optional[int] = Field(default=None)
    skin: Optional[Skin] = None
    name: Optional[str] = None
    category: Optional[str] = None
    tier: Optional[str] = None
    npcSellPrice: Optional[int] = Field(default=None, alias="npc_sell_price")
    id: Optional[str] = None
    salvages: Optional[List[Salvage]] = Field(default=None)
    raritySalvageable: Optional[bool] = Field(default=None, alias="rarity_salvageable")
    description: Optional[str] = None
    itemModel: Optional[str] = Field(default=None, alias="item_model")
    stats: Optional[Dict[StatType, int]] = Field(default=None)
    unstackable: Optional[bool] = None
    dungeonItemConversionCost: Optional[DungeonItemConversionCost] = Field(
        default=None, alias="dungeon_item_conversion_cost"
    )
    upgradeCosts: Optional[List[List[UpgradeCost]]] = Field(default=None, alias="upgrade_costs")
    museumData: Optional[MuseumData] = Field(default=None, alias="museum_data")
    color: Optional[str] = Field(default=None)
    soulbound: Optional[str] = Field(default=None)
    hasUuid: Optional[bool] = Field(default=None, alias="has_uuid")
    canAuction: Optional[bool] = Field(default=None, alias="can_auction")
    glowing: Optional[bool] = None
    canTrade: Optional[bool] = Field(default=None, alias="can_trade")
    canPlace: Optional[bool] = Field(default=None, alias="can_place")
    museum: Optional[bool] = None
    generator: Optional[str] = Field(default=None)
    generatorTier: Optional[int] = Field(default=None, alias="generator_tier")
    furniture: Optional[str] = Field(default=None)
    editioned: Optional[bool] = None
    gearScore: Optional[int] = Field(default=None, alias="gear_score")
    dungeonItem: Optional[bool] = Field(default=None, alias="dungeon_item")
    catacombsRequirement: Optional[CatacombsRequirement] = Field(
        default=None, alias="catacombs_requirements"
    )
    canHaveBooster: Optional[bool] = Field(default=None, alias="can_have_booster")
    hideFromApi: Optional[bool] = Field(default=None, alias="hide_from_api")
    canRecombobulate: Optional[bool] = Field(default=None, alias="can_recombobulate")
    salvageableFromRecipe: Optional[bool] = Field(default=None, alias="salvageable_from_recipe")
    motesSellPrice: Optional[int] = Field(default=None, alias="motes_sell_price")
    doubleTapToDrop: Optional[bool] = Field(default=None, alias="double_tap_to_drop")
    riftTransferrable: Optional[bool] = Field(default=None, alias="rift_transferrable")
    origin: Optional[str] = Field(default=None)
    hideFromViewrecipeCommand: Optional[bool] = Field(
        default=None, alias="hide_from_viewrecipe_command"
    )
    forceWipeRecomb: Optional[bool] = Field(default=None, alias="force_wipe_recomb")
    abilityDamageScaling: Optional[int] = Field(default=None, alias="ability_damage_scaling")
    crystal: Optional[str] = Field(default=None)
    canBurnInFurnace: Optional[bool] = Field(default=None, alias="can_burn_in_furnace")
    serializable: Optional[bool] = None
    canHaveAttributes: Optional[bool] = Field(default=None, alias="can_have_attributes")
    canInteract: Optional[bool] = Field(default=None, alias="can_interact")
    canInteractRightClick: Optional[bool] = Field(default=None, alias="can_interact_right_click")
    privateIsland: Optional[str] = Field(default=None, alias="private_island")
    canHavePowerScroll: Optional[bool] = Field(default=None, alias="can_have_power_scroll")
    canInteractEntity: Optional[bool] = Field(default=None, alias="can_interact_entity")
    miningFortune: Optional[int] = Field(default=None, alias="MINING_FORTUNE")
    rarity: Optional[str] = None
    swordType: Optional[str] = Field(default=None, alias="sword_type")
    isUpgradeableWithoutSoulbinding: Optional[bool] = Field(
        default=None, alias="is_upgradeable_without_soulbinding"
    )
    cannotReforge: Optional[bool] = Field(default=None, alias="cannot_reforge")
    loseMotesValueOnTransfer: Optional[bool] = Field(
        default=None, alias="lose_motes_value_on_transfer"
    )


class Skin(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    value: Optional[str] = None
    signature: Optional[str] = None


class Salvage(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: Optional[str] = None
    essenceType: Optional[str] = Field(default=None, alias="essence_type")
    amount: Optional[int] = None


class DungeonItemConversionCost(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    essenceType: Optional[str] = Field(default=None, alias="essence_type")
    amount: Optional[int] = Field(default=None)


class UpgradeCost(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: Optional[str] = Field(default=None)
    essenceType: Optional[str] = Field(default=None, alias="essence_type")
    amount: Optional[int] = Field(default=None)


class MuseumData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    category: Optional[str] = Field(default=None)
    parent: Optional[Dict[MuseumItem, MuseumItem]] = Field(default=None)
    armorSetDonationXp: Optional[Dict[MuseumItem, int]] = Field(
        default=None, alias="armor_set_donation_xp"
    )
    gameStage: Optional[str] = Field(default=None, alias="game_stage")


class CatacombsRequirement(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: Optional[str] = Field(default=None)
    dungeonType: Optional[str] = Field(default=None, alias="dungeon_type")
    level: Optional[int] = Field(default=None)
