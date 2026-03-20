from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.data.skyblock.skill_type import SkillType
from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class SkillsResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    lastUpdated: int = Field(default=0)
    version: str = Field(default="")
    skills: Dict[str, Skill] = Field(default_factory=dict)
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)

    def get_skill(self, skill_type: SkillType) -> Optional[Skill]:
        return self.skills.get(skill_type.name)


class Skill(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: str = Field(default="")
    description: str = Field(default="")
    maxLevel: int = Field(default=0)
    levels: List[Level] = Field(default_factory=list)


class Level(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    level: int
    totalExpRequired: float = Field(default=0.0)
    unlocks: List[str] = Field(default_factory=list)
