from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class RateLimit(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    limit: int
    remaining: int
    reset: int
