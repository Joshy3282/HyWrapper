from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from hywrapper.data.game_type import GameType
from hywrapper.models.hypixel_response import HypixelResponse
from hywrapper.models.rate_limit import RateLimit


class GuildResponse(HypixelResponse):
    model_config = ConfigDict(populate_by_name=True)
    success: bool = Field(default=False)
    cause: Optional[str] = None
    guild: Optional[Guild] = None
    rateLimit: Optional[RateLimit] = None


class Guild(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str = Field(default="")
    name: str = Field(default="")
    nameLower: str = Field(default="")
    coins: int = Field(default=0)
    coinsEver: int = Field(default=0)
    created: int = Field(default=0)
    members: List[Member] = Field(default=[])
    ranks: List[Rank] = Field(default=[])
    achievements: Dict[str, int] = Field(default={})
    exp: int = Field(default=0)
    tagColor: str = Field(default="")
    banner: Optional[Banner] = None
    publiclyListed: Optional[bool] = None
    preferredGames: List[str] = Field(default=[])
    description: str = Field(default="")
    chatMute: int = Field(default=0)
    tag: str = Field(default="")
    guildExpByGameType: Dict[str, int] = Field(default={})
    parsedPreferredGames: List[GameType]


class Member(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    uuid: str = Field(default="")
    rank: str = Field(default="")
    joined: int = Field(default=0)
    questParticipation: int = Field(default=0)
    mutedTill: int = Field(default=0)
    expHistory: Dict[str, int] = Field(default={})


class Rank(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: str = Field(default="")
    default: Optional[bool] = None
    tag: Optional[str] = None
    created: int = Field(default=0)
    priority: int = Field(default=0)


class Banner(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    base: str = Field(default="")
    patterns: List[Pattern] = Field(default=[])


class Pattern(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    pattern: str = Field(default="")
    color: str = Field(default="")
