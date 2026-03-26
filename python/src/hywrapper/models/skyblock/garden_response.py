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
    """
    Information about a player's Garden.

    :param success: Whether the request was successful.
    :param cause: The cause of the error, if the request failed.
    :param garden: Information about the Garden.
    """

    model_config = ConfigDict(populate_by_name=True)
    garden: Optional[Garden] = None
    rateLimit: Optional[RateLimit] = Field(default=None, exclude=True)


class Garden(BaseModel):
    """
    Information about a player's Garden.

    :param uuid: Garden UUID.
    :param unlocked_plots: A list of [GardenPlot] that have been unlocked.
    :param commission_data: Information about visitor commissions.
    :param resources_collected: The amount of each [GardenResource] collected.
    :param garden_experience: The amount of garden experience gained.
    :param active_commissions: A list of active visitor commissions.
    :param composter_data: Information about the Garden's composter.
    :param selected_barn_skin: The current selected Barn skin.
    :param crop_upgrade_levels: The upgrade level of each [GardenResource].
    :param garden_upgrades: The upgrade level of each [GardenUpgrade].
    :param unlocked_barn_skins: A list of all unlocked Barn skins.
    :param greenhouse_slots: Unknown.
    :param last_growth_stage_time: Timestamp of the last Greenhouse growth.
    """

    model_config = ConfigDict(populate_by_name=True)
    uuid: Optional[str] = Field(default=None)
    unlocked_plots: Optional[List[GardenPlot]] = Field(default=None, alias="unlocked_plots_ids")
    commission_data: Optional[CommissionData] = Field(default=None, alias="commission_data")
    resources_collected: Optional[Dict[GardenResource, int]] = Field(
        default=None, alias="resources_collected"
    )
    garden_experience: Optional[float] = Field(default=None, alias="garden_experience")
    active_commissions: Optional[List[Any]] = Field(
        default=None, alias="active_commissions"
    )  # TODO empty in tests
    composter_data: Optional[ComposterData] = Field(default=None, alias="composter_data")
    selected_barn_skin: Optional[str] = Field(
        default=None, alias="selected_barn_skin"
    )  # TODO change to enum
    crop_upgrade_levels: Optional[Dict[GardenResource, int]] = Field(
        default=None, alias="crop_upgrade_levels"
    )
    garden_upgrades: Optional[Dict[GardenUpgrade, int]] = Field(
        default=None, alias="garden_upgrades"
    )
    unlocked_barn_skins: Optional[List[str]] = Field(
        default=None, alias="unlocked_barn_skins"
    )  # TODO change to enum
    greenhouse_slots: Optional[List[GreenhouseCoordinate]] = Field(
        default=None, alias="greenhouse_slots"
    )  # TODO unknown
    last_growth_stage_time: Optional[int] = Field(default=None, alias="last_growth_stage_time")


class CommissionData(BaseModel):
    """
    Information about visitor commissions.

    :param visits: A list of how many times each visitor has visited.
    :param completed: A list of how many times each visitor's commission has been completed.
    :param total_completed: Total amount of visitor commissions completed.
    :param unique_npcs_served: How many unique visitors' commissions have been completed.
    """

    model_config = ConfigDict(populate_by_name=True)
    visits: Optional[Dict[Visitor, int]] = Field(default=None)
    completed: Optional[Dict[Visitor, int]] = Field(default=None)
    total_completed: Optional[int] = Field(default=None, alias="total_completed")
    unique_npcs_served: Optional[int] = Field(default=None, alias="unique_npcs_served")


class ComposterData(BaseModel):
    """
    Information about the Garden's composter.

    :param organic_matter: The amount of organic matter currently in the composter.
    :param fuel: The amount of fuel currently in the composter.
    :param compost_units: Either this or compost_items are the amount of compost in the composter, the other is unknown.
    :param compost_items: Either this or compost_units are the amount of compost in the composter, the other is unknown.
    :param conversion_ticks: Unknown.
    :param last_save: The timestamp the composter was last modified (eg; fuel put in, compost taken).
    :param upgrades: Upgrades levels for the composter.
    """

    model_config = ConfigDict(populate_by_name=True)
    organic_matter: Optional[float] = Field(default=None, alias="organic_matter")
    fuel: Optional[float] = Field(default=None, alias="fuel_units")
    compost_units: Optional[int] = Field(default=None, alias="compost_units")
    compost_items: Optional[int] = Field(default=None, alias="compost_items")
    conversion_ticks: Optional[int] = Field(default=None, alias="conversion_ticks")
    last_save: Optional[int] = Field(default=None, alias="last_save")
    upgrades: Optional[ComposterUpgrades] = None


class ComposterUpgrades(BaseModel):
    """
    Upgrade levels for the composter.

    :param speed: The speed upgrade of the composter.
    :param multi_drop: The multi drop upgrade of the composter.
    :param fuel_cap: The fuel cap upgrade of the composter.
    :param organic_matter_cap: The organic matter cap of the composter.
    :param cost_reduction: The cost reduction cap of the composter.
    """

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
