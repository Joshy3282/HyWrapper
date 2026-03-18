import asyncio
from typing import Optional, TypeVar

import httpx
from pydantic import BaseModel

from .models import (
    AchievementsResponse,
    AuctionsEndedResponse,
    AuctionsResponse,
    BazaarResponse,
    BingoResponse,
    BoostersResponse,
    ChallengesResponse,
    CollectionsResponse,
    CountsResponse,
    ElectionResponse,
    FiresalesResponse,
    GamesResponse,
    GardenResponse,
    GuildResponse,
    GuildsAchievementsResponse,
    HousingActiveResponse,
    HousingHouseResponse,
    ItemsResponse,
    LeaderboardsResponse,
    MuseumResponse,
    NewsResponse,
    OnlineResponse,
    PlayerResponse,
    ProfileResponse,
    PunishmentStatsResponse,
    QuestsResponse,
    RateLimit,
    RecentGamesResponse,
    SkillsResponse,
    VanityResponse,
)
from .uuid_utils import UuidUtils

T = TypeVar("T", bound=BaseModel)


class HypixelException(Exception):
    def __init__(self, message: str, code: Optional[int] = None):
        super().__init__(message)
        self.code = code


class InvalidApiKeyException(HypixelException):
    def __init__(self, message: str):
        super().__init__(message, 403)


class RateLimitException(HypixelException):
    def __init__(self, message: str, is_global: bool = False, retry_after: Optional[int] = None):
        super().__init__(message, 429)
        self.is_global = is_global
        self.retry_after = retry_after


class ResourceNotFoundException(HypixelException):
    def __init__(self, message: str):
        super().__init__(message, 404)


class MissingFieldException(HypixelException):
    def __init__(self, message: str):
        super().__init__(message, 400)


class InvalidDataException(HypixelException):
    def __init__(self, message: str):
        super().__init__(message, 422)


class DataNotPopulatedException(HypixelException):
    def __init__(self, message: str):
        super().__init__(message, 503)


class HypixelClient:
    def __init__(
        self,
        api_key: str,
        http_client: Optional[httpx.AsyncClient] = None,
        base_url: str = "https://api.hypixel.net/v2",
        default_cache_duration_minutes: int = 1,
        auto_retry: bool = False,
        max_retries: int = 3,
    ) -> None:
        self.api_key = api_key
        self.base_url = base_url
        self.default_cache_duration_minutes = default_cache_duration_minutes
        self.auto_retry = auto_retry
        self.max_retries = max_retries
        self.last_rate_limit: Optional[RateLimit] = None

        if http_client is None:
            self.internal_http_client = httpx.AsyncClient(timeout=30.0)
        else:
            self.internal_http_client = http_client

    async def close(self) -> None:
        await self.internal_http_client.aclose()

    async def get_player(self, uuid: str) -> PlayerResponse:
        return await self._fetch("/player", PlayerResponse, {"uuid": UuidUtils.undash(uuid)})

    async def get_recent_games(self, uuid: str) -> RecentGamesResponse:
        return await self._fetch(
            "/recentgames", RecentGamesResponse, {"uuid": UuidUtils.undash(uuid)}
        )

    async def get_status(self, uuid: str) -> OnlineResponse:
        return await self._fetch("/status", OnlineResponse, {"uuid": UuidUtils.undash(uuid)})

    async def get_guild_by_id(self, id: str) -> GuildResponse:
        return await self._fetch("/guild", GuildResponse, {"id": id})

    async def get_guild_by_player(self, uuid: str) -> GuildResponse:
        return await self._fetch("/guild", GuildResponse, {"player": UuidUtils.undash(uuid)})

    async def get_guild_by_name(self, name: str) -> GuildResponse:
        return await self._fetch("/guild", GuildResponse, {"name": name})

    async def get_housing_active(self) -> HousingActiveResponse:
        return await self._fetch("/housing/active", HousingActiveResponse)

    async def get_housing_house(self, house_uuid: str) -> HousingHouseResponse:
        return await self._fetch(
            "/housing/house", HousingHouseResponse, {"house": UuidUtils.undash(house_uuid)}
        )

    async def get_boosters(self) -> BoostersResponse:
        return await self._fetch("/boosters", BoostersResponse)

    async def get_counts(self) -> CountsResponse:
        return await self._fetch("/counts", CountsResponse)

    async def get_leaderboards(self) -> LeaderboardsResponse:
        return await self._fetch("/leaderboards", LeaderboardsResponse)

    async def get_punishment_stats(self) -> PunishmentStatsResponse:
        return await self._fetch("/punishmentstats", PunishmentStatsResponse)

    async def get_resource_games(self) -> GamesResponse:
        return await self._fetch("/resources/games", GamesResponse, authenticated=False)

    async def get_resource_achievements(self) -> AchievementsResponse:
        return await self._fetch(
            "/resources/achievements", AchievementsResponse, authenticated=False
        )

    async def get_resource_challenges(self) -> ChallengesResponse:
        return await self._fetch("/resources/challenges", ChallengesResponse, authenticated=False)

    async def get_resource_quests(self) -> QuestsResponse:
        return await self._fetch("/resources/quests", QuestsResponse, authenticated=False)

    async def get_resource_guild_achievements(self) -> GuildsAchievementsResponse:
        return await self._fetch(
            "/resources/guilds/achievements", GuildsAchievementsResponse, authenticated=False
        )

    async def get_resource_vanity_pets(self) -> VanityResponse:
        return await self._fetch("/resources/vanity/pets", VanityResponse, authenticated=False)

    async def get_resource_vanity_companions(self) -> VanityResponse:
        return await self._fetch(
            "/resources/vanity/companions", VanityResponse, authenticated=False
        )

    async def get_bingo(self) -> BingoResponse:
        return await self._fetch("/skyblock/bingo", BingoResponse)

    async def get_election(self) -> ElectionResponse:
        return await self._fetch("/skyblock/election", ElectionResponse)

    async def get_skyblock_news(self) -> NewsResponse:
        return await self._fetch("/skyblock/news", NewsResponse)

    async def get_skyblock_items(self) -> ItemsResponse:
        return await self._fetch("/resources/skyblock/items", ItemsResponse, authenticated=False)

    async def get_bazaar(self) -> BazaarResponse:
        return await self._fetch("/skyblock/bazaar", BazaarResponse)

    async def get_collections(self) -> CollectionsResponse:
        return await self._fetch(
            "/resources/skyblock/collections", CollectionsResponse, authenticated=False
        )

    async def get_auctions_ended(self) -> AuctionsEndedResponse:
        return await self._fetch("/skyblock/auctions_ended", AuctionsEndedResponse)

    async def get_auctions(self, page: int) -> AuctionsResponse:
        return await self._fetch("/skyblock/auctions", AuctionsResponse, {"page": str(page)})

    async def get_garden(self, profile_uuid: str) -> GardenResponse:
        return await self._fetch(
            "/skyblock/garden", GardenResponse, {"profile": UuidUtils.undash(profile_uuid)}
        )

    async def get_museum(self, profile_uuid: str) -> MuseumResponse:
        return await self._fetch(
            "/skyblock/museum", MuseumResponse, {"profile": UuidUtils.undash(profile_uuid)}
        )

    async def get_firesales(self) -> FiresalesResponse:
        return await self._fetch("/skyblock/firesales", FiresalesResponse)

    async def get_skyblock_skills(self) -> SkillsResponse:
        return await self._fetch("/resources/skyblock/skills", SkillsResponse, authenticated=False)

    async def get_profile(self, uuid: str) -> ProfileResponse:
        return await self._fetch(
            "/skyblock/profile", ProfileResponse, {"uuid": UuidUtils.undash(uuid)}
        )

    def _parse_rate_limit(self, headers: httpx.Headers) -> Optional[RateLimit]:
        try:
            limit = int(headers.get("RateLimit-Limit", ""))
            remaining = int(headers.get("RateLimit-Remaining", ""))
            reset = int(headers.get("RateLimit-Reset", ""))
            return RateLimit(limit=limit, remaining=remaining, reset=reset)
        except (ValueError, TypeError):
            return None

    async def _fetch(
        self,
        endpoint: str,
        response_model: type[T],
        query_params: Optional[dict[str, str]] = None,
        authenticated: bool = True,
    ) -> T:
        attempts = 0
        while True:
            url = f"{self.base_url}{endpoint}"
            headers = {"Accept": "application/json"}
            if authenticated:
                headers["API-Key"] = self.api_key

            try:
                response = await self.internal_http_client.get(
                    url, params=query_params, headers=headers
                )

                rate_limit = self._parse_rate_limit(response.headers)
                if rate_limit:
                    self.last_rate_limit = rate_limit

                if response.is_error:
                    error_data = response.json() if response.content else {}
                    cause = error_data.get("cause", f"HTTP Error: {response.status_code}")

                    if response.status_code == 400:
                        if "Missing" in cause:
                            raise MissingFieldException(cause)
                        else:
                            raise InvalidDataException(cause)
                    elif response.status_code == 403:
                        raise InvalidApiKeyException(cause)
                    elif response.status_code == 404:
                        raise ResourceNotFoundException(cause)
                    elif response.status_code == 422:
                        raise InvalidDataException(cause)
                    elif response.status_code == 429:
                        is_global = error_data.get("global", False)
                        retry_after = response.headers.get("Retry-After")
                        retry_after_val = (
                            int(retry_after) if retry_after and retry_after.isdigit() else None
                        )
                        raise RateLimitException(cause, is_global, retry_after_val)
                    elif response.status_code == 503:
                        raise DataNotPopulatedException(cause)
                    else:
                        raise HypixelException(cause, response.status_code)

                decoded = response.json()
                model = response_model.model_validate(decoded)

                if hasattr(model, "rateLimit"):
                    model.rateLimit = rate_limit

                success = getattr(model, "success", False)
                if not success:
                    cause = getattr(model, "cause", "Unknown error")
                    raise HypixelException(f"API Error: {cause}")

                return model

            except RateLimitException as e:
                if self.auto_retry and attempts < self.max_retries:
                    wait_time = e.retry_after or (
                        self.last_rate_limit.reset if self.last_rate_limit else 1
                    )
                    await asyncio.sleep(wait_time)
                    attempts += 1
                    continue
                raise e
            except httpx.HTTPError as e:
                raise HypixelException(f"Network error: {str(e)}") from e
            except Exception as e:
                if isinstance(e, HypixelException):
                    raise e
                raise HypixelException(f"Unexpected error: {str(e)}") from e
