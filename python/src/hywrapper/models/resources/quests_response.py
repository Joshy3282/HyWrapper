from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse


class QuestReward(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: str = ""
    amount: int = 0


class QuestObjective(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str = ""
    type: str = ""
    integer_value: Optional[int] = Field(default=None, alias="integer")


class QuestRequirement(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: str = ""


class Quest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str = ""
    name: str = ""
    description: str = ""
    rewards: List[QuestReward] = Field(default_factory=list)
    objectives: List[QuestObjective] = Field(default_factory=list)
    requirements: List[QuestRequirement] = Field(default_factory=list)


class QuestsResponse(HypixelResponse):
    last_updated: int = Field(default=0, alias="lastUpdated")
    quests: Dict[str, List[Quest]] = Field(default_factory=dict)
