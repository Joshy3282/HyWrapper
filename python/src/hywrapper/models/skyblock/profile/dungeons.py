from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field


class BestRun(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    timestamp: Optional[int] = Field(default=None)
    score_exploration: Optional[int] = Field(default=None, alias="score_exploration")
    score_speed: Optional[int] = Field(default=None, alias="score_speed")
    score_skill: Optional[int] = Field(default=None, alias="score_skill")
    score_bonus: Optional[int] = Field(default=None, alias="score_bonus")
    dungeon_class: Optional[str] = Field(default=None, alias="dungeon_class")
    teammates: Optional[List[str]] = Field(default=None)
    elapsed_time: Optional[int] = Field(default=None, alias="elapsed_time")
    damage_dealt: Optional[float] = Field(default=None, alias="damage_dealt")
    deaths: Optional[int] = Field(default=None)
    mobs_killed: Optional[int] = Field(default=None, alias="mobs_killed")
    secrets_found: Optional[int] = Field(default=None, alias="secrets_found")
    damage_mitigated: Optional[float] = Field(default=None, alias="damage_mitigated")
    ally_healing: Optional[float] = Field(default=None, alias="ally_healing")


class Catacombs(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    times_played: Optional[Dict[str, int]] = Field(default=None, alias="times_played")
    experience: Optional[float] = Field(default=None)
    tier_completions: Optional[Dict[str, int]] = Field(default=None, alias="tier_completions")
    fastest_time: Optional[Dict[str, int]] = Field(default=None, alias="fastest_time")
    best_runs: Optional[Dict[str, BestRun]] = Field(default=None, alias="best_runs")
    best_score: Optional[Dict[str, int]] = Field(default=None, alias="best_score")
    mobs_killed: Optional[Dict[str, int]] = Field(default=None, alias="mobs_killed")
    most_mobs_killed: Optional[Dict[str, int]] = Field(default=None, alias="most_mobs_killed")
    most_damage_tank: Optional[Dict[str, float]] = Field(default=None, alias="most_damage_tank")
    most_healing: Optional[Dict[str, float]] = Field(default=None, alias="most_healing")
    watcher_kills: Optional[Dict[str, int]] = Field(default=None, alias="watcher_kills")
    highest_tier_completed: Optional[int] = Field(default=None, alias="highest_tier_completed")
    fastest_time_s: Optional[Dict[str, float]] = Field(default=None, alias="fastest_time_s")
    fastest_time_s_plus: Optional[Dict[str, float]] = Field(
        default=None, alias="fastest_time_s_plus"
    )
    most_damage_berserk: Optional[Dict[str, float]] = Field(
        default=None, alias="most_damage_berserk"
    )
    most_damage_healer: Optional[Dict[str, float]] = Field(default=None, alias="most_damage_healer")
    most_damage_mage: Optional[Dict[str, float]] = Field(default=None, alias="most_damage_mage")
    milestone_completions: Optional[Dict[str, float]] = Field(
        default=None, alias="milestone_completions"
    )
    most_damage_archer: Optional[Dict[str, float]] = Field(default=None, alias="most_damage_archer")


class MasterCatacombs(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    times_played: Optional[Dict[str, int]] = Field(default=None, alias="times_played")
    tier_completions: Optional[Dict[str, int]] = Field(default=None, alias="tier_completions")
    fastest_time: Optional[Dict[str, int]] = Field(default=None, alias="fastest_time")
    best_runs: Optional[Dict[str, BestRun]] = Field(default=None, alias="best_runs")
    best_score: Optional[Dict[str, int]] = Field(default=None, alias="best_score")
    mobs_killed: Optional[Dict[str, int]] = Field(default=None, alias="mobs_killed")
    most_mobs_killed: Optional[Dict[str, int]] = Field(default=None, alias="most_mobs_killed")
    most_damage_tank: Optional[Dict[str, float]] = Field(default=None, alias="most_damage_tank")
    most_healing: Optional[Dict[str, float]] = Field(default=None, alias="most_healing")
    watcher_kills: Optional[Dict[str, int]] = Field(default=None, alias="watcher_kills")
    highest_tier_completed: Optional[int] = Field(default=None, alias="highest_tier_completed")
    fastest_time_s: Optional[Dict[str, float]] = Field(default=None, alias="fastest_time_s")
    fastest_time_s_plus: Optional[Dict[str, float]] = Field(
        default=None, alias="fastest_time_s_plus"
    )
    most_damage_berserk: Optional[Dict[str, float]] = Field(
        default=None, alias="most_damage_berserk"
    )
    most_damage_healer: Optional[Dict[str, float]] = Field(default=None, alias="most_damage_healer")
    most_damage_mage: Optional[Dict[str, float]] = Field(default=None, alias="most_damage_mage")
    milestone_completions: Optional[Dict[str, float]] = Field(
        default=None, alias="milestone_completions"
    )
    most_damage_archer: Optional[Dict[str, float]] = Field(default=None, alias="most_damage_archer")


class DungeonType(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    catacombs: Optional[Catacombs] = None
    master_catacombs: Optional[MasterCatacombs] = Field(default=None, alias="master_catacombs")


class DungeonJournal(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    unlocked_journals: Optional[List[str]] = Field(default=None, alias="unlocked_journals")


class DailyRuns(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    current_day_stamp: Optional[int] = Field(default=None, alias="current_day_stamp")
    completed_runs_count: Optional[int] = Field(default=None, alias="completed_runs_count")


class Treasures(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    runs: Optional[List[Any]] = Field(default=None)
    chests: Optional[List[Any]] = Field(default=None)


class DungeonHubRaceSettings(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    selected_race: Optional[str] = Field(default=None, alias="selected_race")
    selected_setting: Optional[str] = Field(default=None, alias="selected_setting")
    runback: Optional[bool] = None


class Dungeons(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    dungeon_types: Optional[DungeonType] = Field(default=None, alias="dungeon_types")
    player_classes: Optional[Dict[str, Dict[str, float]]] = Field(
        default=None, alias="player_classes"
    )
    dungeon_journal: Optional[DungeonJournal] = Field(default=None, alias="dungeon_journal")
    dungeons_blah_blah: Optional[List[str]] = Field(default=None, alias="dungeons_blah_blah")
    selected_dungeon_class: Optional[str] = Field(default=None, alias="selected_dungeon_class")
    daily_runs: Optional[DailyRuns] = Field(default=None, alias="daily_runs")
    treasures: Optional[Treasures] = None
    dungeon_hub_race_settings: Optional[DungeonHubRaceSettings] = Field(
        default=None, alias="dungeon_hub_race_settings"
    )
    last_dungeon_run: Optional[str] = Field(default=None, alias="last_dungeon_run")
    secrets: Optional[int] = Field(default=None)
