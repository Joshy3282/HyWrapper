from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.rate_limit import RateLimit


class PunishmentStatsResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    cause: Optional[str] = None
    watchdogLastMinute: int = Field(default=0)
    staffRollingDaily: int = Field(default=0)
    watchdogTotal: int = Field(default=0)
    watchdogRollingDaily: int = Field(default=0)
    staffTotal: int = Field(default=0)
    rateLimit: Optional[RateLimit] = None
