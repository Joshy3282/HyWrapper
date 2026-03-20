from __future__ import annotations

from typing import List, Optional

from pydantic import ConfigDict

from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.skyblock.profile_response import Profile


class ProfilesResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    profiles: Optional[List[Profile]] = None
