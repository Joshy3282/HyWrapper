from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from hywrapper.models.rate_limit import RateLimit


class HypixelResponse(BaseModel):
    success: bool
    cause: Optional[str] = None
    rateLimit: Optional[RateLimit] = None
