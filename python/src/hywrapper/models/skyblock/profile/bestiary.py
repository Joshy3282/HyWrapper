from __future__ import annotations

from typing import Dict, Optional

from pydantic import BaseModel, ConfigDict, Field


class Bestiary(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    migratedStats: Optional[bool] = Field(default=None, alias="migrated_stats")
    migration: Optional[bool] = Field(default=None)
    kills: Optional[Dict[str, int]] = Field(default=None)
    deaths: Optional[Dict[str, int]] = Field(default=None)
    milestone: Optional[Milestone] = Field(default=None)
    miscellaneous: Optional[Miscellaneous] = Field(default=None)


class Milestone(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    lastClaimedMilestone: Optional[int] = Field(default=None, alias="last_claimed_milestone")


class Miscellaneous(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    maxKillsVisible: Optional[bool] = Field(default=None, alias="max_kills_visible")
    milestonesNotifications: Optional[bool] = Field(default=None, alias="milestones_notifications")
