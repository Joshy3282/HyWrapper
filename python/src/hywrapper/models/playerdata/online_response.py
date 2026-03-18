from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class OnlineResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    cause: Optional[str] = None
    uuid: str = Field(default="")
    session: Session
    rateLimit: Optional[RateLimit] = None


class Session(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    online: Optional[bool] = None
