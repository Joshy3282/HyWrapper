from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.data.skyblock.stat_type import StatType
from hywrapper.models.rate_limit import RateLimit
from hywrapper.models.skyblock.museum_response import MuseumItem


class ItemsResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    cause: Optional[str] = None
    lastUpdated: Optional[int] = Field(default=0)
    items: List[Item] = Field(default=[])
    rateLimit: Optional[RateLimit] = None


class Item(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    material: str = Field(default="")
    durability: int = Field(default=0)
    skin: Optional[Skin] = None
    name: Optional[str] = None
    category: Optional[str] = None
    tier: Optional[str] = None
    npcSellPrice: Optional[int] = None
    id: Optional[str] = None
    salvages: List[Salvage] = Field(default=[])
    raritySalvageable: Optional[bool] = None
    description: Optional[str] = None
    itemModel: Optional[str] = None
    stats: Dict[StatType, int] = Field(default={})
    unstackable: Optional[bool] = None
    dungeonItemConversionCost: Optional[DungeonItemConversionCost] = None
    upgradeCosts: List[List[UpgradeCost]] = Field(default=[])
    museumData: Optional[MuseumData] = None
    color: str = Field(default="")
    soulbound: str = Field(default="")
    hasUuid: Optional[bool] = None
    canAuction: Optional[bool] = None
    glowing: Optional[bool] = None
    canTrade: Optional[bool] = None
    canPlace: Optional[bool] = None
    museum: Optional[bool] = None
    generator: str = Field(default="")
    generatorTier: int = Field(default=0)
    furniture: str = Field(default="")
    editioned: Optional[bool] = None
    gearScore: int = Field(default=0)
    dungeonItem: Optional[bool] = None
    catacombsRequirement: Optional[CatacombsRequirement] = None
    canHaveBooster: Optional[bool] = None
    hideFromApi: Optional[bool] = None
    canRecombobulate: Optional[bool] = None
    salvageableFromRecipe: Optional[bool] = None
    motesSellPrice: Optional[int] = Field(default=0)
    doubleTapToDrop: Optional[bool] = None
    riftTransferrable: Optional[bool] = None
    origin: str = Field(default="")
    hideFromViewrecipeCommand: Optional[bool] = None
    forceWipeRecomb: Optional[bool] = None
    abilityDamageScaling: int = Field(default=0)
    crystal: str = Field(default="")
    canBurnInFurnace: Optional[bool] = None
    serializable: Optional[bool] = None
    canHaveAttributes: Optional[bool] = None
    canInteract: Optional[bool] = None
    canInteractRightClick: Optional[bool] = None
    privateIsland: Optional[str] = None
    canHavePowerScroll: Optional[bool] = None
    canInteractEntity: Optional[bool] = None
    miningFortune: Optional[int] = None
    rarity: Optional[str] = None
    swordType: Optional[str] = None
    isUpgradeableWithoutSoulbinding: Optional[bool] = None
    cannotReforge: Optional[bool] = None
    loseMotesValueOnTransfer: Optional[bool] = None


class Skin(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    value: Optional[str] = None
    signature: Optional[str] = None


class Salvage(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: Optional[str] = None
    essenceType: Optional[str] = None
    amount: Optional[int] = None


class DungeonItemConversionCost(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    essenceType: str = Field(default="")
    amount: int = Field(default=0)


class UpgradeCost(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: str = Field(default="")
    essenceType: str = Field(default="")
    amount: int = Field(default=0)


class MuseumData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    category: str = Field(default="")
    parent: Dict[MuseumItem, MuseumItem] = Field(default={})
    armorSetDonationXp: Dict[MuseumItem, int] = Field(default={})
    gameStage: str = Field(default="")


class CatacombsRequirement(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: str = Field(default="")
    dungeonType: str = Field(default="")
    level: int = Field(default=0)
