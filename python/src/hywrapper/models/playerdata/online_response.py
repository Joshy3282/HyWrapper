from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict

from hywrapper.models.hypixel_response import HypixelResponse


class Session(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    online: Optional[bool] = None


class OnlineResponse(HypixelResponse):
    uuid: str = ""
    session: Session
