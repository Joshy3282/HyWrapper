from __future__ import annotations

from pydantic import Field

from hywrapper.models.hypixel_response import HypixelResponse


class PunishmentStatsResponse(HypixelResponse):
    watchdog_last_minute: int = Field(default=0, alias="watchdog_lastMinute")
    staff_rolling_daily: int = Field(default=0, alias="staff_rollingDaily")
    watchdog_total: int = Field(default=0, alias="watchdog_total")
    watchdog_rolling_daily: int = Field(default=0, alias="watchdog_rollingDaily")
    staff_total: int = Field(default=0, alias="staff_total")
