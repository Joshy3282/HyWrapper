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
    profileId: Optional[str] = Field(default=None, alias="profile_id")
    communityUpgrades: Optional[CommunityUpgrades] = Field(default=None, alias="community_upgrades")
    members: Optional[Dict[str, MemberData]] = Field(default=None)
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
    playerId: Optional[str] = Field(default=None, alias="player_id")
    crimsonIslePlayerData: Optional[CrimsonIslePlayerData] = Field(
        default=None, alias="nether_island_player_data"
    )


class GlacitePlayerData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    # TODO enum
    fossilsDonated: Optional[List[str]] = Field(default=None, alias="fossils_donated")
    fossilDust: Optional[float] = Field(default=None, alias="fossil_dust")
    # TODO enum
    corpsesLooted: Optional[Dict[str, int]] = Field(default=None, alias="corpses_looted")
    mineshaftsEntered: Optional[int] = Field(default=None, alias="mineshafts_entered")


class ProfileData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    bankAccount: Optional[float] = Field(default=None, alias="bank_account")
    firstJoin: Optional[int] = Field(default=None, alias="first_join")
    personalBankUpgrade: Optional[int] = Field(default=None, alias="personal_bank_upgrade")
    cookieBuffActive: Optional[bool] = Field(default=None, alias="cookie_buff_active")


class GardenPlayerData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    copper: Optional[int] = Field(default=None)
    larvaConsumed: Optional[int] = Field(default=None, alias="larva_consumed")
    # TODO enum
    analyzedGreenhouseCrops: Optional[List[str]] = Field(
        default=None, alias="analyzed_greenhouse_crops"
    )
    # TODO enum
    discoveredGreenhouseCrops: Optional[List[str]] = Field(
        default=None, alias="discovered_greenhouse_crops"
    )


class AccessoryBagStorage(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    tuning: Optional[Dict[str, TuningSlot]] = Field(default=None)
    # TODO ENUM
    selectedPower: Optional[str] = Field(default=None, alias="selected_power")
    bagUpgradesPurchased: Optional[int] = Field(default=None, alias="bag_upgrades_purchased")
    # TODO enum
    unlockedPowers: Optional[List[str]] = Field(default=None, alias="unlocked_powers")
    highestMagicalPower: Optional[int] = Field(default=None, alias="highest_magical_power")


class TuningSlot(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    health: Optional[int] = Field(default=None)
    defense: Optional[int] = Field(default=None)
    walkSpeed: Optional[int] = Field(default=None, alias="walk_speed")
    strength: Optional[int] = Field(default=None)
    criticalDamage: Optional[int] = Field(default=None, alias="critical_damage")
    criticalChance: Optional[int] = Field(default=None, alias="critical_chance")
    attackSpeed: Optional[int] = Field(default=None, alias="attack_speed")
    intelligence: Optional[int] = Field(default=None)


class Leveling(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    experience: Optional[int] = Field(default=None)
    # TODO enum
    completions: Optional[Dict[str, int]] = Field(default=None)
    # TODO enum
    completedTasks: Optional[List[str]] = Field(default=None, alias="completed_tasks")
    highestPetScore: Optional[int] = Field(default=None, alias="highest_pet_score")
    miningFiestaOresMined: Optional[int] = Field(default=None, alias="mining_fiesta_ores_mined")
    migrated: Optional[bool] = None
    migratedCompletionsV2: Optional[bool] = Field(default=None, alias="migrated_completions_2")
    claimedTalisman: Optional[bool] = Field(default=None, alias="claimed_talisman")
    # TODO enum
    bopBonus: Optional[str] = Field(default=None, alias="bop_bonus")
    # TODO enum
    emblemUnlocks: Optional[List[str]] = Field(default=None, alias="emblem_unlocks")
    categoryExpanded: Optional[bool] = Field(default=None, alias="category_expanded")
    fishingFestivalSharksKilled: Optional[int] = Field(
        default=None, alias="fishing_festival_sharks_killed"
    )
    # TODO enum
    taskSort: Optional[str] = Field(default=None, alias="task_sort")
    # TODO enum
    lastViewedTasks: Optional[List[str]] = Field(default=None, alias="last_viewed_tasks")
    # TODO enum
    selectedSymbol: Optional[str] = Field(default=None, alias="selected_symbol")


class ItemData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    soulflow: Optional[int] = Field(default=None)
    favoriteArrow: Optional[str] = Field(default=None, alias="favorite_arrow")


class Currencies(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    coinPurse: Optional[float] = Field(default=None, alias="coin_purse")
    motesPurse: Optional[float] = Field(default=None, alias="motes_purse")
    essence: Optional[Dict[str, EssenceInfo]] = Field(default=None)


class EssenceInfo(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    current: Optional[int] = Field(default=None)


class CommunityUpgrades(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    currentlyUpgrading: Optional[str] = Field(default=None, alias="currently_upgrading")
    upgradeStates: Optional[List[UpgradeState]] = Field(default=None, alias="upgrade_states")


class UpgradeState(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    upgrade: Optional[str] = Field(default=None)
    tier: Optional[int] = Field(default=None)
    startedMs: Optional[int] = Field(default=None, alias="started_ms")
    startedBy: Optional[str] = Field(default=None, alias="started_by")
    claimedBy: Optional[str] = Field(default=None, alias="claimed_by")


class Banking(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    balance: Optional[float] = Field(default=None)
    transactions: Optional[List[Transaction]] = Field(default=None)


class Transaction(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    amount: Optional[float] = Field(default=None)
    timestamp: Optional[int] = Field(default=None)
    action: Optional[str] = Field(default=None)
    initiatorName: Optional[str] = Field(default=None, alias="initiator_name")
