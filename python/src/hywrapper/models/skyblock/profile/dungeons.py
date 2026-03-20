from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field


class BestRun(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    timestamp: int = Field(default=0)
    score_exploration: int = Field(default=1, alias="score_exploration")
    score_speed: int = Field(default=1, alias="score_speed")
    score_skill: int = Field(default=1, alias="score_skill")
    score_bonus: int = Field(default=1, alias="score_bonus")
    dungeon_class: str = Field(default="", alias="dungeon_class")
    teammates: List[str] = Field(default_factory=list)
    elapsed_time: int = Field(default=0, alias="elapsed_time")
    damage_dealt: float = Field(default=0.0, alias="damage_dealt")
    deaths: int = Field(default=1)
    mobs_killed: int = Field(default=0, alias="mobs_killed")
    secrets_found: int = Field(default=0, alias="secrets_found")
    damage_mitigated: float = Field(default=0.0, alias="damage_mitigated")
    ally_healing: float = Field(default=0.0, alias="ally_healing")


class Catacombs(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    times_played: Dict[str, int] = Field(default_factory=dict, alias="times_played")
    experience: float = Field(default=0.0)
    tier_completions: Dict[str, int] = Field(default_factory=dict, alias="tier_completions")
    fastest_time: Dict[str, int] = Field(default_factory=dict, alias="fastest_time")
    best_runs: Dict[str, BestRun] = Field(default_factory=dict, alias="best_runs")
    best_score: Dict[str, int] = Field(default_factory=dict, alias="best_score")
    mobs_killed: Dict[str, int] = Field(default_factory=dict, alias="mobs_killed")
    most_mobs_killed: Dict[str, int] = Field(default_factory=dict, alias="most_mobs_killed")
    most_damage_tank: Dict[str, float] = Field(default_factory=dict, alias="most_damage_tank")
    most_healing: Dict[str, float] = Field(default_factory=dict, alias="most_healing")
    watcher_kills: Dict[str, int] = Field(default_factory=dict, alias="watcher_kills")
    highest_tier_completed: int = Field(default=0, alias="highest_tier_completed")
    fastest_time_s: Dict[str, float] = Field(default_factory=dict, alias="fastest_time_s")
    fastest_time_s_plus: Dict[str, float] = Field(default_factory=dict, alias="fastest_time_s_plus")
    most_damage_berserk: Dict[str, float] = Field(default_factory=dict, alias="most_damage_berserk")
    most_damage_healer: Dict[str, float] = Field(default_factory=dict, alias="most_damage_healer")
    most_damage_mage: Dict[str, float] = Field(default_factory=dict, alias="most_damage_mage")
    milestone_completions: Dict[str, float] = Field(
        default_factory=dict, alias="milestone_completions"
    )
    most_damage_archer: Dict[str, float] = Field(default_factory=dict, alias="most_damage_archer")


class MasterCatacombs(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    times_played: Dict[str, int] = Field(default_factory=dict, alias="times_played")
    tier_completions: Dict[str, int] = Field(default_factory=dict, alias="tier_completions")
    fastest_time: Dict[str, int] = Field(default_factory=dict, alias="fastest_time")
    best_runs: Dict[str, BestRun] = Field(default_factory=dict, alias="best_runs")
    best_score: Dict[str, int] = Field(default_factory=dict, alias="best_score")
    mobs_killed: Dict[str, int] = Field(default_factory=dict, alias="mobs_killed")
    most_mobs_killed: Dict[str, int] = Field(default_factory=dict, alias="most_mobs_killed")
    most_damage_tank: Dict[str, float] = Field(default_factory=dict, alias="most_damage_tank")
    most_healing: Dict[str, float] = Field(default_factory=dict, alias="most_healing")
    watcher_kills: Dict[str, int] = Field(default_factory=dict, alias="watcher_kills")
    highest_tier_completed: int = Field(default=0, alias="highest_tier_completed")
    fastest_time_s: Dict[str, float] = Field(default_factory=dict, alias="fastest_time_s")
    fastest_time_s_plus: Dict[str, float] = Field(default_factory=dict, alias="fastest_time_s_plus")
    most_damage_berserk: Dict[str, float] = Field(default_factory=dict, alias="most_damage_berserk")
    most_damage_healer: Dict[str, float] = Field(default_factory=dict, alias="most_damage_healer")
    most_damage_mage: Dict[str, float] = Field(default_factory=dict, alias="most_damage_mage")
    milestone_completions: Dict[str, float] = Field(
        default_factory=dict, alias="milestone_completions"
    )
    most_damage_archer: Dict[str, float] = Field(default_factory=dict, alias="most_damage_archer")


class DungeonType(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    catacombs: Optional[Catacombs] = None
    master_catacombs: Optional[MasterCatacombs] = Field(default=None, alias="master_catacombs")


class DungeonJournal(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    unlocked_journals: List[str] = Field(default_factory=list, alias="unlocked_journals")


class DailyRuns(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    current_day_stamp: int = Field(default=0, alias="current_day_stamp")
    completed_runs_count: int = Field(default=0, alias="completed_runs_count")


class DungeonHubRaceSettings(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    selected_race: str = Field(default="", alias="selected_race")
    selected_setting: str = Field(default="", alias="selected_setting")
    runback: Optional[bool] = None


class Dungeons(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    dungeon_types: Optional[DungeonType] = Field(default=None, alias="dungeon_types")
    player_classes: Dict[str, Dict[str, float]] = Field(
        default_factory=dict, alias="player_classes"
    )
    dungeon_journal: Optional[DungeonJournal] = Field(default=None, alias="dungeon_journal")
    dungeons_blah_blah: List[str] = Field(default_factory=list, alias="dungeons_blah_blah")
    selected_dungeon_class: str = Field(default="", alias="selected_dungeon_class")
    daily_runs: Optional[DailyRuns] = Field(default=None, alias="daily_runs")
    dungeon_hub_race_settings: Optional[DungeonHubRaceSettings] = Field(
        default=None, alias="dungeon_hub_race_settings"
    )
    last_dungeon_run: str = Field(default="", alias="last_dungeon_run")
    secrets: int = Field(default=0)
