from __future__ import annotations

from typing import Dict, Optional

from pydantic import BaseModel, ConfigDict, Field


class PlayerInventory(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    bag_contents: Optional[BagContents] = Field(default=None, alias="bag_contents")
    inv_contents: Optional[InventoryObject] = Field(default=None, alias="inv_contents")
    ender_chest_contents: Optional[InventoryObject] = Field(
        default=None, alias="ender_chest_contents"
    )
    backpack_icons: Optional[Dict[str, InventoryObject]] = Field(
        default=None, alias="backpack_icons"
    )
    inv_armor: Optional[InventoryObject] = Field(default=None, alias="inv_armor")
    equipment_contents: Optional[InventoryObject] = Field(default=None, alias="equipment_contents")
    personal_vault_contents: Optional[InventoryObject] = Field(
        default=None, alias="personal_vault_contents"
    )
    wardrobe_equipped_slot: Optional[int] = Field(default=None, alias="wardrobe_equipped_slot")
    backpack_contents: Optional[Dict[str, InventoryObject]] = Field(
        default=None, alias="backpack_contents"
    )
    sacks_counts: Optional[Dict[str, int]] = Field(default=None, alias="sacks_counts")
    wardrobe_contents: Optional[InventoryObject] = Field(default=None, alias="wardrobe_contents")


class BagContents(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    sacks_bag: Optional[InventoryObject] = Field(default=None, alias="sacks_bag")
    potion_bag: Optional[InventoryObject] = Field(default=None, alias="potion_bag")
    talisman_bag: Optional[InventoryObject] = Field(default=None, alias="talisman_bag")
    fishing_bag: Optional[InventoryObject] = Field(default=None, alias="fishing_bag")
    quiver: Optional[InventoryObject] = None


class InventoryObject(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: Optional[int] = None
    data: Optional[str] = None
