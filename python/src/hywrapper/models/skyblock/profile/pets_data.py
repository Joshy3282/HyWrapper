from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field


class PetData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    uuid: str = ""
    unique_id: str = Field(default="", alias="uniqueId")
    # TODO enum
    type: str = ""
    exp: float = 0.0
    active: Optional[bool] = None
    # TODO enum
    tier: str = ""
    # TODO enum
    held_item: str = Field(default="", alias="heldItem")
    candy_used: int = Field(default=0, alias="candyUsed")
    pet_soulbound: Optional[bool] = Field(default=None, alias="petSoulbound")
    # TODO enum
    skin: str = ""
    # TODO enum
    extra: Dict[str, int] = Field(default_factory=dict)


class AutopetException(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str = ""
    # TODO enums
    data: Dict[str, str] = Field(default_factory=dict)


class AutopetRule(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    uuid: str = ""
    # TODO enum
    id: str = ""
    name: str = ""
    unique_id: str = Field(default="", alias="uniqueId")
    exceptions: List[AutopetException] = Field(default_factory=list)
    disabled: bool = False
    # TODO enums
    data: Dict[str, str] = Field(default_factory=dict)


class Autopet(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    rules_limit: int = Field(default=0, alias="rules_limit")
    rules: List[AutopetRule] = Field(default_factory=list)
    migrated: Optional[bool] = None
    migrated_2: Optional[bool] = Field(default=None, alias="migrated_2")


class PetCare(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    coins_spent: float = Field(default=0.0, alias="coins_spent")
    # TODO enum
    pet_types_sacrificed: List[str] = Field(default_factory=list, alias="pet_types_sacrificed")


class PetsData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    pet_care: Optional[PetCare] = Field(default=None, alias="pet_care")
    autopet: Optional[Autopet] = None
    pets: List[PetData] = Field(default_factory=list)
