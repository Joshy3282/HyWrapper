from __future__ import annotations

from typing import Dict, Optional

from pydantic import BaseModel, ConfigDict, Field


class PlayerInventory(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    bagContents: Optional[BagContents] = Field(default=None, alias="bag_contents")
    invContents: Optional[InventoryObject] = Field(default=None, alias="inv_contents")
    enderChestContents: Optional[InventoryObject] = Field(
        default=None, alias="ender_chest_contents"
    )
    backpackIcons: Optional[Dict[str, InventoryObject]] = Field(
        default=None, alias="backpack_icons"
    )
    invArmor: Optional[InventoryObject] = Field(default=None, alias="inv_armor")
    equipmentContents: Optional[InventoryObject] = Field(default=None, alias="equipment_contents")
    personalVaultContents: Optional[InventoryObject] = Field(
        default=None, alias="personal_vault_contents"
    )
    wardrobeEquippedSlot: Optional[int] = Field(default=None, alias="wardrobe_equipped_slot")
    backpackContents: Optional[Dict[str, InventoryObject]] = Field(
        default=None, alias="backpack_contents"
    )
    sacksCounts: Optional[Dict[str, int]] = Field(default=None, alias="sacks_counts")
    wardrobeContents: Optional[InventoryObject] = Field(default=None, alias="wardrobe_contents")


class BagContents(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    sacksBag: Optional[InventoryObject] = Field(default=None, alias="sacks_bag")
    potionBag: Optional[InventoryObject] = Field(default=None, alias="potion_bag")
    talismanBag: Optional[InventoryObject] = Field(default=None, alias="talisman_bag")
    fishingBag: Optional[InventoryObject] = Field(default=None, alias="fishing_bag")
    quiver: Optional[InventoryObject] = None


class InventoryObject(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: Optional[int] = None
    data: Optional[str] = None
