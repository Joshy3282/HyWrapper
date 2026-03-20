from __future__ import annotations

from typing import Dict, List

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse


class GuildAchievementTier(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    tier: int = 0
    amount: int = 0


class GuildTieredAchievement(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: str = ""
    description: str = ""
    tiers: List[GuildAchievementTier] = Field(default_factory=list)


class GuildOneTimeAchievement(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: str = ""
    description: str = ""


class GuildsAchievementsResponse(HypixelResponse):
    last_updated: int = Field(default=0, alias="lastUpdated")
    one_time: Dict[str, GuildOneTimeAchievement] = Field(default_factory=dict, alias="one_time")
    tiered: Dict[str, GuildTieredAchievement] = Field(default_factory=dict)
