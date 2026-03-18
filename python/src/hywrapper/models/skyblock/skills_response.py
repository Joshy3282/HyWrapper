from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.rate_limit import RateLimit


class SkillsResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    cause: Optional[str] = None
    lastUpdated: int = Field(default=0)
    version: str = Field(default="")
    skills: Dict[str, Skill] = Field(default={})
    rateLimit: Optional[RateLimit] = None


class Skill(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: str = Field(default="")
    description: str = Field(default="")
    maxLevel: int = Field(default=0)
    levels: List[Level] = Field(default=[])


class Level(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    level: int
    totalExpRequired: float = Field(default=0.0)
    unlocks: List[str] = Field(default=[])
