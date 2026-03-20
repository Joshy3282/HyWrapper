from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse


class AchievementTier(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    tier: Optional[int] = None
    points: Optional[int] = None
    amount: Optional[int] = None


class TieredAchievement(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: Optional[str] = None
    description: Optional[str] = None
    tiers: Optional[List[AchievementTier]] = Field(default=None)


class OneTimeAchievement(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: Optional[str] = None
    description: Optional[str] = None
    points: Optional[int] = None
    game_percent_unlocked: Optional[float] = Field(default=None, alias="gamePercentUnlocked")
    global_percent_unlocked: Optional[float] = Field(default=None, alias="globalPercentUnlocked")


class GameAchievement(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    one_time: Optional[Dict[str, OneTimeAchievement]] = Field(default=None, alias="one_time")
    tiered: Optional[Dict[str, TieredAchievement]] = Field(default=None)
    total_points: Optional[int] = Field(default=None, alias="total_points")
    total_legacy_points: Optional[int] = Field(default=None, alias="total_legacy_points")


class AchievementsResponse(HypixelResponse):
    last_updated: Optional[int] = Field(default=None, alias="lastUpdated")
    achievements: Optional[Dict[str, GameAchievement]] = Field(default=None)
