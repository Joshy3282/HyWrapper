from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field


class PetsData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    petCare: Optional[PetCare] = None
    autopet: Optional[Autopet] = None
    pets: List[PetData] = Field(default=[])


class PetCare(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    coinsSpent: float = Field(default=0.0)
    petTypesSacrificed: List[str] = Field(default=[])


class Autopet(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    rulesLimit: int = Field(default=0)
    rules: List[AutopetRule] = Field(default=[])
    migrated: Optional[bool] = None
    migrated2: Optional[bool] = None


class AutopetRule(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    uuid: str = Field(default="")
    id: str = Field(default="")
    name: str = Field(default="")
    uniqueId: str = Field(default="")
    exceptions: List[AutopetException] = Field(default=[])
    disabled: bool = Field(default=False)
    data: Dict[str, str] = Field(default={})


class AutopetException(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str = Field(default="")
    data: Dict[str, str] = Field(default={})


class PetData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    uuid: str = Field(default="")
    uniqueId: str = Field(default="")
    type: str = Field(default="")
    exp: float = Field(default=0.0)
    active: Optional[bool] = None
    tier: str = Field(default="")
    heldItem: str = Field(default="")
    candyUsed: int = Field(default=0)
    petSoulbound: Optional[bool] = None
    skin: str = Field(default="")
    extra: Dict[str, int] = Field(default={})
