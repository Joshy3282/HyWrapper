import axios, { AxiosInstance } from "axios";
import {
    DataNotPopulatedException,
    HypixelException,
    HypixelResponse,
    InvalidApiKeyException,
    InvalidDataException,
    MissingFieldException,
    RateLimit,
    RateLimitException,
    ResourceNotFoundException,
} from "./types";
import { UuidUtils } from "./utils/uuid_utils";
import {
    PlayerResponse,
    RecentGamesResponse,
    OnlineResponse,
    GuildResponse,
    GamesResponse,
    AchievementsResponse,
    ChallengesResponse,
    QuestsResponse,
    GuildsAchievementsResponse,
    VanityResponse,
    CollectionsResponse,
    SkillsResponse,
    ItemsResponse,
    ElectionResponse,
    BingoResponse,
    NewsResponse,
    AuctionsResponse,
    AuctionsEndedResponse,
    BazaarResponse,
    ProfileResponse,
    ProfilesResponse,
    MuseumResponse,
    GardenResponse,
    FiresalesResponse,
    HousingActiveResponse,
    HousingHouseResponse,
    HousingHousesResponse,
    BoostersResponse,
    CountsResponse,
    LeaderboardsResponse,
    PunishmentStatsResponse,
} from "./models";

export interface ClientOptions {
    api_key: string;
    base_url?: string;
    default_cache_duration_minutes?: number;
    auto_retry?: boolean;
    max_retries?: number;
    axios_instance?: AxiosInstance;
}

/**
 * A client for interacting with the Hypixel API.
 *
 * This client handles authentication, rate limiting, and automatic retries.
 * It uses Promises for asynchronous requests.
 *
 * @param options The client configuration options.
 */
export class HypixelClient {
    private readonly apiKey: string;
    private readonly baseUrl: string;
    private readonly defaultCacheDurationMinutes: number;
    private readonly autoRetry: boolean;
    private readonly maxRetries: number;
    private readonly axiosInstance: AxiosInstance;

    private _lastRateLimit: RateLimit | null = null;

    constructor(options: ClientOptions) {
        this.apiKey = options.api_key;
        this.baseUrl = options.base_url || "https://api.hypixel.net/v2";
        this.defaultCacheDurationMinutes = options.default_cache_duration_minutes ?? 1;
        this.autoRetry = options.auto_retry ?? false;
        this.maxRetries = options.max_retries ?? 3;

        this.axiosInstance = options.axios_instance || axios.create({
            baseURL: this.baseUrl,
            timeout: 30000,
            headers: {
                Accept: "application/json",
            },
        });
    }

    /**
     * The rate limit information from the last successful API request.
     */
    public get lastRateLimit(): RateLimit | null {
        return this._lastRateLimit;
    }

    /**
     * Retrieves data of a specific player, including game stats.
     * https://api.hypixel.net/v2/player
     *
     * @param uuid The UUID of the player.
     * @returns A {@link PlayerResponse} containing the player's data.
     * @throws HypixelException if the API returns an error.
     */
    public async getPlayer(uuid: string): Promise<PlayerResponse> {
        return this.fetch("/player", { uuid: UuidUtils.undash(uuid) });
    }

    /**
     * Retrieves the recently played games of a specific player.
     * https://api.hypixel.net/v2/recentgames
     *
     * @param uuid The UUID of the player.
     * @returns A {@link RecentGamesResponse} containing the recent games data.
     */
    public async getRecentGames(uuid: string): Promise<RecentGamesResponse> {
        return this.fetch("/recentgames", { uuid: UuidUtils.undash(uuid) });
    }

    /**
     * Retrieves the current online status of a specific player.
     * https://api.hypixel.net/v2/status
     *
     * @param uuid The UUID of the player.
     * @returns An {@link OnlineResponse} containing the player's online status.
     */
    public async getStatus(uuid: string): Promise<OnlineResponse> {
        return this.fetch("/status", { uuid: UuidUtils.undash(uuid) });
    }

    /**
     * Retrieves a guild by an id.
     * https://api.hypixel.net/v2/guild
     *
     * @param id The ID of the guild.
     * @returns A {@link GuildResponse} containing the guild's data.
     */
    public async getGuildById(id: string): Promise<GuildResponse> {
        return this.fetch("/guild", { id });
    }

    /**
     * Retrieves a guild by a player.
     * https://api.hypixel.net/v2/guild
     *
     * @param uuid The UUID of the player.
     * @returns A {@link GuildResponse} containing the guild's data.
     */
    public async getGuildByPlayer(uuid: string): Promise<GuildResponse> {
        return this.fetch("/guild", { player: UuidUtils.undash(uuid) });
    }

    /**
     * Retrieves a guild by a name.
     * https://api.hypixel.net/v2/guild
     *
     * @param name The name of the guild.
     * @returns A {@link GuildResponse} containing the guild's data.
     */
    public async getGuildByName(name: string): Promise<GuildResponse> {
        return this.fetch("/guild", { name });
    }

    /**
     * Retrieves current player counts across all games.
     * https://api.hypixel.net/v2/counts
     *
     * @returns A {@link CountsResponse} containing the player counts.
     */
    public async getCounts(): Promise<CountsResponse> {
        return this.fetch("/counts");
    }

    /**
     * Retrieves current boosters.
     * https://api.hypixel.net/v2/boosters
     *
     * @returns A {@link BoostersResponse} containing the boosters.
     */
    public async getBoosters(): Promise<BoostersResponse> {
        return this.fetch("/boosters");
    }

    /**
     * Retrieves current leaderboards.
     * https://api.hypixel.net/v2/leaderboards
     *
     * @returns A {@link LeaderboardsResponse} containing the leaderboards.
     */
    public async getLeaderboards(): Promise<LeaderboardsResponse> {
        return this.fetch("/leaderboards");
    }

    /**
     * Retrieves punishment statistics.
     * https://api.hypixel.net/v2/punishmentstats
     *
     * @returns A {@link PunishmentStatsResponse} containing the punishment statistics.
     */
    public async getPunishmentStats(): Promise<PunishmentStatsResponse> {
        return this.fetch("/punishmentstats");
    }

    /**
     * Retrieves the list of games.
     * https://api.hypixel.net/v2/resources/games
     *
     * @returns A {@link GamesResponse} containing the list of games.
     */
    public async getGames(): Promise<GamesResponse> {
        return this.fetch("/resources/games", {}, false);
    }

    /**
     * Retrieves the list of achievements.
     * https://api.hypixel.net/v2/resources/achievements
     *
     * @returns An {@link AchievementsResponse} containing the list of achievements.
     */
    public async getAchievements(): Promise<AchievementsResponse> {
        return this.fetch("/resources/achievements", {}, false);
    }

    /**
     * Retrieves the list of challenges.
     * https://api.hypixel.net/v2/resources/challenges
     *
     * @returns A {@link ChallengesResponse} containing the list of challenges.
     */
    public async getChallenges(): Promise<ChallengesResponse> {
        return this.fetch("/resources/challenges", {}, false);
    }

    /**
     * Retrieves the list of quests.
     * https://api.hypixel.net/v2/resources/quests
     *
     * @returns A {@link QuestsResponse} containing the list of quests.
     */
    public async getQuests(): Promise<QuestsResponse> {
        return this.fetch("/resources/quests", {}, false);
    }

    /**
     * Retrieves the list of guild achievements.
     * https://api.hypixel.net/v2/resources/guilds/achievements
     *
     * @returns A {@link GuildsAchievementsResponse} containing the list of guild achievements.
     */
    public async getGuildAchievements(): Promise<GuildsAchievementsResponse> {
        return this.fetch("/resources/guilds/achievements", {}, false);
    }

    /**
     * Retrieves the list of vanity pets.
     * https://api.hypixel.net/v2/resources/vanity/pets
     *
     * @returns A {@link VanityResponse} containing the list of vanity pets.
     */
    public async getVanityPets(): Promise<VanityResponse> {
        return this.fetch("/resources/vanity/pets", {}, false);
    }

    /**
     * Retrieves the list of vanity companions.
     * https://api.hypixel.net/v2/resources/vanity/companions
     *
     * @returns A {@link VanityResponse} containing the list of vanity companions.
     */
    public async getVanityCompanions(): Promise<VanityResponse> {
        return this.fetch("/resources/vanity/companions", {}, false);
    }

    /**
     * Retrieves the current SkyBlock election information.
     * https://api.hypixel.net/v2/resources/skyblock/election
     *
     * @returns An {@link ElectionResponse} containing the election information.
     */
    public async getSkyBlockElection(): Promise<ElectionResponse> {
        return this.fetch("/resources/skyblock/election", {}, false);
    }

    /**
     * Retrieves the list of SkyBlock items.
     * https://api.hypixel.net/v2/resources/skyblock/items
     *
     * @returns An {@link ItemsResponse} containing the list of items.
     */
    public async getSkyBlockItems(): Promise<ItemsResponse> {
        return this.fetch("/resources/skyblock/items", {}, false);
    }

    /**
     * Retrieves the list of SkyBlock collections.
     * https://api.hypixel.net/v2/resources/skyblock/collections
     *
     * @returns A {@link CollectionsResponse} containing the list of collections.
     */
    public async getSkyBlockCollections(): Promise<CollectionsResponse> {
        return this.fetch("/resources/skyblock/collections", {}, false);
    }

    /**
     * Retrieves SkyBlock skills information.
     * https://api.hypixel.net/v2/resources/skyblock/skills
     *
     * @returns A {@link SkillsResponse} containing the skills information.
     */
    public async getSkyBlockSkills(): Promise<SkillsResponse> {
        return this.fetch("/resources/skyblock/skills", {}, false);
    }

    /**
     * Retrieves the current SkyBlock bingo information.
     * https://api.hypixel.net/v2/resources/skyblock/bingo
     */
    public async getBingo(): Promise<BingoResponse> {
        return this.fetch("/skyblock/bingo", {}, false);
    }

    /**
     * Retrieves SkyBlock news.
     * https://api.hypixel.net/v2/skyblock/news
     */
    public async getNews(): Promise<NewsResponse> {
        return this.fetch("/skyblock/news");
    }

    /**
     * Searches for SkyBlock auctions by UUID, player, or profile.
     * https://api.hypixel.net/v2/skyblock/auction
     *
     * @param uuid The auction UUID.
     * @param player The player UUID.
     * @param profile The profile UUID.
     */
    public async getAuction(uuid?: string, player?: string, profile?: string): Promise<AuctionsResponse> {
        const params: Record<string, string> = {};
        if (uuid) params.uuid = UuidUtils.undash(uuid);
        if (player) params.player = UuidUtils.undash(player);
        if (profile) params.profile = UuidUtils.undash(profile);
        return this.fetch("/skyblock/auction", params);
    }

    /**
     * Retrieves active SkyBlock auctions.
     * https://api.hypixel.net/v2/skyblock/auctions
     *
     * @param page The page number to get.
     */
    public async getAuctions(page = 0): Promise<AuctionsResponse> {
        return this.fetch("/skyblock/auctions", { page: page.toString() }, false);
    }

    /**
     * Retrieves recently ended SkyBlock auctions.
     * https://api.hypixel.net/v2/skyblock/auctions_ended
     */
    public async getAuctionsEnded(): Promise<AuctionsEndedResponse> {
        return this.fetch("/skyblock/auctions_ended", {}, false);
    }

    /**
     * Retrieves current bazaar data.
     * https://api.hypixel.net/v2/skyblock/bazaar
     */
    public async getBazaar(): Promise<BazaarResponse> {
        return this.fetch("/skyblock/bazaar", {}, false);
    }

    /**
     * Retrieves a specific SkyBlock profile by its UUID.
     * https://api.hypixel.net/v2/skyblock/profile
     *
     * @param uuid The UUID of the profile.
     */
    public async getProfile(uuid: string): Promise<ProfileResponse> {
        return this.fetch("/skyblock/profile", { profile: UuidUtils.undash(uuid) });
    }

    /**
     * Retrieves all SkyBlock profiles for a player.
     * https://api.hypixel.net/v2/skyblock/profiles
     *
     * @param uuid The UUID of the player.
     */
    public async getProfiles(uuid: string): Promise<ProfilesResponse> {
        return this.fetch("/skyblock/profiles", { uuid: UuidUtils.undash(uuid) });
    }

    /**
     * Retrieves SkyBlock museum information for a profile.
     * https://api.hypixel.net/v2/skyblock/museum
     *
     * @param profileUuid The UUID of the SkyBlock profile.
     */
    public async getMuseum(profileUuid: string): Promise<MuseumResponse> {
        return this.fetch("/skyblock/museum", { profile: UuidUtils.undash(profileUuid) });
    }

    /**
     * Retrieves SkyBlock garden information for a profile.
     * https://api.hypixel.net/v2/skyblock/garden
     *
     * @param profileUuid The UUID of the SkyBlock profile.
     */
    public async getGarden(profileUuid: string): Promise<GardenResponse> {
        return this.fetch("/skyblock/garden", { profile: UuidUtils.undash(profileUuid) });
    }

    /**
     * Retrieves SkyBlock bingo data for a player.
     * https://api.hypixel.net/v2/skyblock/bingo
     *
     * @param uuid The UUID of the player.
     */
    public async getPlayerBingo(uuid: string): Promise<BingoResponse> {
        return this.fetch("/skyblock/bingo", { uuid: UuidUtils.undash(uuid) });
    }

    /**
     * Retrieves current SkyBlock fire sales.
     * https://api.hypixel.net/v2/skyblock/firesales
     */
    public async getFiresales(): Promise<FiresalesResponse> {
        return this.fetch("/skyblock/firesales", {}, false);
    }

    /**
     * Retrieves the currently active housing.
     * https://api.hypixel.net/v2/housing/active
     */
    public async getHousingActive(): Promise<HousingActiveResponse> {
        return this.fetch("/housing/active");
    }

    /**
     * Retrieves information about a specific housing instance.
     * https://api.hypixel.net/v2/housing/house
     *
     * @param houseUuid The UUID of the housing instance.
     */
    public async getHousingHouse(houseUuid: string): Promise<HousingHouseResponse> {
        return this.fetch("/housing/house", { house: UuidUtils.undash(houseUuid) });
    }

    /**
     * Retrieves the housing instances owned by a player.
     * https://api.hypixel.net/v2/housing/houses
     *
     * @param uuid The UUID of the player.
     */
    public async getHousingHouses(uuid: string): Promise<HousingHousesResponse> {
        return this.fetch("/housing/houses", { player: UuidUtils.undash(uuid) });
    }

    private async fetch<T extends HypixelResponse>(
        endpoint: string,
        params: Record<string, string> = {},
        authenticated: boolean = true,
    ): Promise<T> {
        let attempts = 0;

        // eslint-disable-next-line no-constant-condition
        while (true) {
            const headers: Record<string, string> = {};
            if (authenticated) {
                headers["API-Key"] = this.apiKey;
            }

            try {
                const response = await this.axiosInstance.get<T>(endpoint, {
                    params,
                    headers,
                });

                if (response.status >= 200 && response.status < 300 && this.defaultCacheDurationMinutes > 0) {
                    response.headers["Cache-Control"] = `public, max-age=${this.defaultCacheDurationMinutes * 60}`;
                }

                const rateLimit = this.parseRateLimit(response.headers);
                if (rateLimit) {
                    this._lastRateLimit = rateLimit;
                }

                const data = response.data;
                data.rateLimit = rateLimit ?? undefined;

                if (!data.success) {
                    throw new HypixelException(`API Error: ${data.cause || "Unknown error"}`);
                }

                return data;
            } catch (error: any) {
                if (axios.isAxiosError(error) && error.response) {
                    const response = error.response;
                    const rateLimit = this.parseRateLimit(response.headers);
                    if (rateLimit) {
                        this._lastRateLimit = rateLimit;
                    }

                    const cause = response.data?.cause || `HTTP Error: ${response.status}`;
                    let exception: HypixelException;

                    switch (response.status) {
                        case 400:
                            exception = cause.toLowerCase().includes("missing")
                                ? new MissingFieldException(cause)
                                : new InvalidDataException(cause);
                            break;
                        case 403:
                            exception = new InvalidApiKeyException(cause);
                            break;
                        case 404:
                            exception = new ResourceNotFoundException(cause);
                            break;
                        case 422:
                            exception = new InvalidDataException(cause);
                            break;
                        case 429: {
                            const isGlobal = response.data?.global ?? false;
                            const retryAfter = response.headers["retry-after"]
                                ? parseInt(response.headers["retry-after"])
                                : undefined;
                            exception = new RateLimitException(cause, isGlobal, retryAfter);
                            break;
                        }
                        case 502:
                            exception = new HypixelException(cause, 502);
                            break;
                        case 503:
                            exception = new DataNotPopulatedException(cause);
                            break;
                        default:
                            exception = new HypixelException(cause, response.status);
                    }

                    if (exception instanceof RateLimitException && this.autoRetry && attempts < this.maxRetries) {
                        const waitTime =
                            exception.retryAfter ?? (this._lastRateLimit?.reset ? this._lastRateLimit.reset : 1);
                        await new Promise((resolve) => setTimeout(resolve, waitTime * 1000));
                        attempts++;
                        continue;
                    }

                    throw exception;
                }

                if (error instanceof HypixelException) {
                    throw error;
                }

                throw new HypixelException(`Unexpected error: ${error.message}`);
            }
        }
    }

    private parseRateLimit(headers: any): RateLimit | null {
        const limit = parseInt(headers["ratelimit-limit"]);
        const remaining = parseInt(headers["ratelimit-remaining"]);
        const reset = parseInt(headers["ratelimit-reset"]);

        if (isNaN(limit) || isNaN(remaining) || isNaN(reset)) {
            return null;
        }

        return { limit, remaining, reset };
    }
}
