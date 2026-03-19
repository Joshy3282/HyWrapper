from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit
from hywrapper.models.skyblock.profile.event import Event
from hywrapper.models.skyblock.profile.pets_data import PetsData
from hywrapper.models.skyblock.profile.player_data import PlayerData
from hywrapper.models.skyblock.profile.rift import Rift


class ProfileResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    cause: Optional[str] = None
    profile: Optional[Profile] = None
    rateLimit: Optional[RateLimit] = None


class Profile(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    profileId: str = Field(default="")
    communityUpgrades: Optional[CommunityUpgrades] = None
    members: Dict[str, MemberData] = Field(default={})
    banking: Optional[Banking] = None


class MemberData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    rift: Optional[Rift] = None
    playerData: Optional[PlayerData] = None
    glacitePlayerData: Optional[GlacitePlayerData] = None
    profile: Optional[ProfileData] = None
    event: Optional[Event] = None
    gardenPlayerData: Optional[GardenPlayerData] = None
    petsData: Optional[PetsData] = None
    accessoryBagStorage: Optional[AccessoryBagStorage] = None
    leveling: Optional[Leveling] = None
    itemData: Optional[ItemData] = None


class GlacitePlayerData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    fossilsDonated: List[str] = Field(default=[])
    fossilDust: float = Field(default=0.0)
    corpsesLooted: Dict[str, int] = Field(default={})
    mineshaftsEntered: int = Field(default=0)


class ProfileData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    bankAccount: float = Field(default=0.0)
    firstJoin: Optional[int] = Field(default=0)
    personalBankUpgrade: int = Field(default=0)
    cookieBuffActive: Optional[bool] = None


class GardenPlayerData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    copper: int = Field(default=0)
    larvaConsumed: int = Field(default=0)
    analyzedGreenhouseCrops: List[str] = Field(default=[])
    discoveredGreenhouseCrops: List[str] = Field(default=[])


class AccessoryBagStorage(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    tuning: Dict[str, TuningSlot] = Field(default={})
    selectedPower: str = Field(default="")
    bagUpgradesPurchased: int = Field(default=0)
    unlockedPowers: List[str] = Field(default=[])
    highestMagicalPower: int = Field(default=0)


class TuningSlot(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    health: int = Field(default=0)
    defense: int = Field(default=0)
    walkSpeed: int = Field(default=0)
    strength: int = Field(default=0)
    criticalDamage: int = Field(default=0)
    criticalChance: int = Field(default=0)
    attackSpeed: int = Field(default=0)
    intelligence: int = Field(default=0)


class Leveling(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    experience: int = Field(default=0)
    completions: Dict[str, int] = Field(default={})
    completedTasks: List[str] = Field(default=[])
    highestPetScore: int = Field(default=0)
    miningFiestaOresMined: int = Field(default=0)
    migrated: Optional[bool] = None
    migratedCompletionsV2: Optional[bool] = None
    claimedTalisman: Optional[bool] = None
    bopBonus: str = Field(default="")
    emblemUnlocks: List[str] = Field(default=[])
    categoryExpanded: Optional[bool] = None
    fishingFestivalSharksKilled: int = Field(default=0)
    taskSort: str = Field(default="")
    lastViewedTasks: List[str] = Field(default=[])
    selectedSymbol: str = Field(default="")


class ItemData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    soulflow: int = Field(default=0)
    favoriteArrow: str = Field(default="")


class CommunityUpgrades(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    currentlyUpgrading: str = Field(default="")
    upgradeStates: List[UpgradeState] = Field(default=[])


class UpgradeState(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    upgrade: str = Field(default="")
    tier: int = Field(default=1)
    startedMs: int = Field(default=0)
    startedBy: str = Field(default="")
    claimedBy: str = Field(default="")


class Banking(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    balance: float = Field(default=0.0)
    transactions: List[Transaction] = Field(default=[])


class Transaction(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    amount: float = Field(default=0.0)
    timestamp: int = Field(default=0)
    action: str = Field(default="")
    initiatorName: str = Field(default="")
