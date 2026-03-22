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
    HousingHousesResponse,
    ItemsResponse,
    LeaderboardsResponse,
    MuseumResponse,
    NewsResponse,
    OnlineResponse,
    PlayerResponse,
    ProfileResponse,
    ProfilesResponse,
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
    """
    Base exception for all Hypixel API related errors.

    :param message: The error message.
    :param code: The HTTP status code associated with the error, if available.
    """

    def __init__(self, message: str, code: Optional[int] = None):
        super().__init__(message)
        self.code = code


class InvalidApiKeyException(HypixelException):
    """
    Thrown when the provided API key is invalid
    """

    def __init__(self, message: str):
        super().__init__(message, 403)


class RateLimitException(HypixelException):
    """
    Thrown when the API rate limit has been exceeded.

    :param message: The error message.
    :param is_global: Whether the rate limit was triggered by the global throttle.
    :param retry_after: The number of seconds to wait before retrying
    """

    def __init__(self, message: str, is_global: bool = False, retry_after: Optional[int] = None):
        super().__init__(message, 429)
        self.is_global = is_global
        self.retry_after = retry_after


class ResourceNotFoundException(HypixelException):
    """
    Thrown when the requested resource was not found.
    """

    def __init__(self, message: str):
        super().__init__(message, 404)


class MissingFieldException(HypixelException):
    """
    Thrown when a required field is missing from the request.
    """

    def __init__(self, message: str):
        super().__init__(message, 400)


class InvalidDataException(HypixelException):
    """
    Thrown when the provided data is invalid.
    """

    def __init__(self, message: str):
        super().__init__(message, 422)


class DataNotPopulatedException(HypixelException):
    """
    Thrown when the requested data has not been populated yet (e.g bazaar, auctions)
    This does not seem to happen any more and is only a thing for new endpoints
    """

    def __init__(self, message: str):
        super().__init__(message, 503)


class HypixelClient:
    """
    A client for interacting with the Hypixel API.

    This client handles authentication, rate limiting, and automatic retries.
    It uses asyncio for asynchronous requests.

    :param api_key: The Hypixel API key.
    :param http_client: The httpx.AsyncClient instance to use for requests.
    :param base_url: The base URL for the Hypixel API.
    :param default_cache_duration_minutes: The duration for which successful responses should be cached.
    :param auto_retry: Whether to automatically retry requests that fail due to rate limiting.
    :param max_retries: The maximum number of retries for rate-limited requests.
    """

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
        """
        Retrieves data of a specific player, including game stats.
        https://api.hypixel.net/v2/player

        :param uuid: The UUID of the player.
        :return: A PlayerResponse containing the player's data.
        :raises HypixelException: if the API returns an error.
        """
        return await self._fetch("/player", PlayerResponse, {"uuid": UuidUtils.undash(uuid)})

    async def get_recent_games(self, uuid: str) -> RecentGamesResponse:
        """
        Retrieves the recently played games of a specific player.
        https://api.hypixel.net/v2/recentgames

        :param uuid: The UUID of the player.
        :return: A RecentGamesResponse containing the recent games data.
        """
        return await self._fetch(
            "/recentgames", RecentGamesResponse, {"uuid": UuidUtils.undash(uuid)}
        )

    async def get_status(self, uuid: str) -> OnlineResponse:
        """
        Retrieves the current online status of a specific player.
        https://api.hypixel.net/v2/status

        :param uuid: The UUID of the player.
        :return: An OnlineResponse containing the player's online status.
        """
        return await self._fetch("/status", OnlineResponse, {"uuid": UuidUtils.undash(uuid)})

    async def get_guild_by_id(self, id: str) -> GuildResponse:
        """
        Retrieves a guild by an id.
        https://api.hypixel.net/v2/guild

        :param id: The ID of the guild.
        :return: A GuildResponse containing the guild's data.
        """
        return await self._fetch("/guild", GuildResponse, {"id": id})

    async def get_guild_by_player(self, uuid: str) -> GuildResponse:
        """
        Retrieves a guild by a player.
        https://api.hypixel.net/v2/guild

        :param uuid: The UUID of the player.
        :return: A GuildResponse containing the guild's data.
        """
        return await self._fetch("/guild", GuildResponse, {"player": UuidUtils.undash(uuid)})

    async def get_guild_by_name(self, name: str) -> GuildResponse:
        """
        Retrieves a guild by a name.
        https://api.hypixel.net/v2/guild

        :param name: The name of the guild.
        :return: A GuildResponse containing the guild's data.
        """
        return await self._fetch("/guild", GuildResponse, {"name": name})

    async def get_housing_active(self) -> HousingActiveResponse:
        """
        Retrieves the currently active housing.
        https://api.hypixel.net/v2/housing/active
        """
        return await self._fetch("/housing/active", HousingActiveResponse)

    async def get_housing_houses(self, uuid: str) -> HousingHousesResponse:
        """
        Retrieves the housing instances owned by a player.
        https://api.hypixel.net/v2/housing/houses

        :param uuid: The UUID of the player.
        """
        return await self._fetch(
            "/housing/houses", HousingHousesResponse, {"player": UuidUtils.undash(uuid)}
        )

    async def get_housing_house(self, house_uuid: str) -> HousingHouseResponse:
        """
        Retrieves information about a specific housing instance.
        https://api.hypixel.net/v2/housing/house

        :param house_uuid: The UUID of the housing instance.
        """
        return await self._fetch(
            "/housing/house", HousingHouseResponse, {"house": UuidUtils.undash(house_uuid)}
        )

    async def get_boosters(self) -> BoostersResponse:
        """
        Retrieves the current boosters.
        https://api.hypixel.net/v2/boosters
        """
        return await self._fetch("/boosters", BoostersResponse)

    async def get_counts(self) -> CountsResponse:
        """
        Retrieves the player counts across various games.
        https://api.hypixel.net/v2/counts
        """
        return await self._fetch("/counts", CountsResponse)

    async def get_leaderboards(self) -> LeaderboardsResponse:
        """
        Retrieves the current leaderboards.
        https://api.hypixel.net/v2/leaderboards
        """
        return await self._fetch("/leaderboards", LeaderboardsResponse)

    async def get_punishment_stats(self) -> PunishmentStatsResponse:
        """
        Retrieves punishment statistics.
        https://api.hypixel.net/v2/punishmentstats
        """
        return await self._fetch("/punishmentstats", PunishmentStatsResponse)

    async def get_resource_games(self) -> GamesResponse:
        """
        Retrieves the list of games.
        https://api.hypixel.net/v2/resources/games
        """
        return await self._fetch("/resources/games", GamesResponse, authenticated=False)

    async def get_resource_achievements(self) -> AchievementsResponse:
        """
        Retrieves the list of achievements.
        https://api.hypixel.net/v2/resources/achievements
        """
        return await self._fetch(
            "/resources/achievements", AchievementsResponse, authenticated=False
        )

    async def get_resource_challenges(self) -> ChallengesResponse:
        """
        Retrieves the list of challenges.
        https://api.hypixel.net/v2/resources/challenges
        """
        return await self._fetch("/resources/challenges", ChallengesResponse, authenticated=False)

    async def get_resource_quests(self) -> QuestsResponse:
        """
        Retrieves the list of quests.
        https://api.hypixel.net/v2/resources/challenges
        """
        return await self._fetch("/resources/quests", QuestsResponse, authenticated=False)

    async def get_resource_guild_achievements(self) -> GuildsAchievementsResponse:
        """
        Retrieves the list of guild achievements.
        https://api.hypixel.net/v2/resources/guilds/achievements
        """
        return await self._fetch(
            "/resources/guilds/achievements", GuildsAchievementsResponse, authenticated=False
        )

    async def get_resource_vanity_pets(self) -> VanityResponse:
        """
        Retrieves the list of vanity pets.
        https://api.hypixel.net/v2/resources/vanity/pets
        """
        return await self._fetch("/resources/vanity/pets", VanityResponse, authenticated=False)

    async def get_resource_vanity_companions(self) -> VanityResponse:
        """
        Retrieves the list of vanity companions.
        https://api.hypixel.net/v2/resources/vanity/companions
        """
        return await self._fetch(
            "/resources/vanity/companions", VanityResponse, authenticated=False
        )

    async def get_bingo(self) -> BingoResponse:
        """
        Retrieves the current SkyBlock bingo information.
        https://api.hypixel.net/v2/resources/skyblock/bingo
        """
        return await self._fetch("/skyblock/bingo", BingoResponse)

    async def get_election(self) -> ElectionResponse:
        """
        Retrieves the current SkyBlock election information.
        https://api.hypixel.net/v2/resources/skyblock/election
        """
        return await self._fetch("/skyblock/election", ElectionResponse, authenticated=False)

    async def get_skyblock_news(self) -> NewsResponse:
        """
        Retrieves SkyBlock news.
        https://api.hypixel.net/v2/skyblock/news
        """
        return await self._fetch("/skyblock/news", NewsResponse)

    async def get_skyblock_items(self) -> ItemsResponse:
        """
        Retrieves the list of SkyBlock items.
        https://api.hypixel.net/v2/resources/skyblock/items
        """
        return await self._fetch("/resources/skyblock/items", ItemsResponse, authenticated=False)

    async def get_bazaar(self) -> BazaarResponse:
        """
        Retrieves current bazaar data.
        https://api.hypixel.net/v2/skyblock/bazaar
        """
        return await self._fetch("/skyblock/bazaar", BazaarResponse, authenticated=False)

    async def get_collections(self) -> CollectionsResponse:
        """
        Retrieves the list of SkyBlock collections.
        https://api.hypixel.net/v2/resources/skyblock/collections
        """
        return await self._fetch(
            "/resources/skyblock/collections", CollectionsResponse, authenticated=False
        )

    async def get_auctions_ended(self) -> AuctionsEndedResponse:
        """
        Retrieves recently ended SkyBlock auctions.
        https://api.hypixel.net/v2/skyblock/auctions_ended
        """
        return await self._fetch(
            "/skyblock/auctions_ended", AuctionsEndedResponse, authenticated=False
        )

    async def get_auctions(self, page: int = 0) -> AuctionsResponse:
        """
        Retrieves active SkyBlock auctions.
        https://api.hypixel.net/v2/skyblock/auctions

        :param page: The page number to get.
        """
        return await self._fetch(
            "/skyblock/auctions", AuctionsResponse, {"page": str(page)}, authenticated=False
        )

    async def get_garden(self, profile_uuid: str) -> GardenResponse:
        """
        Retrieves SkyBlock garden information for a profile.
        https://api.hypixel.net/v2/skyblock/garden

        :param profile_uuid: The UUID of the SkyBlock profile.
        """
        return await self._fetch(
            "/skyblock/garden", GardenResponse, {"profile": UuidUtils.undash(profile_uuid)}
        )

    async def get_museum(self, profile_uuid: str) -> MuseumResponse:
        """
        Retrieves SkyBlock museum information for a profile.
        https://api.hypixel.net/v2/skyblock/museum

        :param profile_uuid: The UUID of the SkyBlock profile.
        """
        return await self._fetch(
            "/skyblock/museum", MuseumResponse, {"profile": UuidUtils.undash(profile_uuid)}
        )

    async def get_firesales(self) -> FiresalesResponse:
        """
        Retrieves current SkyBlock fire sales.
        https://api.hypixel.net/v2/skyblock/firesales
        """
        return await self._fetch("/skyblock/firesales", FiresalesResponse, authenticated=False)

    async def get_skyblock_skills(self) -> SkillsResponse:
        """
        Retrieves SkyBlock skills information.
        https://api.hypixel.net/v2/resources/skyblock/skills
        """
        return await self._fetch("/resources/skyblock/skills", SkillsResponse, authenticated=False)

    async def get_profiles(self, uuid: str) -> ProfilesResponse:
        """
        Retrieves all SkyBlock profiles for a player.
        https://api.hypixel.net/v2/skyblock/profiles

        :param uuid: The UUID of the player.
        """
        return await self._fetch(
            "/skyblock/profiles", ProfilesResponse, {"uuid": UuidUtils.undash(uuid)}
        )

    async def get_player_bingo(self, uuid: str) -> BingoResponse:
        """
        Retrieves SkyBlock bingo data for a player.
        https://api.hypixel.net/v2/skyblock/bingo

        :param uuid: The UUID of the player.
        """
        return await self._fetch("/skyblock/bingo", BingoResponse, {"uuid": UuidUtils.undash(uuid)})

    async def get_auction(
        self,
        uuid: Optional[str] = None,
        player: Optional[str] = None,
        profile: Optional[str] = None,
    ) -> AuctionsResponse:
        """
        Searches for SkyBlock auctions by UUID, player, or profile.
        https://api.hypixel.net/v2/skyblock/auction

        :param uuid: The auction UUID.
        :param player: The player UUID.
        :param profile: The profile UUID.
        """
        params = {}
        if uuid:
            params["uuid"] = UuidUtils.undash(uuid)
        if player:
            params["player"] = UuidUtils.undash(player)
        if profile:
            params["profile"] = UuidUtils.undash(profile)
        return await self._fetch("/skyblock/auction", AuctionsResponse, params)

    async def get_profile(self, uuid: str) -> ProfileResponse:
        """
        Retrieves a specific SkyBlock profile by its UUID.
        https://api.hypixel.net/v2/skyblock/profile

        :param uuid: The UUID of the profile.
        """
        return await self._fetch(
            "/skyblock/profile", ProfileResponse, {"profile": UuidUtils.undash(uuid)}
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
                    elif response.status_code == 502:
                        raise HypixelException(cause, 502)
                    elif response.status_code == 503:
                        raise DataNotPopulatedException(cause)
                    else:
                        raise HypixelException(cause, response.status_code)

                decoded = response.json()
                model = response_model.model_validate(decoded)

                if hasattr(model, "rate_limit"):
                    model.rate_limit = rate_limit

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
