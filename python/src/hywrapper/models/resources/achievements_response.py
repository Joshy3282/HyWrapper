from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse


class AchievementTier(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    tier: int = 0
    points: int = 0
    amount: int = 0


class TieredAchievement(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: str
    description: str = ""
    tiers: List[AchievementTier] = Field(default_factory=list)


class OneTimeAchievement(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: str = ""
    description: str = ""
    points: int = 0
    game_percent_unlocked: Optional[float] = Field(default=None, alias="gamePercentUnlocked")
    global_percent_unlocked: Optional[float] = Field(default=None, alias="globalPercentUnlocked")


class GameAchievement(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    one_time: Dict[str, OneTimeAchievement] = Field(default_factory=dict, alias="one_time")
    tiered: Dict[str, TieredAchievement] = Field(default_factory=dict)
    total_points: int = Field(default=0, alias="total_points")
    total_legacy_points: int = Field(default=0, alias="total_legacy_points")


class AchievementsResponse(HypixelResponse):
    last_updated: int = Field(default=0, alias="lastUpdated")
    achievements: Dict[str, GameAchievement] = Field(default_factory=dict)
