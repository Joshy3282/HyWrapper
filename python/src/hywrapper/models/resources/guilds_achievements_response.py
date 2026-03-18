from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.rate_limit import RateLimit


class GuildsAchievementsResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    cause: Optional[str] = None
    lastUpdated: int = Field(default=0)
    oneTime: Dict[str, GuildOneTimeAchievement] = Field(default={})
    tiered: Dict[str, GuildTieredAchievement] = Field(default={})
    rateLimit: Optional[RateLimit] = None


class GuildOneTimeAchievement(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: str = Field(default="")
    description: str = Field(default="")


class GuildTieredAchievement(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: str = Field(default="")
    description: str = Field(default="")
    tiers: List[GuildAchievementTier] = Field(default=[])


class GuildAchievementTier(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    tier: int = Field(default=0)
    amount: int = Field(default=0)
