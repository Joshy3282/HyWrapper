from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse


class QuestReward(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: Optional[str] = None
    amount: Optional[int] = None


class QuestObjective(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: Optional[str] = None
    type: Optional[str] = None
    integer_value: Optional[int] = Field(default=None, alias="integer")


class QuestRequirement(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: Optional[str] = None


class Quest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    rewards: Optional[List[QuestReward]] = Field(default=None)
    objectives: Optional[List[QuestObjective]] = Field(default=None)
    requirements: Optional[List[QuestRequirement]] = Field(default=None)


class QuestsResponse(HypixelResponse):
    last_updated: Optional[int] = Field(default=None, alias="lastUpdated")
    quests: Optional[Dict[str, List[Quest]]] = Field(default=None)
