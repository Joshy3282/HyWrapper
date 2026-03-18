from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.rate_limit import RateLimit


class QuestsResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    cause: Optional[str] = None
    lastUpdated: int = Field(default=0)
    quests: Dict[str, List[Quest]] = Field(default={})
    rateLimit: Optional[RateLimit] = None


class Quest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str = Field(default="")
    name: str = Field(default="")
    description: str = Field(default="")
    rewards: List[QuestReward] = Field(default=[])
    objectives: List[QuestObjective] = Field(default=[])
    requirements: List[QuestRequirement] = Field(default=[])


class QuestReward(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: str = Field(default="")
    amount: int = Field(default=0)


class QuestObjective(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str = Field(default="")
    type: str = Field(default="")
    integerValue: Optional[int] = None


class QuestRequirement(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: str = Field(default="")
