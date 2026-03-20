from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.rate_limit import RateLimit


class HypixelResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    success: Optional[bool] = None
    cause: Optional[str] = None
    rateLimit: Optional[RateLimit] = Field(default=None)
