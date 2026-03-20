from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.data.skyblock.garden_plot import GardenPlot
from hywrapper.data.skyblock.garden_resource import GardenResource
from hywrapper.data.skyblock.garden_upgrade import GardenUpgrade
from hywrapper.data.skyblock.visitor import Visitor
from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class GardenResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    garden: Optional[Garden] = None
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class Garden(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    uuid: Optional[str] = Field(default=None)
    unlockedPlots: Optional[List[GardenPlot]] = Field(default=None, alias="unlocked_plots_ids")
    commissionData: Optional[CommissionData] = Field(default=None, alias="commission_data")
    resourcesCollected: Optional[Dict[GardenResource, int]] = Field(
        default=None, alias="resources_collected"
    )
    gardenExperience: Optional[float] = Field(default=None, alias="garden_experience")
    composterData: Optional[ComposterData] = Field(default=None, alias="composter_data")
    selectedBarnSkin: Optional[str] = Field(default=None, alias="selected_barn_skin")
    cropUpgradeLevels: Optional[Dict[GardenResource, int]] = Field(
        default=None, alias="crop_upgrade_levels"
    )
    gardenUpgrades: Optional[Dict[GardenUpgrade, int]] = Field(
        default=None, alias="garden_upgrades"
    )
    unlockedBarnSkins: Optional[List[str]] = Field(default=None, alias="unlocked_barn_skins")
    greenhouseSlots: Optional[List[GreenhouseCoordinate]] = Field(
        default=None, alias="greenhouse_slots"
    )
    lastGrowthStageTime: Optional[int] = Field(default=None, alias="last_growth_stage_time")


class CommissionData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    visits: Optional[Dict[Visitor, int]] = Field(default=None)
    completed: Optional[Dict[Visitor, int]] = Field(default=None)
    totalCompleted: Optional[int] = Field(default=None, alias="total_completed")
    uniqueNpcsServed: Optional[int] = Field(default=None, alias="unique_npcs_served")


class ComposterData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    organicMatter: Optional[float] = Field(default=None, alias="organic_matter")
    fuelUnits: Optional[float] = Field(default=None, alias="fuel_units")
    compostUnits: Optional[int] = Field(default=None, alias="compost_units")
    compostItems: Optional[int] = Field(default=None, alias="compost_items")
    conversionTicks: Optional[int] = Field(default=None, alias="conversion_ticks")
    lastSave: Optional[int] = Field(default=None, alias="last_save")
    upgrades: Optional[ComposterUpgrades] = None


class ComposterUpgrades(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    speed: Optional[int] = Field(default=None)
    multiDrop: Optional[int] = Field(default=None, alias="multi_drop")
    fuelCap: Optional[int] = Field(default=None, alias="fuel_cap")
    organicMatterCap: Optional[int] = Field(default=None, alias="organic_matter_cap")
    costReduction: Optional[int] = Field(default=None, alias="cost_reduction")


class GreenhouseCoordinate(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    x: Optional[int] = Field(default=None)
    y: Optional[int] = Field(default=None)
