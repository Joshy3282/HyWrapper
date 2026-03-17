package com.joshy.hywrapper

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import com.joshy.hywrapper.model.housing.HousingActiveResponse
import com.joshy.hywrapper.model.housing.HousingHouseResponse
import com.joshy.hywrapper.model.parseRateLimit
import com.joshy.hywrapper.model.playerdata.GuildResponse
import com.joshy.hywrapper.model.playerdata.OnlineResponse
import com.joshy.hywrapper.model.playerdata.PlayerResponse
import com.joshy.hywrapper.model.playerdata.RecentGamesResponse
import com.joshy.hywrapper.model.resources.*
import com.joshy.hywrapper.model.skyblock.*
import com.joshy.hywrapper.util.UuidUtils
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

open class HypixelException(message: String, val code: Int? = null) : Exception(message)

class InvalidApiKeyException(message: String) : HypixelException(message, 403)

class RateLimitException(message: String, val isGlobal: Boolean = false) : HypixelException(message, 429)


class ResourceNotFoundException(message: String) : HypixelException(message, 404)


class MissingFieldException(message: String) : HypixelException(message, 400)


class InvalidDataException(message: String) : HypixelException(message, 422)


class DataNotPopulatedException(message: String) : HypixelException(message, 503)

class HypixelClient(
    private val apiKey: String,
    httpClient: OkHttpClient = OkHttpClient(),
    private val baseUrl: String = "https://api.hypixel.net/v2",
    private val defaultCacheDurationMinutes: Int = 1,
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
        }

    @Volatile
    var lastRateLimit: RateLimit? = null
        private set

    suspend fun getPlayer(uuid: String): PlayerResponse =
        fetch(
            "/player",
            mapOf("uuid" to UuidUtils.undash(uuid)),
        )

    suspend fun getRecentGames(uuid: String): RecentGamesResponse =
        fetch(
            "/recentgames",
            mapOf("uuid" to UuidUtils.undash(uuid)),
        )

    suspend fun getStatus(uuid: String): OnlineResponse =
        fetch(
            "/status",
            mapOf("uuid" to UuidUtils.undash(uuid)),
        )

    suspend fun getGuildById(id: String): GuildResponse =
        fetch(
            "/guild",
            mapOf("id" to id),
        )

    suspend fun getGuildByPlayer(uuid: String): GuildResponse =
        fetch(
            "/guild",
            mapOf("player" to UuidUtils.undash(uuid)),
        )

    suspend fun getGuildByName(name: String): GuildResponse =
        fetch(
            "/guild",
            mapOf("name" to name),
        )

    suspend fun getHousingActive(): HousingActiveResponse = fetch("/housing/active")

    suspend fun getHousingHouse(houseUuid: String): HousingHouseResponse =
        fetch(
            "/housing/house",
            mapOf("house" to UuidUtils.undash(houseUuid)),
        )

    suspend fun getResourceGames(): GamesResponse =
        fetch(
            "/resources/games",
            authenticated = false,
        )

    suspend fun getResourceAchievements(): AchievementsResponse =
        fetch(
            "/resources/achievements",
            authenticated = false,
        )

    suspend fun getResourceChallenges(): ChallengesResponse =
        fetch(
            "/resources/challenges",
            authenticated = false,
        )

    suspend fun getResourceQuests(): QuestsResponse =
        fetch(
            "/resources/quests",
            authenticated = false,
        )

    suspend fun getResourceGuildAchievements(): GuildsAchievementsResponse =
        fetch(
            "/resources/guilds/achievements",
            authenticated = false,
        )

    suspend fun getResourceVanityPets(): VanityResponse =
        fetch(
            "/resources/vanity/pets",
            authenticated = false,
        )

    suspend fun getResourceVanityCompanions(): VanityResponse =
        fetch(
            "/resources/vanity/companions",
            authenticated = false,
        )

    suspend fun getBingo(): BingoResponse = fetch("/skyblock/bingo")

    suspend fun getElection(): ElectionResponse = fetch("/skyblock/election")

    suspend fun getSkyblockNews(): NewsResponse = fetch("/skyblock/news")


    suspend fun getBazaar(): BazaarResponse = fetch("/skyblock/bazaar")

    suspend fun getCollections(): CollectionsResponse = fetch("/resources/skyblock/collections", authenticated = false)

    suspend fun getAuctionsEnded(): AuctionsEndedResponse = fetch("/skyblock/auctions_ended")

    suspend fun getAuctions(page: Int): AuctionsResponse =
        fetch(
            "/skyblock/auctions",
            mapOf("page" to page.toString()),
        )

    suspend fun getFiresales(): FiresalesResponse = fetch("/skyblock/firesales")

    suspend fun getSkyblockSkills(): SkillsResponse = fetch("/resources/skyblock/skills", authenticated = false)


    private suspend inline fun <reified T : HypixelResponse> fetch(
        endpoint: String,
        queryParams: Map<String, String> = emptyMap(),
        authenticated: Boolean = true,
    ): T {
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

        return suspendCancellableCoroutine { continuation ->
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
                                        json.parseToJsonElement(errorBody).jsonObject["cause"]?.jsonPrimitive?.content
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
                                                    json.parseToJsonElement(errorBody).jsonObject["global"]?.jsonPrimitive?.boolean
                                                }.getOrNull() ?: false
                                            RateLimitException(cause, isGlobal)
                                        }

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

                                if (!decoded.success) {
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
}
