from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit
from hywrapper.models.skyblock.profile.crimson_isle import CrimsonIslePlayerData
from hywrapper.models.skyblock.profile.dungeons import Dungeons
from hywrapper.models.skyblock.profile.event import Event
from hywrapper.models.skyblock.profile.foraging import Foraging
from hywrapper.models.skyblock.profile.jacobs_content import JacobsContent
from hywrapper.models.skyblock.profile.pets_data import PetsData
from hywrapper.models.skyblock.profile.player_data import PlayerData
from hywrapper.models.skyblock.profile.rift import Rift


class ProfileResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    profile: Optional[Profile] = None
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class Profile(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    profileId: str = Field(default="", alias="profile_id")
    communityUpgrades: Optional[CommunityUpgrades] = Field(default=None, alias="community_upgrades")
    members: Dict[str, MemberData] = Field(default_factory=dict)
    banking: Optional[Banking] = None


class MemberData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    rift: Optional[Rift] = None
    playerData: Optional[PlayerData] = Field(default=None, alias="player_data")
    glacitePlayerData: Optional[GlacitePlayerData] = Field(
        default=None, alias="glacite_player_data"
    )
    profile: Optional[ProfileData] = None
    event: Optional[Event] = None
    gardenPlayerData: Optional[GardenPlayerData] = Field(default=None, alias="garden_player_data")
    # TODO skill_tree
    petsData: Optional[PetsData] = Field(default=None, alias="pets_data")
    accessoryBagStorage: Optional[AccessoryBagStorage] = Field(
        default=None, alias="accessory_bag_storage"
    )
    leveling: Optional[Leveling] = None
    itemData: Optional[ItemData] = Field(default=None, alias="item_data")
    jacobsContent: Optional[JacobsContent] = Field(default=None, alias="jacobs_contest")
    currencies: Optional[Currencies] = None
    foraging: Optional[Foraging] = None
    dungeons: Optional[Dungeons] = None
    playerId: str = Field(default="", alias="player_id")
    crimsonIslePlayerData: Optional[CrimsonIslePlayerData] = Field(
        default=None, alias="nether_island_player_data"
    )


class GlacitePlayerData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    # TODO enum
    fossilsDonated: List[str] = Field(default_factory=list, alias="fossils_donated")
    fossilDust: float = Field(default=0.0, alias="fossil_dust")
    # TODO enum
    corpsesLooted: Dict[str, int] = Field(default_factory=dict, alias="corpses_looted")
    mineshaftsEntered: int = Field(default=0, alias="mineshafts_entered")


class ProfileData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    bankAccount: float = Field(default=0.0, alias="bank_account")
    firstJoin: Optional[int] = Field(default=0, alias="first_join")
    personalBankUpgrade: int = Field(default=0, alias="personal_bank_upgrade")
    cookieBuffActive: Optional[bool] = Field(default=None, alias="cookie_buff_active")


class GardenPlayerData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    copper: int = Field(default=0)
    larvaConsumed: int = Field(default=0, alias="larva_consumed")
    # TODO enum
    analyzedGreenhouseCrops: List[str] = Field(
        default_factory=list, alias="analyzed_greenhouse_crops"
    )
    # TODO enum
    discoveredGreenhouseCrops: List[str] = Field(
        default_factory=list, alias="discovered_greenhouse_crops"
    )


class AccessoryBagStorage(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    tuning: Dict[str, TuningSlot] = Field(default_factory=dict)
    # TODO ENUM
    selectedPower: str = Field(default="", alias="selected_power")
    bagUpgradesPurchased: int = Field(default=0, alias="bag_upgrades_purchased")
    # TODO enum
    unlockedPowers: List[str] = Field(default_factory=list, alias="unlocked_powers")
    highestMagicalPower: int = Field(default=0, alias="highest_magical_power")


class TuningSlot(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    health: int = Field(default=0)
    defense: int = Field(default=0)
    walkSpeed: int = Field(default=0, alias="walk_speed")
    strength: int = Field(default=0)
    criticalDamage: int = Field(default=0, alias="critical_damage")
    criticalChance: int = Field(default=0, alias="critical_chance")
    attackSpeed: int = Field(default=0, alias="attack_speed")
    intelligence: int = Field(default=0)


class Leveling(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    experience: int = Field(default=0)
    # TODO enum
    completions: Dict[str, int] = Field(default_factory=dict)
    # TODO enum
    completedTasks: List[str] = Field(default_factory=list, alias="completed_tasks")
    highestPetScore: int = Field(default=0, alias="highest_pet_score")
    miningFiestaOresMined: int = Field(default=0, alias="mining_fiesta_ores_mined")
    migrated: Optional[bool] = None
    migratedCompletionsV2: Optional[bool] = Field(default=None, alias="migrated_completions_2")
    claimedTalisman: Optional[bool] = Field(default=None, alias="claimed_talisman")
    # TODO enum
    bopBonus: str = Field(default="", alias="bop_bonus")
    # TODO enum
    emblemUnlocks: List[str] = Field(default_factory=list, alias="emblem_unlocks")
    categoryExpanded: Optional[bool] = Field(default=None, alias="category_expanded")
    fishingFestivalSharksKilled: int = Field(default=0, alias="fishing_festival_sharks_killed")
    # TODO enum
    taskSort: str = Field(default="", alias="task_sort")
    # TODO enum
    lastViewedTasks: List[str] = Field(default_factory=list, alias="last_viewed_tasks")
    # TODO enum
    selectedSymbol: str = Field(default="", alias="selected_symbol")


class ItemData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    soulflow: int = Field(default=0)
    favoriteArrow: str = Field(default="", alias="favorite_arrow")


class Currencies(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    coinPurse: float = Field(default=0.0, alias="coin_purse")
    motesPurse: float = Field(default=0.0, alias="motes_purse")
    essence: Dict[str, EssenceInfo] = Field(default_factory=dict)


class EssenceInfo(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    current: int = Field(default=0)


class CommunityUpgrades(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    currentlyUpgrading: str = Field(default="", alias="currently_upgrading")
    upgradeStates: List[UpgradeState] = Field(default_factory=list, alias="upgrade_states")


class UpgradeState(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    upgrade: str = Field(default="")
    tier: int = Field(default=1)
    startedMs: int = Field(default=0, alias="started_ms")
    startedBy: str = Field(default="", alias="started_by")
    claimedBy: str = Field(default="", alias="claimed_by")


class Banking(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    balance: float = Field(default=0.0)
    transactions: List[Transaction] = Field(default_factory=list)


class Transaction(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    amount: float = Field(default=0.0)
    timestamp: int = Field(default=0)
    action: str = Field(default="")
    initiatorName: str = Field(default="", alias="initiator_name")
