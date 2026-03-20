from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field


class Content(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    collected: int = 0
    claimed_rewards: Optional[bool] = Field(default=None, alias="claimed_rewards")
    claimed_position: int = Field(default=0, alias="claimed_position")
    claimed_participants: int = Field(default=0, alias="claimed_participants")


class Perks(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    double_drops: int = Field(default=0, alias="double_drops")
    farming_level_cap: int = Field(default=0, alias="farming_level_cap")
    personal_bests: Optional[bool] = Field(default=None, alias="personal_bests")


class JacobsContent(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    # TODO enum
    medals_inv: Dict[str, int] = Field(default_factory=dict, alias="medals_inv")
    perks: Optional[Perks] = None
    talked: Optional[bool] = None
    contents: Dict[str, Content] = Field(default_factory=dict)
    # TODO enum
    unique_brackets: Dict[str, List[str]] = Field(default_factory=dict, alias="unique_brackets")
    migration: Optional[bool] = None
    # TODO enum
    personal_bests: Dict[str, int] = Field(default_factory=dict, alias="personal_bests")
