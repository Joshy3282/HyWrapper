from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field


class PetData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    uuid: Optional[str] = None
    unique_id: Optional[str] = Field(default=None, alias="uniqueId")
    # TODO enum
    type: Optional[str] = None
    exp: Optional[float] = None
    active: Optional[bool] = None
    # TODO enum
    tier: Optional[str] = None
    # TODO enum
    held_item: Optional[str] = Field(default=None, alias="heldItem")
    candy_used: Optional[int] = Field(default=None, alias="candyUsed")
    pet_soulbound: Optional[bool] = Field(default=None, alias="petSoulbound")
    # TODO enum
    skin: Optional[str] = None
    # TODO enum
    extra: Optional[Dict[str, int]] = Field(default=None)


class AutopetException(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: Optional[str] = None
    # TODO enums
    data: Optional[Dict[str, str]] = Field(default=None)


class AutopetRule(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    uuid: Optional[str] = None
    # TODO enum
    id: Optional[str] = None
    name: Optional[str] = None
    unique_id: Optional[str] = Field(default=None, alias="uniqueId")
    exceptions: Optional[List[AutopetException]] = Field(default=None)
    disabled: Optional[bool] = None
    # TODO enums
    data: Optional[Dict[str, str]] = Field(default=None)


class Autopet(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    rules_limit: Optional[int] = Field(default=None, alias="rules_limit")
    rules: Optional[List[AutopetRule]] = Field(default=None)
    migrated: Optional[bool] = None
    migrated_2: Optional[bool] = Field(default=None, alias="migrated_2")


class PetCare(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    coins_spent: Optional[float] = Field(default=None, alias="coins_spent")
    # TODO enum
    pet_types_sacrificed: Optional[List[str]] = Field(default=None, alias="pet_types_sacrificed")


class PetsData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    pet_care: Optional[PetCare] = Field(default=None, alias="pet_care")
    autopet: Optional[Autopet] = None
    pets: Optional[List[PetData]] = Field(default=None)
