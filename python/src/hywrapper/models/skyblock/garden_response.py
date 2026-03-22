from __future__ import annotations

from typing import Any, Dict, List, Optional

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
    unlocked_plots: Optional[List[GardenPlot]] = Field(default=None, alias="unlocked_plots_ids")
    commission_data: Optional[CommissionData] = Field(default=None, alias="commission_data")
    resources_collected: Optional[Dict[GardenResource, int]] = Field(
        default=None, alias="resources_collected"
    )
    garden_experience: Optional[float] = Field(default=None, alias="garden_experience")
    active_commissions: Optional[List[Any]] = Field(default=None, alias="active_commissions")
    composter_data: Optional[ComposterData] = Field(default=None, alias="composter_data")
    selected_barn_skin: Optional[str] = Field(default=None, alias="selected_barn_skin")
    crop_upgrade_levels: Optional[Dict[GardenResource, int]] = Field(
        default=None, alias="crop_upgrade_levels"
    )
    garden_upgrades: Optional[Dict[GardenUpgrade, int]] = Field(
        default=None, alias="garden_upgrades"
    )
    unlocked_barn_skins: Optional[List[str]] = Field(default=None, alias="unlocked_barn_skins")
    greenhouse_slots: Optional[List[GreenhouseCoordinate]] = Field(
        default=None, alias="greenhouse_slots"
    )
    last_growth_stage_time: Optional[int] = Field(default=None, alias="last_growth_stage_time")


class CommissionData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    visits: Optional[Dict[Visitor, int]] = Field(default=None)
    completed: Optional[Dict[Visitor, int]] = Field(default=None)
    total_completed: Optional[int] = Field(default=None, alias="total_completed")
    unique_npcs_served: Optional[int] = Field(default=None, alias="unique_npcs_served")


class ComposterData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    organic_matter: Optional[float] = Field(default=None, alias="organic_matter")
    fuel_units: Optional[float] = Field(default=None, alias="fuel_units")
    compost_units: Optional[int] = Field(default=None, alias="compost_units")
    compost_items: Optional[int] = Field(default=None, alias="compost_items")
    conversion_ticks: Optional[int] = Field(default=None, alias="conversion_ticks")
    last_save: Optional[int] = Field(default=None, alias="last_save")
    upgrades: Optional[ComposterUpgrades] = None


class ComposterUpgrades(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    speed: Optional[int] = Field(default=None)
    multi_drop: Optional[int] = Field(default=None, alias="multi_drop")
    fuel_cap: Optional[int] = Field(default=None, alias="fuel_cap")
    organic_matter_cap: Optional[int] = Field(default=None, alias="organic_matter_cap")
    cost_reduction: Optional[int] = Field(default=None, alias="cost_reduction")


class GreenhouseCoordinate(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    x: Optional[int] = Field(default=None)
    y: Optional[int] = Field(default=None)
