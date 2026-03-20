from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.data.skyblock.skill_type import SkillType
from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class SkillsResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    lastUpdated: Optional[int] = Field(default=None)
    version: Optional[str] = Field(default=None)
    skills: Optional[Dict[str, Skill]] = Field(default=None)
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)

    def get_skill(self, skill_type: SkillType) -> Optional[Skill]:
        if self.skills is None:
            return None
        return self.skills.get(skill_type.name)


class Skill(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    maxLevel: Optional[int] = Field(default=None)
    levels: Optional[List[Level]] = Field(default=None)


class Level(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    level: Optional[int] = Field(default=None)
    totalExpRequired: Optional[float] = Field(default=None)
    unlocks: Optional[List[str]] = Field(default=None)
