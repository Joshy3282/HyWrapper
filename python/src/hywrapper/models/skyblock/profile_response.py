from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit
from hywrapper.models.skyblock.profile.bestiary import Bestiary
from hywrapper.models.skyblock.profile.crimson_isle import CrimsonIslePlayerData
from hywrapper.models.skyblock.profile.dungeons import Dungeons
from hywrapper.models.skyblock.profile.event import Event
from hywrapper.models.skyblock.profile.experimentation import Experimentation
from hywrapper.models.skyblock.profile.foraging import Foraging
from hywrapper.models.skyblock.profile.inventory import InventoryObject, PlayerInventory
from hywrapper.models.skyblock.profile.jacobs_content import JacobsContent
from hywrapper.models.skyblock.profile.mining_core import MiningCore
from hywrapper.models.skyblock.profile.pets_data import PetsData
from hywrapper.models.skyblock.profile.player_data import PlayerData
from hywrapper.models.skyblock.profile.player_stats import PlayerStats
from hywrapper.models.skyblock.profile.rift import Rift
from hywrapper.models.skyblock.profile.slayer import Slayer


class ProfileResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    profile: Optional[Profile] = None
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class Profile(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    profile_id: Optional[str] = Field(default=None, alias="profile_id")
    community_upgrades: Optional[CommunityUpgrades] = Field(
        default=None, alias="community_upgrades"
    )
    members: Optional[Dict[str, MemberData]] = Field(default=None)
    banking: Optional[Banking] = None


class MemberData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    rift: Optional[Rift] = None
    player_data: Optional[PlayerData] = Field(default=None, alias="player_data")
    glacite_player_data: Optional[GlacitePlayerData] = Field(
        default=None, alias="glacite_player_data"
    )
    profile: Optional[ProfileData] = None
    event: Optional[Event] = None
    garden_player_data: Optional[GardenPlayerData] = Field(default=None, alias="garden_player_data")
    skill_tree: Optional[SkillTree] = Field(default=None, alias="skill_tree")
    pets_data: Optional[PetsData] = Field(default=None, alias="pets_data")
    accessory_bag_storage: Optional[AccessoryBagStorage] = Field(
        default=None, alias="accessory_bag_storage"
    )
    leveling: Optional[Leveling] = None
    item_data: Optional[ItemData] = Field(default=None, alias="item_data")
    jacobs_content: Optional[JacobsContent] = Field(default=None, alias="jacobs_contest")
    currencies: Optional[Currencies] = None
    foraging: Optional[Foraging] = None
    dungeons: Optional[Dungeons] = None
    player_id: Optional[str] = Field(default=None, alias="player_id")
    crimson_isle_player_data: Optional[CrimsonIslePlayerData] = Field(
        default=None, alias="nether_island_player_data"
    )
    experimentation: Optional[Experimentation] = None
    foraging_core: Optional[ForagingCore] = Field(default=None, alias="foraging_core")
    shards: Optional[Shards] = None
    mining_core: Optional[MiningCore] = Field(default=None, alias="mining_core")
    bestiary: Optional[Bestiary] = None
    quests: Optional[Quests] = None
    player_stats: Optional[PlayerStats] = Field(default=None, alias="player_stats")
    inventory: Optional[PlayerInventory] = None
    winter_player_data: Optional[WinterPlayerData] = Field(default=None, alias="winter_player_data")
    forge: Optional[Forge] = None
    fairy_soul: Optional[FairySoul] = Field(default=None, alias="fairy_soul")
    temples: Optional[Temples] = None
    shared_inventory: Optional[SharedInventory] = Field(default=None, alias="shared_inventory")
    attributes: Optional[Attributes] = None
    slayer: Optional[Slayer] = None
    trophy_fish: Optional[Dict[str, Any]] = Field(default=None, alias="trophy_fish")
    objectives: Optional[List[Objective]] = None
    collection: Optional[Dict[str, int]] = None


class SkillTree(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    nodes: Optional[Dict[str, Dict[str, Any]]] = Field(default=None)


class Forge(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    forge_processes: Optional[Dict[str, Dict[str, Any]]] = Field(
        default=None, alias="forge_processes"
    )


class GlacitePlayerData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    # TODO enum
    fossils_donated: Optional[List[str]] = Field(default=None, alias="fossils_donated")
    fossil_dust: Optional[float] = Field(default=None, alias="fossil_dust")
    # TODO enum
    corpses_looted: Optional[Dict[str, int]] = Field(default=None, alias="corpses_looted")
    mineshafts_entered: Optional[int] = Field(default=None, alias="mineshafts_entered")


class ProfileData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    bank_account: Optional[float] = Field(default=None, alias="bank_account")
    first_join: Optional[int] = Field(default=None, alias="first_join")
    personal_bank_upgrade: Optional[int] = Field(default=None, alias="personal_bank_upgrade")
    cookie_buff_active: Optional[bool] = Field(default=None, alias="cookie_buff_active")


class GardenPlayerData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    copper: Optional[int] = Field(default=None)
    larva_consumed: Optional[int] = Field(default=None, alias="larva_consumed")
    # TODO enum
    analyzed_greenhouse_crops: Optional[List[str]] = Field(
        default=None, alias="analyzed_greenhouse_crops"
    )
    # TODO enum
    discovered_greenhouse_crops: Optional[List[str]] = Field(
        default=None, alias="discovered_greenhouse_crops"
    )


class AccessoryBagStorage(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    tuning: Optional[Dict[str, TuningSlot]] = Field(default=None)
    # TODO ENUM
    selected_power: Optional[str] = Field(default=None, alias="selected_power")
    bag_upgrades_purchased: Optional[int] = Field(default=None, alias="bag_upgrades_purchased")
    # TODO enum
    unlocked_powers: Optional[List[str]] = Field(default=None, alias="unlocked_powers")
    highest_magical_power: Optional[int] = Field(default=None, alias="highest_magical_power")


class TuningSlot(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    health: Optional[int] = Field(default=None)
    defense: Optional[int] = Field(default=None)
    walk_speed: Optional[int] = Field(default=None, alias="walk_speed")
    strength: Optional[int] = Field(default=None)
    critical_damage: Optional[int] = Field(default=None, alias="critical_damage")
    critical_chance: Optional[int] = Field(default=None, alias="critical_chance")
    attack_speed: Optional[int] = Field(default=None, alias="attack_speed")
    intelligence: Optional[int] = Field(default=None)


class Leveling(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    experience: Optional[int] = Field(default=None)
    # TODO enum
    completions: Optional[Dict[str, int]] = Field(default=None)
    # TODO enum
    completed_tasks: Optional[List[str]] = Field(default=None, alias="completed_tasks")
    highest_pet_score: Optional[int] = Field(default=None, alias="highest_pet_score")
    mining_fiesta_ores_mined: Optional[int] = Field(default=None, alias="mining_fiesta_ores_mined")
    migrated: Optional[bool] = None
    migrated_completions_v2: Optional[bool] = Field(default=None, alias="migrated_completions_2")
    claimed_talisman: Optional[bool] = Field(default=None, alias="claimed_talisman")
    # TODO enum
    bop_bonus: Optional[str] = Field(default=None, alias="bop_bonus")
    # TODO enum
    emblem_unlocks: Optional[List[str]] = Field(default=None, alias="emblem_unlocks")
    category_expanded: Optional[bool] = Field(default=None, alias="category_expanded")
    fishing_festival_sharks_killed: Optional[int] = Field(
        default=None, alias="fishing_festival_sharks_killed"
    )
    # TODO enum
    task_sort: Optional[str] = Field(default=None, alias="task_sort")
    # TODO enum
    last_viewed_tasks: Optional[List[str]] = Field(default=None, alias="last_viewed_tasks")
    # TODO enum
    selected_symbol: Optional[str] = Field(default=None, alias="selected_symbol")


class ItemData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    soulflow: Optional[int] = Field(default=None)
    favorite_arrow: Optional[str] = Field(default=None, alias="favorite_arrow")


class Currencies(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    coin_purse: Optional[float] = Field(default=None, alias="coin_purse")
    motes_purse: Optional[float] = Field(default=None, alias="motes_purse")
    essence: Optional[Dict[str, EssenceInfo]] = Field(default=None)


class EssenceInfo(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    current: Optional[int] = Field(default=None)


class CommunityUpgrades(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    currently_upgrading: Optional[str] = Field(default=None, alias="currently_upgrading")
    upgrade_states: Optional[List[UpgradeState]] = Field(default=None, alias="upgrade_states")


class UpgradeState(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    upgrade: Optional[str] = Field(default=None)
    tier: Optional[int] = Field(default=None)
    started_ms: Optional[int] = Field(default=None, alias="started_ms")
    started_by: Optional[str] = Field(default=None, alias="started_by")
    claimed_by: Optional[str] = Field(default=None, alias="claimed_by")


class Banking(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    balance: Optional[float] = Field(default=None)
    transactions: Optional[List[Transaction]] = Field(default=None)


class Transaction(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    amount: Optional[float] = Field(default=None)
    timestamp: Optional[int] = Field(default=None)
    action: Optional[str] = Field(default=None)
    initiator_name: Optional[str] = Field(default=None, alias="initiator_name")


class ForagingCore(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    daily_trees_cut_day: Optional[int] = Field(default=None, alias="daily_trees_cut_day")
    daily_trees_cut: Optional[int] = Field(default=None, alias="daily_trees_cut")
    daily_gifts: Optional[int] = Field(default=None, alias="daily_gifts")
    daily_log_cut_day: Optional[int] = Field(default=None, alias="daily_log_cut_day")
    daily_log_cut: Optional[List[Any]] = Field(default=None, alias="daily_log_cut")
    forest_whispers: Optional[int] = Field(default=None, alias="forests_whispers")
    forest_whispers_spent: Optional[int] = Field(default=None, alias="forests_whispers_spent")
    current_daily_effect: Optional[str] = Field(default=None, alias="current_daily_effect")
    current_daily_effect_last_changed: Optional[int] = Field(
        default=None, alias="current_daily_effect_last_changed"
    )


class Shards(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    traps: Optional[Dict[str, Any]] = Field(default=None)
    shard_sort: Optional[str] = Field(default=None, alias="shard_sort")
    fusion_result_sort: Optional[str] = Field(default=None, alias="fusion_result_sort")
    owned: Optional[List[ShardOwned]] = None


class ShardOwned(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: Optional[str] = None
    amount_owned: Optional[int] = Field(default=None, alias="amount_owned")
    captured: Optional[int] = None


class Quests(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    trapper_quest: Optional[TrapperQuest] = Field(default=None, alias="trapper_quest")


class TrapperQuest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    last_task_time: Optional[int] = Field(default=None, alias="last_task_time")
    pelt_count: Optional[int] = Field(default=None, alias="pelt_count")


class WinterPlayerData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    refined_jyrre_uses: Optional[int] = Field(default=None, alias="refined_jyrre_uses")


class FairySoul(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    fairy_exchanges: Optional[int] = Field(default=None, alias="fairy_exchanges")
    total_collected: Optional[int] = Field(default=None, alias="total_collected")
    unspent_souls: Optional[int] = Field(default=None, alias="unspent_souls")


class Temples(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    unlocked_temples: Optional[List[str]] = Field(default=None, alias="unlocked_temples")


class SharedInventory(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    carnival_mask_inventory_contents: Optional[InventoryObject] = Field(
        default=None, alias="carnival_mask_inventory_contents"
    )
    candy_inventory_contents: Optional[InventoryObject] = Field(
        default=None, alias="candy_inventory_contents"
    )


class Attributes(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    stacks: Optional[Dict[str, int]] = None


class Objective(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    status: Optional[str] = None
    progress: Optional[float] = None
    completed_at: Optional[int] = Field(default=None, alias="completed_at")
    data: Dict[str, str] = Field(default_factory=dict)
