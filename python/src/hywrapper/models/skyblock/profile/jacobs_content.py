from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field


class Content(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    collected: Optional[int] = None
    claimed_rewards: Optional[bool] = Field(default=None, alias="claimed_rewards")
    claimed_position: Optional[int] = Field(default=None, alias="claimed_position")
    claimed_participants: Optional[int] = Field(default=None, alias="claimed_participants")


class Perks(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    double_drops: Optional[int] = Field(default=None, alias="double_drops")
    farming_level_cap: Optional[int] = Field(default=None, alias="farming_level_cap")
    personal_bests: Optional[bool] = Field(default=None, alias="personal_bests")


class JacobsContent(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    # TODO enum
    medals_inv: Optional[Dict[str, int]] = Field(default=None, alias="medals_inv")
    perks: Optional[Perks] = None
    talked: Optional[bool] = None
    contents: Optional[Dict[str, Content]] = Field(default=None)
    # TODO enum
    unique_brackets: Optional[Dict[str, List[str]]] = Field(default=None, alias="unique_brackets")
    migration: Optional[bool] = None
    # TODO enum
    personal_bests: Optional[Dict[str, int]] = Field(default=None, alias="personal_bests")
