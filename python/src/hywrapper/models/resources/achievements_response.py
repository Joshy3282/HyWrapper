from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.rate_limit import RateLimit


class AchievementsResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    cause: Optional[str] = None
    lastUpdated: int = Field(default=0)
    achievements: Dict[str, GameAchievement] = Field(default={})
    rateLimit: Optional[RateLimit] = None


class GameAchievement(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    oneTime: Dict[str, OneTimeAchievement] = Field(default={})
    tiered: Dict[str, TieredAchievement] = Field(default={})
    totalPoints: int = Field(default=0)
    totalLegacyPoints: int = Field(default=0)


class OneTimeAchievement(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: str = Field(default="")
    description: str = Field(default="")
    points: int = Field(default=0)
    gamePercentUnlocked: Optional[float] = None
    globalPercentUnlocked: Optional[float] = None


class TieredAchievement(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: str
    description: str = Field(default="")
    tiers: List[AchievementTier] = Field(default=[])


class AchievementTier(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    tier: int = Field(default=0)
    points: int = Field(default=0)
    amount: int = Field(default=0)
