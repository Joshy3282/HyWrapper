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
    uuid: str = Field(default="")
    unlockedPlots: List[GardenPlot] = Field(default_factory=list, alias="unlocked_plots_ids")
    commissionData: Optional[CommissionData] = Field(default=None, alias="commission_data")
    resourcesCollected: Dict[GardenResource, int] = Field(
        default_factory=dict, alias="resources_collected"
    )
    gardenExperience: float = Field(default=0.0, alias="garden_experience")
    composterData: Optional[ComposterData] = Field(default=None, alias="composter_data")
    selectedBarnSkin: str = Field(default="", alias="selected_barn_skin")
    cropUpgradeLevels: Dict[GardenResource, int] = Field(
        default_factory=dict, alias="crop_upgrade_levels"
    )
    gardenUpgrades: Dict[GardenUpgrade, int] = Field(default_factory=dict, alias="garden_upgrades")
    unlockedBarnSkins: List[str] = Field(default_factory=list, alias="unlocked_barn_skins")
    greenhouseSlots: List[GreenhouseCoordinate] = Field(
        default_factory=list, alias="greenhouse_slots"
    )
    lastGrowthStageTime: int = Field(default=0, alias="last_growth_stage_time")


class CommissionData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    visits: Dict[Visitor, int] = Field(default_factory=dict)
    completed: Dict[Visitor, int] = Field(default_factory=dict)
    totalCompleted: int = Field(default=0, alias="total_completed")
    uniqueNpcsServed: int = Field(default=0, alias="unique_npcs_served")


class ComposterData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    organicMatter: float = Field(default=0.0, alias="organic_matter")
    fuelUnits: float = Field(default=0.0, alias="fuel_units")
    compostUnits: int = Field(default=0, alias="compost_units")
    compostItems: int = Field(default=0, alias="compost_items")
    conversionTicks: int = Field(default=0, alias="conversion_ticks")
    lastSave: Optional[int] = Field(default=0, alias="last_save")
    upgrades: Optional[ComposterUpgrades] = None


class ComposterUpgrades(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    speed: int = Field(default=0)
    multiDrop: int = Field(default=0, alias="multi_drop")
    fuelCap: int = Field(default=0, alias="fuel_cap")
    organicMatterCap: int = Field(default=0, alias="organic_matter_cap")
    costReduction: int = Field(default=0, alias="cost_reduction")


class GreenhouseCoordinate(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    x: int = Field(default=0)
    y: int = Field(default=0)
