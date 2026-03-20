from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse


class GuildAchievementTier(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    tier: Optional[int] = None
    amount: Optional[int] = None


class GuildTieredAchievement(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: Optional[str] = None
    description: Optional[str] = None
    tiers: Optional[List[GuildAchievementTier]] = Field(default=None)


class GuildOneTimeAchievement(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: Optional[str] = None
    description: Optional[str] = None


class GuildsAchievementsResponse(HypixelResponse):
    last_updated: Optional[int] = Field(default=None, alias="lastUpdated")
    one_time: Optional[Dict[str, GuildOneTimeAchievement]] = Field(default=None, alias="one_time")
    tiered: Optional[Dict[str, GuildTieredAchievement]] = Field(default=None)
