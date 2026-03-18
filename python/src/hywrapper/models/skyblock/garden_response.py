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
    success: bool = Field(default=False)
    cause: Optional[str] = None
    garden: Optional[Garden] = None
    rateLimit: Optional[RateLimit] = None


class Garden(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    uuid: str = Field(default="")
    unlockedPlots: List[GardenPlot] = Field(default=[])
    commissionData: Optional[CommissionData] = None
    resourcesCollected: Dict[GardenResource, int] = Field(default={})
    gardenExperience: float = Field(default=0.0)
    composterData: Optional[ComposterData] = None
    selectedBarnSkin: str = Field(default="")
    cropUpgradeLevels: Dict[GardenResource, int] = Field(default={})
    gardenUpgrades: Dict[GardenUpgrade, int] = Field(default={})
    unlockedBarnSkins: List[str] = Field(default=[])
    greenhouseSlots: List[GreenhouseCoordinate] = Field(default=[])
    lastGrowthStageTime: int = Field(default=0)


class CommissionData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    visits: Dict[Visitor, int] = Field(default={})
    completed: Dict[Visitor, int] = Field(default={})
    totalCompleted: int = Field(default=0)
    uniqueNpcsServed: int = Field(default=0)


class ComposterData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    organicMatter: float = Field(default=0.0)
    fuelUnits: float = Field(default=0.0)
    compostUnits: int = Field(default=0)
    compostItems: int = Field(default=0)
    conversionTicks: int = Field(default=0)
    lastSave: Optional[int] = Field(default=0)
    upgrades: Optional[ComposterUpgrades] = None


class ComposterUpgrades(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    speed: int = Field(default=0)
    multiDrop: int = Field(default=0)
    fuelCap: int = Field(default=0)
    organicMatterCap: int = Field(default=0)
    costReduction: int = Field(default=0)


class GreenhouseCoordinate(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    x: int = Field(default=0)
    y: int = Field(default=0)
