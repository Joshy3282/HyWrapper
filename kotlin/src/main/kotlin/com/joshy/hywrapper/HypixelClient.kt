package com.joshy.hywrapper

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import com.joshy.hywrapper.model.housing.HousingActiveResponse
import com.joshy.hywrapper.model.housing.HousingHouseResponse
import com.joshy.hywrapper.model.housing.HousingHousesResponse
import com.joshy.hywrapper.model.other.BoostersResponse
import com.joshy.hywrapper.model.other.CountsResponse
import com.joshy.hywrapper.model.other.LeaderboardsResponse
import com.joshy.hywrapper.model.other.PunishmentStatsResponse
import com.joshy.hywrapper.model.parseRateLimit
import com.joshy.hywrapper.model.playerdata.GuildResponse
import com.joshy.hywrapper.model.playerdata.OnlineResponse
import com.joshy.hywrapper.model.playerdata.PlayerResponse
import com.joshy.hywrapper.model.playerdata.RecentGamesResponse
import com.joshy.hywrapper.model.resources.*
import com.joshy.hywrapper.model.skyblock.*
import com.joshy.hywrapper.util.UuidUtils
import kotlinx.coroutines.delay
import kotlinx.coroutines.suspendCancellableCoroutine
import kotlinx.serialization.json.Json
import kotlinx.serialization.json.boolean
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive
import okhttp3.*
import okhttp3.HttpUrl.Companion.toHttpUrl
import java.io.IOException
import kotlin.coroutines.resume
import kotlin.coroutines.resumeWithException

/**
 * Base exception for all Hypixel API related errors.
 *
 * @property code The HTTP status code associated with the error, if available.
 */
open class HypixelException(message: String, val code: Int? = null) : Exception(message)

/**
 * Thrown when the provided API key is invalid
 */
class InvalidApiKeyException(message: String) : HypixelException(message, 403)

/**
 * Thrown when the API rate limit has been exceeded.
 *
 * @property isGlobal Whether the rate limit was triggered by the global throttle.
 * @property retryAfter The number of seconds to wait before retrying
 */
class RateLimitException(message: String, val isGlobal: Boolean = false, val retryAfter: Long? = null) :
    HypixelException(message, 429)

/**
 * Thrown when the requested resource was not found.
 */
class ResourceNotFoundException(message: String) : HypixelException(message, 404)

/**
 * Thrown when a required field is missing from the request.
 */
class MissingFieldException(message: String) : HypixelException(message, 400)

/**
 * Thrown when the provided data is invalid.
 */
class InvalidDataException(message: String) : HypixelException(message, 422)

/**
 * Thrown when the requested data has not been populated yet (e.g bazaar, auctions)
 * This does not seem to happen any more and is only a thing for new endpoints
 */
class DataNotPopulatedException(message: String) : HypixelException(message, 503)

/**
 * A client for interacting with the Hypixel API.
 *
 * This client handles authentication, rate limiting, and automatic retries.
 * It uses Coroutines for asynchronous requests.
 *
 * @param apiKey The Hypixel API key.
 * @param httpClient The [OkHttpClient] instance to use for requests.
 * @param baseUrl The base URL for the Hypixel API.
 * @param defaultCacheDurationMinutes The duration for which successful responses should be cached.
 * @param autoRetry Whether to automatically retry requests that fail due to rate limiting.
 * @param maxRetries The maximum number of retries for rate-limited requests.
 */
class HypixelClient(
    private val apiKey: String,
    httpClient: OkHttpClient = OkHttpClient(),
    private val baseUrl: String = "https://api.hypixel.net/v2",
    private val defaultCacheDurationMinutes: Int = 1,
    private val autoRetry: Boolean = false,
    private val maxRetries: Int = 3,
) {
    private val internalHttpClient: OkHttpClient =
        httpClient.newBuilder()
            .addNetworkInterceptor { chain ->
                val response = chain.proceed(chain.request())
                if (response.isSuccessful && defaultCacheDurationMinutes > 0) {
                    response.newBuilder()
                        .header("Cache-Control", "public, max-age=${defaultCacheDurationMinutes * 60}")
                        .build()
                } else {
                    response
                }
            }
            .build()

    private val json =
        Json {
            ignoreUnknownKeys = true
            isLenient = true
            encodeDefaults = true
            decodeEnumsCaseInsensitive = true
        }

    /**
     * The rate limit information from the last successful API request.
     */
    @Volatile
    var lastRateLimit: RateLimit? = null
        private set

    /**
     * Retrieves data of a specific player, including game stats.
     * https://api.hypixel.net/v2/player
     *
     * @param uuid The UUID of the player.
     * @return A [PlayerResponse] containing the player's data.
     * @throws HypixelException if the API returns an error.
     */
    suspend fun getPlayer(uuid: String): PlayerResponse =
        fetch(
            "/player",
            mapOf("uuid" to UuidUtils.undash(uuid)),
        )

    /**
     * Retrieves the recently played games of a specific player.
     * https://api.hypixel.net/v2/recentgames
     *
     * @param uuid The UUID of the player.
     * @return A [RecentGamesResponse] containing the recent games data.
     */
    suspend fun getRecentGames(uuid: String): RecentGamesResponse =
        fetch(
            "/recentgames",
            mapOf("uuid" to UuidUtils.undash(uuid)),
        )

    /**
     * Retrieves the current online status of a specific player.
     * https://api.hypixel.net/v2/status
     *
     * @param uuid The UUID of the player.
     * @return An [OnlineResponse] containing the player's online status.
     */
    suspend fun getStatus(uuid: String): OnlineResponse =
        fetch(
            "/status",
            mapOf("uuid" to UuidUtils.undash(uuid)),
        )

    /**
     * Retrieves a guild by an id.
     * https://api.hypixel.net/v2/guild
     *
     * @param id The ID of the guild.
     * @return A [GuildResponse] containing the guild's data.
     */
    suspend fun getGuildById(id: String): GuildResponse =
        fetch(
            "/guild",
            mapOf("id" to id),
        )

    /**
     * Retrieves a guild by a player.
     * https://api.hypixel.net/v2/guild
     *
     * @param uuid The UUID of the player.
     * @return A [GuildResponse] containing the guild's data.
     */
    suspend fun getGuildByPlayer(uuid: String): GuildResponse =
        fetch(
            "/guild",
            mapOf("player" to UuidUtils.undash(uuid)),
        )

    /**
     * Retrieves a guild by a name.
     * https://api.hypixel.net/v2/guild
     *
     * @param name The name of the guild.
     * @return A [GuildResponse] containing the guild's data.
     */
    suspend fun getGuildByName(name: String): GuildResponse =
        fetch(
            "/guild",
            mapOf("name" to name),
        )

    /**
     * Retrieves the list of games.
     * https://api.hypixel.net/v2/resources/games
     */
    suspend fun getGames(): GamesResponse =
        fetch(
            "/resources/games",
            authenticated = false,
        )

    /**
     * Retrieves the list of achievements.
     * https://api.hypixel.net/v2/resources/achievements
     */
    suspend fun getAchievements(): AchievementsResponse =
        fetch(
            "/resources/achievements",
            authenticated = false,
        )

    /**
     * Retrieves the list of challenges.
     * https://api.hypixel.net/v2/resources/challenges
     */
    suspend fun getChallenges(): ChallengesResponse =
        fetch(
            "/resources/challenges",
            authenticated = false,
        )

    /**
     * Retrieves the list of quests.
     * https://api.hypixel.net/v2/resources/challenges
     */
    suspend fun getQuests(): QuestsResponse =
        fetch(
            "/resources/quests",
            authenticated = false,
        )

    /**
     * Retrieves the list of guild achievements.
     * https://api.hypixel.net/v2/resources/guilds/achievements
     */
    suspend fun getGuildAchievements(): GuildsAchievementsResponse =
        fetch(
            "/resources/guilds/achievements",
            authenticated = false,
        )

    /**
     * Retrieves the list of vanity pets.
     * https://api.hypixel.net/v2/resources/vanity/pets
     */
    suspend fun getVanityPets(): VanityResponse =
        fetch(
            "/resources/vanity/pets",
            authenticated = false,
        )

    /**
     * Retrieves the list of vanity companions.
     * https://api.hypixel.net/v2/resources/vanity/companions
     */
    suspend fun getVanityCompanions(): VanityResponse =
        fetch(
            "/resources/vanity/companions",
            authenticated = false,
        )

    /**
     * Retrieves the list of SkyBlock collections.
     * https://api.hypixel.net/v2/resources/skyblock/collections
     */
    suspend fun getCollections(): CollectionsResponse =
        fetch<CollectionsResponse>("/resources/skyblock/collections", authenticated = false)

    /**
     * Retrieves SkyBlock skills information.
     * https://api.hypixel.net/v2/resources/skyblock/skills
     */
    suspend fun getSkills(): SkillsResponse =
        fetch<SkillsResponse>("/resources/skyblock/skills", authenticated = false)

    /**
     * Retrieves the list of SkyBlock items.
     * https://api.hypixel.net/v2/resources/skyblock/items
     */
    suspend fun getItems(): ItemsResponse =
        fetch<ItemsResponse>("/resources/skyblock/items", authenticated = false)

    /**
     * Retrieves the current SkyBlock election information.
     * https://api.hypixel.net/v2/resources/skyblock/election
     */
    suspend fun getElection(): ElectionResponse = fetch<ElectionResponse>("/skyblock/election", authenticated = false)

    /**
     * Retrieves the current SkyBlock bingo information.
     * https://api.hypixel.net/v2/resources/skyblock/bingo
     */
    suspend fun getBingo(): BingoResponse = fetch<BingoResponse>("/skyblock/bingo", authenticated = false)

    /**
     * Retrieves SkyBlock news.
     * https://api.hypixel.net/v2/skyblock/news
     */
    suspend fun getNews(): NewsResponse = fetch<NewsResponse>("/skyblock/news")

    /**
     * Searches for SkyBlock auctions by UUID, player, or profile.
     * https://api.hypixel.net/v2/skyblock/auction
     *
     * @param uuid The auction UUID.
     * @param player The player UUID.
     * @param profile The profile UUID.
     */
    suspend fun getAuction(
        uuid: String? = null,
        player: String? = null,
        profile: String? = null,
    ): AuctionsResponse {
        val params = mutableMapOf<String, String>()
        uuid?.let { params["uuid"] = UuidUtils.undash(it) }
        player?.let { params["player"] = UuidUtils.undash(it) }
        profile?.let { params["profile"] = UuidUtils.undash(it) }
        return fetch<AuctionsResponse>("/skyblock/auction", params)
    }

    /**
     * Retrieves active SkyBlock auctions.
     * https://api.hypixel.net/v2/skyblock/auctions
     *
     * @param page The page number to get.
     */
    suspend fun getAuctions(page: Int = 0): AuctionsResponse =
        fetch<AuctionsResponse>("/skyblock/auctions", mapOf("page" to page.toString()), authenticated = false)


    /**
     * Retrieves recently ended SkyBlock auctions.
     * https://api.hypixel.net/v2/skyblock/auctions_ended
     */
    suspend fun getAuctionsEnded(): AuctionsEndedResponse =
        fetch<AuctionsEndedResponse>("/skyblock/auctions_ended", authenticated = false)

    /**
     * Retrieves current bazaar data.
     * https://api.hypixel.net/v2/skyblock/bazaar
     */
    suspend fun getBazaar(): BazaarResponse = fetch<BazaarResponse>("/skyblock/bazaar", authenticated = false)

    /**
     * Retrieves a specific SkyBlock profile by its UUID.
     * https://api.hypixel.net/v2/skyblock/profile
     *
     * @param uuid The UUID of the profile.
     */
    suspend fun getProfile(uuid: String): ProfileResponse =
        fetch(
            "/skyblock/profile",
            mapOf("profile" to UuidUtils.undash(uuid)),
        )

    /**
     * Retrieves all SkyBlock profiles for a player.
     * https://api.hypixel.net/v2/skyblock/profiles
     *
     * @param uuid The UUID of the player.
     */
    suspend fun getProfiles(uuid: String): ProfilesResponse =
        fetch(
            "/skyblock/profiles",
            mapOf("uuid" to UuidUtils.undash(uuid)),
        )

    /**
     * Retrieves SkyBlock museum information for a profile.
     * https://api.hypixel.net/v2/skyblock/museum
     *
     * @param profileUuid The UUID of the SkyBlock profile.
     */
    suspend fun getMuseum(profileUuid: String): MuseumResponse =
        fetch(
            "/skyblock/museum",
            mapOf("profile" to UuidUtils.undash(profileUuid)),
        )


    /**
     * Retrieves SkyBlock garden information for a profile.
     * https://api.hypixel.net/v2/skyblock/garden
     *
     * @param profileUuid The UUID of the SkyBlock profile.
     */
    suspend fun getGarden(profileUuid: String): GardenResponse =
        fetch(
            "/skyblock/garden",
            mapOf("profile" to UuidUtils.undash(profileUuid)),
        )


    /**
     * Retrieves SkyBlock bingo data for a player.
     * https://api.hypixel.net/v2/skyblock/bingo
     *
     * @param uuid The UUID of the player.
     */
    suspend fun getPlayerBingo(uuid: String): BingoResponse =
        fetch(
            "/skyblock/bingo",
            mapOf("uuid" to UuidUtils.undash(uuid)),
        )

    /**
     * Retrieves current SkyBlock fire sales.
     * https://api.hypixel.net/v2/skyblock/firesales
     */
    suspend fun getFiresales(): FiresalesResponse =
        fetch<FiresalesResponse>("/skyblock/firesales", authenticated = false)


    /**
     * Retrieves the currently active housing.
     * https://api.hypixel.net/v2/housing/active
     */
    suspend fun getHousingActive(): HousingActiveResponse = fetch<HousingActiveResponse>("/housing/active")

    /**
     * Retrieves information about a specific housing instance.
     * https://api.hypixel.net/v2/housing/house
     *
     * @param houseUuid The UUID of the housing instance.
     */
    suspend fun getHousingHouse(houseUuid: String): HousingHouseResponse =
        fetch(
            "/housing/house",
            mapOf("house" to UuidUtils.undash(houseUuid)),
        )


    /**
     * Retrieves the housing instances owned by a player.
     * https://api.hypixel.net/v2/housing/houses
     *
     * @param uuid The UUID of the player.
     */
    suspend fun getHousingHouses(uuid: String): HousingHousesResponse =
        fetch(
            "/housing/houses",
            mapOf("player" to UuidUtils.undash(uuid)),
        )

    /**
     * Retrieves the current boosters.
     * https://api.hypixel.net/v2/boosters
     */
    suspend fun getBoosters(): BoostersResponse = fetch<BoostersResponse>("/boosters")

    /**
     * Retrieves the player counts across various games.
     * https://api.hypixel.net/v2/counts
     */
    suspend fun getCounts(): CountsResponse = fetch<CountsResponse>("/counts")

    /**
     * Retrieves the current leaderboards.
     * https://api.hypixel.net/v2/leaderboards
     */
    suspend fun getLeaderboards(): LeaderboardsResponse = fetch<LeaderboardsResponse>("/leaderboards")

    /**
     * Retrieves punishment statistics.
     * https://api.hypixel.net/v2/punishmentstats
     */
    suspend fun getPunishmentStats(): PunishmentStatsResponse = fetch<PunishmentStatsResponse>("/punishmentstats")

    private suspend inline fun <reified T : HypixelResponse> fetch(
        endpoint: String,
        queryParams: Map<String, String> = emptyMap(),
        authenticated: Boolean = true,
    ): T {
        var attempts = 0
        while (true) {
            val urlBuilder = "$baseUrl$endpoint".toHttpUrl().newBuilder()
            queryParams.forEach { (name, value) ->
                urlBuilder.addQueryParameter(name, value)
            }
            val url = urlBuilder.build()

            val requestBuilder =
                Request.Builder()
                    .url(url)
                    .header("Accept", "application/json")

            if (authenticated) {
                requestBuilder.header("API-Key", apiKey)
            }

            val request = requestBuilder.build()

            val result =
                runCatching {
                    suspendCancellableCoroutine { continuation ->
                        val call = internalHttpClient.newCall(request)

                        continuation.invokeOnCancellation {
                            call.cancel()
                        }

                        call.enqueue(
                            object : Callback {
                                override fun onResponse(
                                    call: Call,
                                    response: Response,
                                ) {
                                    response.use {
                                        val rateLimit = parseRateLimit(response.headers)
                                        if (rateLimit != null) {
                                            lastRateLimit = rateLimit
                                        }

                                        if (!response.isSuccessful) {
                                            val errorBody = response.body.string()
                                            val cause =
                                                runCatching {
                                                    val element = json.parseToJsonElement(errorBody)
                                                    element.jsonObject["cause"]?.jsonPrimitive?.content
                                                }.getOrNull() ?: "HTTP Error: ${response.code}"

                                            val exception =
                                                when (response.code) {
                                                    400 -> {
                                                        if (cause.contains("Missing", ignoreCase = true)) {
                                                            MissingFieldException(cause)
                                                        } else {
                                                            InvalidDataException(cause)
                                                        }
                                                    }

                                                    403 -> InvalidApiKeyException(cause)
                                                    404 -> ResourceNotFoundException(cause)
                                                    422 -> InvalidDataException(cause)
                                                    429 -> {
                                                        val isGlobal =
                                                            runCatching {
                                                                json.parseToJsonElement(errorBody)
                                                                    .jsonObject["global"]?.jsonPrimitive?.boolean
                                                            }.getOrNull() ?: false
                                                        val retryAfter = response.header("Retry-After")?.toLongOrNull()
                                                        RateLimitException(cause, isGlobal, retryAfter)
                                                    }

                                                    502 -> HypixelException(cause, 502)
                                                    503 -> DataNotPopulatedException(cause)
                                                    else -> HypixelException(cause, response.code)
                                                }
                                            continuation.resumeWithException(exception)
                                            return
                                        }

                                        try {
                                            val body = response.body.string()
                                            val decoded = json.decodeFromString<T>(body)

                                            decoded.rateLimit = rateLimit

                                            if (decoded.success != true) {
                                                continuation.resumeWithException(
                                                    HypixelException("API Error: ${decoded.cause ?: "Unknown error"}"),
                                                )
                                            } else {
                                                continuation.resume(decoded)
                                            }
                                        } catch (e: Exception) {
                                            continuation.resumeWithException(e)
                                        }
                                    }
                                }

                                override fun onFailure(
                                    call: Call,
                                    e: IOException,
                                ) {
                                    continuation.resumeWithException(e)
                                }
                            },
                        )
                    }
                }

            if (result.isSuccess) {
                return result.getOrThrow()
            } else {
                val exception = result.exceptionOrNull()
                if (exception is RateLimitException && autoRetry && attempts < maxRetries) {
                    val waitTime = exception.retryAfter ?: lastRateLimit?.reset?.toLong() ?: 1L
                    delay(waitTime * 1000)
                    attempts++
                } else {
                    throw exception ?: HypixelException("Unknown error during fetch")
                }
            }
        }
    }
}
