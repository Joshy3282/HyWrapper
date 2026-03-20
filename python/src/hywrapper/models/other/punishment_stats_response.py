from __future__ import annotations

from typing import Optional

from pydantic import Field

from hywrapper.models.hypixel_response import HypixelResponse


class PunishmentStatsResponse(HypixelResponse):
    watchdog_last_minute: Optional[int] = Field(default=None, alias="watchdog_lastMinute")
    staff_rolling_daily: Optional[int] = Field(default=None, alias="staff_rollingDaily")
    watchdog_total: Optional[int] = Field(default=None, alias="watchdog_total")
    watchdog_rolling_daily: Optional[int] = Field(default=None, alias="watchdog_rollingDaily")
    staff_total: Optional[int] = Field(default=None, alias="staff_total")
