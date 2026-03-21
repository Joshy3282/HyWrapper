package com.joshy.hywrapper

import com.joshy.hywrapper.data.skyblock.SkillType
import kotlinx.coroutines.runBlocking
import okhttp3.mockwebserver.MockResponse
import okhttp3.mockwebserver.MockWebServer
import org.junit.jupiter.api.AfterEach
import org.junit.jupiter.api.BeforeEach
import org.junit.jupiter.api.Test
import kotlin.test.assertEquals
import kotlin.test.assertFailsWith
import kotlin.test.assertNotNull

class HypixelClientTest {
    private lateinit var server: MockWebServer
    private lateinit var client: HypixelClient

    @BeforeEach
    fun setup() {
        server = MockWebServer()
        server.start()
        client =
            HypixelClient(
                "test-api-key",
                baseUrl = server.url("/").toString().removeSuffix("/"),
            )
    }

    @AfterEach
    fun tearDown() {
        server.shutdown()
    }

    @Test
    fun `test getBingo success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "lastUpdated": 1618214400000,
                    "id": 1,
                    "name": "Bingo",
                    "start": 1618214400000,
                    "end": 1618214400000,
                    "modifier": "Modifier",
                    "goals": []
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getBingo()
            assertEquals(true, response.success)
            assertEquals("Bingo", response.name)

            val recordedRequest = server.takeRequest()
            assertEquals(null, recordedRequest.getHeader("API-Key"))
            assertEquals("/skyblock/bingo", recordedRequest.path)
        }

    @Test
    fun `test getElection success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "lastUpdated": 1618214400000,
                    "mayor": {
                        "key": "mayor_key",
                        "name": "Mayor Name",
                        "perks": []
                    }
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getElection()
            assertEquals(true, response.success)
            assertEquals("Mayor Name", response.mayor?.name)

            val recordedRequest = server.takeRequest()
            assertEquals(null, recordedRequest.getHeader("API-Key"))
            assertEquals("/skyblock/election", recordedRequest.path)
        }

    @Test
    fun `test getNews success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "items": [
                        {
                            "item": {
                                "material": "DIAMOND"
                            },
                            "link": "https://hypixel.net",
                            "title": "SkyBlock v0.11",
                            "text": "15th January 2021"
                        }
                    ]
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getNews()
            assertEquals(true, response.success)
            assertEquals(1, response.news?.size)
            assertEquals("SkyBlock v0.11", response.news?.get(0)?.title)

            val recordedRequest = server.takeRequest()
            assertEquals("/skyblock/news", recordedRequest.path)
        }

    @Test
    fun `test getItems success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "lastUpdated": 1618214400000,
                    "items": [
                        {
                            "id": "SKYBLOCK_ITEM",
                            "name": "SkyBlock Item",
                            "material": "DIAMOND"
                        }
                    ]
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getItems()
            assertEquals(true, response.success)
            assertEquals(1, response.items?.size)
            assertEquals("SKYBLOCK_ITEM", response.items?.get(0)?.id)

            val recordedRequest = server.takeRequest()
            assertEquals("/resources/skyblock/items", recordedRequest.path)
            assertEquals(null, recordedRequest.getHeader("API-Key"))
        }

    @Test
    fun `test getBazaar success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "lastUpdated": 1618214400000,
                    "products": {
                        "INK_SACK:3": {
                            "product_id": "INK_SACK:3",
                            "quick_status": {
                                "productId": "INK_SACK:3",
                                "sellPrice": 1.0,
                                "buyPrice": 2.0
                            }
                        }
                    }
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getBazaar()
            assertEquals(true, response.success)
            assertNotNull(response.products?.get("INK_SACK:3"))

            val recordedRequest = server.takeRequest()
            assertEquals("/skyblock/bazaar", recordedRequest.path)
        }

    @Test
    fun `test getCollections success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "lastUpdated": 1618214400000,
                    "version": "0.1",
                    "collections": {
                        "FARMING": {
                            "name": "Farming",
                            "items": {
                                "INK_SACK:3": {
                                    "name": "Cocoa Beans",
                                    "maxTiers": 9
                                }
                            }
                        }
                    }
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getCollections()
            assertEquals(true, response.success)
            assertNotNull(response.collections?.get("FARMING"))

            val recordedRequest = server.takeRequest()
            assertEquals("/resources/skyblock/collections", recordedRequest.path)
            assertEquals(null, recordedRequest.getHeader("API-Key"))
        }

    @Test
    fun `test getPlayer with dashed uuid success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "player": {
                        "displayname": "PlayerName",
                        "uuid": "ac29411d0826412f98c0dd14b334c1fa"
                    }
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            // Dashed UUID
            val response = client.getPlayer("ac29411d-0826-412f-98c0-dd14b334c1fa")
            assertEquals(true, response.success)

            val recordedRequest = server.takeRequest()
            // Should be undashed in the request
            assertEquals("/player?uuid=ac29411d0826412f98c0dd14b334c1fa", recordedRequest.path)
        }

    @Test
    fun `test getPlayer success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "player": {
                        "displayname": "PlayerName",
                        "uuid": "ac29411d0826412f98c0dd14b334c1fa"
                    }
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getPlayer("ac29411d0826412f98c0dd14b334c1fa")
            assertEquals(true, response.success)

            val recordedRequest = server.takeRequest()
            assertEquals("/player?uuid=ac29411d0826412f98c0dd14b334c1fa", recordedRequest.path)
        }

    @Test
    fun `test getRecentGames success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "uuid": "ac29411d0826412f98c0dd14b334c1fa",
                    "games": [
                        {
                            "date": 1618214400000,
                            "gameType": "SKYWARS",
                            "mode": "solo_normal",
                            "map": "Shire",
                            "ended": 1618214400000
                        }
                    ]
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getRecentGames("ac29411d0826412f98c0dd14b334c1fa")
            assertEquals(true, response.success)
            assertEquals(1, response.games?.size)
            assertEquals("SKYWARS", response.games?.get(0)?.gameType)

            val recordedRequest = server.takeRequest()
            assertEquals("/recentgames?uuid=ac29411d0826412f98c0dd14b334c1fa", recordedRequest.path)
        }

    @Test
    fun `test getStatus success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "uuid": "ac29411d0826412f98c0dd14b334c1fa",
                    "session": {
                        "online": true
                    }
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getStatus("ac29411d0826412f98c0dd14b334c1fa")
            assertEquals(true, response.success)
            assertEquals(true, response.session?.online)

            val recordedRequest = server.takeRequest()
            assertEquals("/status?uuid=ac29411d0826412f98c0dd14b334c1fa", recordedRequest.path)
        }

    @Test
    fun `test getGuildById success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "guild": {
                        "_id": "530967340cf200673456",
                        "name": "The Guild"
                    }
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getGuildById("530967340cf200673456")
            assertEquals(true, response.success)
            assertEquals("The Guild", response.guild?.name)

            val recordedRequest = server.takeRequest()
            assertEquals("/guild?id=530967340cf200673456", recordedRequest.path)
        }

    @Test
    fun `test getGuildByName success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "guild": {
                        "_id": "530967340cf200673456",
                        "name": "The Guild"
                    }
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getGuildByName("The Guild")
            assertEquals(true, response.success)
            assertEquals("The Guild", response.guild?.name)

            val recordedRequest = server.takeRequest()
            assertEquals("/guild?name=The%20Guild", recordedRequest.path)
        }

    @Test
    fun `test getHousingActive success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "houses": [
                        {
                            "uuid": "house_uuid",
                            "owner": "owner_uuid",
                            "name": "Cool House"
                        }
                    ]
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getHousingActive()
            assertEquals(true, response.success)
            assertEquals(1, response.houses?.size)
            assertEquals("Cool House", response.houses?.get(0)?.name)

            val recordedRequest = server.takeRequest()
            assertEquals("/housing/active", recordedRequest.path)
        }

    @Test
    fun `test getHousingHouse success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "house": {
                        "uuid": "house_uuid",
                        "owner": "owner_uuid",
                        "name": "Cool House"
                    }
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getHousingHouse("house_uuid")
            assertEquals(true, response.success)
            assertEquals("Cool House", response.house?.name)

            val recordedRequest = server.takeRequest()
            assertEquals("/housing/house?house=house_uuid", recordedRequest.path)
        }

    @Test
    fun `test getGames success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "lastUpdated": 1618214400000,
                    "games": {
                        "SKYWARS": {
                            "id": 1,
                            "name": "SkyWars"
                        }
                    }
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getGames()
            assertEquals(true, response.success)
            assertEquals("SkyWars", response.games?.get("SKYWARS")?.name)

            val recordedRequest = server.takeRequest()
            assertEquals("/resources/games", recordedRequest.path)
            assertEquals(null, recordedRequest.getHeader("API-Key"))
        }

    @Test
    fun `test getAchievements success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "lastUpdated": 1618214400000,
                    "achievements": {}
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getAchievements()
            assertEquals(true, response.success)

            val recordedRequest = server.takeRequest()
            assertEquals("/resources/achievements", recordedRequest.path)
        }

    @Test
    fun `test getChallenges success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "lastUpdated": 1618214400000,
                    "challenges": {}
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getChallenges()
            assertEquals(true, response.success)

            val recordedRequest = server.takeRequest()
            assertEquals("/resources/challenges", recordedRequest.path)
        }

    @Test
    fun `test getRQuests success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "lastUpdated": 1618214400000,
                    "quests": {}
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getQuests()
            assertEquals(true, response.success)

            val recordedRequest = server.takeRequest()
            assertEquals("/resources/quests", recordedRequest.path)
        }

    @Test
    fun `test getGuildAchievements success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "lastUpdated": 1618214400000,
                    "one_time": {},
                    "tiered": {}
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getGuildAchievements()
            assertEquals(true, response.success)

            val recordedRequest = server.takeRequest()
            assertEquals("/resources/guilds/achievements", recordedRequest.path)
        }

    @Test
    fun `test getVanityPets success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "lastUpdated": 1618214400000,
                    "types": [],
                    "rarities": []
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getVanityPets()
            assertEquals(true, response.success)

            val recordedRequest = server.takeRequest()
            assertEquals("/resources/vanity/pets", recordedRequest.path)
        }

    @Test
    fun `test getVanityCompanions success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "lastUpdated": 1618214400000,
                    "types": [],
                    "rarities": []
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getVanityCompanions()
            assertEquals(true, response.success)

            val recordedRequest = server.takeRequest()
            assertEquals("/resources/vanity/companions", recordedRequest.path)
        }

    @Test
    fun `test API error`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": false,
                    "cause": "Invalid API Key"
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val exception =
                assertFailsWith<HypixelException> {
                    client.getBingo()
                }
            assertEquals("API Error: Invalid API Key", exception.message)
        }

    @Test
    fun `test 403 Invalid API Key`(): Unit =
        runBlocking {
            val jsonResponse = """{"success": false, "cause": "Invalid API key"}"""
            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(403))

            assertFailsWith<InvalidApiKeyException> {
                client.getBingo()
            }
        }

    @Test
    fun `test 404 Not Found`(): Unit =
        runBlocking {
            val jsonResponse = """{"success": false, "cause": "Not Found"}"""
            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(404))

            assertFailsWith<ResourceNotFoundException> {
                client.getBingo()
            }
        }

    @Test
    fun `test 400 Missing Field`(): Unit =
        runBlocking {
            val jsonResponse = """{"success": false, "cause": "Missing one or more fields"}"""
            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(400))

            assertFailsWith<MissingFieldException> {
                client.getBingo()
            }
        }

    @Test
    fun `test 400 Malformed Data`(): Unit =
        runBlocking {
            val jsonResponse = """{"success": false, "cause": "Malformed UUID"}"""
            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(400))

            assertFailsWith<InvalidDataException> {
                client.getBingo()
            }
        }

    @Test
    fun `test 429 Rate Limit`() =
        runBlocking {
            val jsonResponse = """{"success": false, "cause": "Key throttle", "throttle": true}"""
            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(429))

            val exception =
                assertFailsWith<RateLimitException> {
                    client.getBingo()
                }
            assertEquals(false, exception.isGlobal)
        }

    @Test
    fun `test rate limit parsing`() =
        runBlocking {
            val jsonResponse = """{"success": true, "name": "Bingo"}"""
            server.enqueue(
                MockResponse()
                    .setBody(jsonResponse)
                    .addHeader("RateLimit-Limit", "300")
                    .addHeader("RateLimit-Remaining", "299")
                    .addHeader("RateLimit-Reset", "59"),
            )

            val response = client.getBingo()
            val rateLimit = response.rateLimit

            assertEquals(300, rateLimit?.limit)
            assertEquals(299, rateLimit?.remaining)
            assertEquals(59, rateLimit?.reset)

            assertEquals(300, client.lastRateLimit?.limit)
        }

    @Test
    fun `test getAuctionsEnded success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "lastUpdated": 1618214400000,
                    "auctions": [
                        {
                            "auction_id": "auction1",
                            "seller": "seller1",
                            "price": 100
                        }
                    ]
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getAuctionsEnded()
            assertEquals(true, response.success)
            assertEquals(1, response.auctions?.size)
            assertEquals("auction1", response.auctions?.get(0)?.auctionId)

            val recordedRequest = server.takeRequest()
            assertEquals("/skyblock/auctions_ended", recordedRequest.path)
        }

    @Test
    fun `test getGarden success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "garden": {
                        "uuid": "garden-uuid",
                        "unlocked_plots_ids": [],
                        "garden_experience": 1000.5
                    }
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getGarden("ad8fefaa8351454bb739a4eaa872173f")
            assertEquals(true, response.success)
            assertEquals("garden-uuid", response.garden?.uuid)
            assertEquals(1000.5, response.garden?.gardenExperience)

            val recordedRequest = server.takeRequest()
            assertEquals("/skyblock/garden?profile=ad8fefaa8351454bb739a4eaa872173f", recordedRequest.path)
        }

    @Test
    fun `test getMuseum success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "members": {
                        "ad8fefaa8351454bb739a4eaa872173f": {
                            "value": 1000,
                            "appraisal": true,
                            "items": {
                                "HYPERION": {
                                    "donated_time": 1618214400000
                                }
                            }
                        }
                    }
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getMuseum("ad8fefaa8351454bb739a4eaa872173f")
            assertEquals(true, response.success)
            assertNotNull(response.members?.get("ad8fefaa8351454bb739a4eaa872173f"))

            val recordedRequest = server.takeRequest()
            assertEquals("/skyblock/museum?profile=ad8fefaa8351454bb739a4eaa872173f", recordedRequest.path)
        }

    @Test
    fun `test getAuctions success`() =

        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "page": 1,
                    "totalPages": 5,
                    "totalAuctions": 100,
                    "lastUpdated": 1618214400000,
                    "auctions": [
                        {
                            "uuid": "auction-uuid",
                            "auctioneer": "player-uuid",
                            "item_name": "Hyperion",
                            "starting_bid": 1000000000
                        }
                    ]
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getAuctions(1)
            assertEquals(true, response.success)
            assertEquals(1, response.page)
            assertEquals(5, response.totalPages)
            assertEquals(1, response.auctions?.size)
            assertEquals("Hyperion", response.auctions?.get(0)?.itemName)

            val recordedRequest = server.takeRequest()
            assertEquals("/skyblock/auctions?page=1", recordedRequest.path)
        }

    @Test
    fun `test getAuctions 404 page not found`(): Unit =
        runBlocking {
            val jsonResponse = """{"success": false, "cause": "Page not found"}"""
            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(404))

            assertFailsWith<ResourceNotFoundException> {
                client.getAuctions(999)
            }
        }

    @Test
    fun `test getAuctions 422 invalid page`(): Unit =
        runBlocking {
            val jsonResponse = """{"success": false, "cause": "Invalid page"}"""
            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(422))

            assertFailsWith<InvalidDataException> {
                client.getAuctions(-1)
            }
        }

    @Test
    fun `test getAuctions 503 data not populated`(): Unit =
        runBlocking {
            val jsonResponse = """{"success": false, "cause": "Data not populated"}"""
            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(503))

            assertFailsWith<DataNotPopulatedException> {
                client.getAuctions(1)
            }
        }

    @Test
    fun `test getFiresales success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "sales": [
                        {
                            "item_id": "pet_skin_black_cat",
                            "start": 1618214400000,
                            "end": 1618214400000,
                            "amount": 1000,
                            "price": 500
                        }
                    ]
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getFiresales()
            assertEquals(true, response.success)
            assertEquals(1, response.sales?.size)
            assertEquals("pet_skin_black_cat", response.sales?.get(0)?.itemId)

            val recordedRequest = server.takeRequest()
            assertEquals("/skyblock/firesales", recordedRequest.path)
        }

    @Test
    fun `test getSkills success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "lastUpdated": 1618214400000,
                    "version": "1.0",
                    "skills": {
                        "FARMING": {
                            "name": "Farming",
                            "description": "Farming description",
                            "maxLevel": 60
                        }
                    }
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getSkills()
            assertEquals(true, response.success)
            assertEquals("Farming", response.skills?.get(SkillType.FARMING)?.name)

            val recordedRequest = server.takeRequest()
            assertEquals("/resources/skyblock/skills", recordedRequest.path)
        }

    @Test
    fun `test getBoosters success`() =
        runBlocking {
            val jsonResponse = """{"success": true, "boosters": []}"""
            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))
            val response = client.getBoosters()
            assertEquals(true, response.success)
            assertEquals("/boosters", server.takeRequest().path)
        }

    @Test
    fun `test getCounts success`() =
        runBlocking {
            val jsonResponse = """{"success": true, "games": {}, "playerCount": 100}"""
            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))
            val response = client.getCounts()
            assertEquals(true, response.success)
            assertEquals(100, response.playerCount)
            assertEquals("/counts", server.takeRequest().path)
        }

    @Test
    fun `test getLeaderboards success`() =
        runBlocking {
            val jsonResponse = """{"success": true, "leaderboards": {}}"""
            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))
            val response = client.getLeaderboards()
            assertEquals(true, response.success)
            assertEquals("/leaderboards", server.takeRequest().path)
        }

    @Test
    fun `test getPunishmentStats success`() =
        runBlocking {
            val jsonResponse = """{"success": true, "staff_total": 10}"""
            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))
            val response = client.getPunishmentStats()
            assertEquals(true, response.success)
            assertEquals(10, response.staffTotal)
            assertEquals("/punishmentstats", server.takeRequest().path)
        }

    @Test
    fun `test getProfile success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "profile": {
                        "profile_id": "profile-uuid",
                        "members": {}
                    }
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getProfile("ac29411d0826412f98c0dd14b334c1fa")
            assertEquals(true, response.success)

            val recordedRequest = server.takeRequest()
            assertEquals("/skyblock/profile?profile=ac29411d0826412f98c0dd14b334c1fa", recordedRequest.path)
        }

    @Test
    fun `test getGuildByPlayer success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "guild": {
                        "_id": "530967340cf200673456",
                        "name": "The Guild"
                    }
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getGuildByPlayer("ac29411d0826412f98c0dd14b334c1fa")
            assertEquals(true, response.success)
            assertEquals("The Guild", response.guild?.name)

            val recordedRequest = server.takeRequest()
            assertEquals("/guild?player=ac29411d0826412f98c0dd14b334c1fa", recordedRequest.path)
        }

    @Test
    fun `test getHousingHouses success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "houses": [
                        {
                            "uuid": "house_uuid",
                            "owner": "owner_uuid",
                            "name": "Cool House"
                        }
                    ]
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getHousingHouses("ac29411d0826412f98c0dd14b334c1fa")
            assertEquals(true, response.success)
            assertEquals(1, response.houses?.size)

            val recordedRequest = server.takeRequest()
            assertEquals("/housing/houses?player=ac29411d0826412f98c0dd14b334c1fa", recordedRequest.path)
        }

    @Test
    fun `test getProfiles success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "profiles": [
                        {
                            "profile_id": "profile-uuid",
                            "cute_name": "Apple"
                        }
                    ]
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getProfiles("ac29411d0826412f98c0dd14b334c1fa")
            assertEquals(true, response.success)
            assertEquals(1, response.profiles?.size)

            val recordedRequest = server.takeRequest()
            assertEquals("/skyblock/profiles?uuid=ac29411d0826412f98c0dd14b334c1fa", recordedRequest.path)
        }

    @Test
    fun `test getPlayerBingo success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "goals": []
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getPlayerBingo("ac29411d0826412f98c0dd14b334c1fa")
            assertEquals(true, response.success)

            val recordedRequest = server.takeRequest()
            assertEquals("/skyblock/bingo?uuid=ac29411d0826412f98c0dd14b334c1fa", recordedRequest.path)
        }

    @Test
    fun `test getAuction by uuid success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "auctions": []
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getAuction(uuid = "ac29411d-0826-412f-98c0-dd14b334c1fa")
            assertEquals(true, response.success)

            val recordedRequest = server.takeRequest()
            assertEquals("/skyblock/auction?uuid=ac29411d0826412f98c0dd14b334c1fa", recordedRequest.path)
        }

    @Test
    fun `test getAuction by player success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "auctions": []
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getAuction(player = "ac29411d-0826-412f-98c0-dd14b334c1fa")
            assertEquals(true, response.success)

            val recordedRequest = server.takeRequest()
            assertEquals("/skyblock/auction?player=ac29411d0826412f98c0dd14b334c1fa", recordedRequest.path)
        }

    @Test
    fun `test getAuction by profile success`() =
        runBlocking {
            val jsonResponse =
                """
                {
                    "success": true,
                    "auctions": []
                }
                """.trimIndent()

            server.enqueue(MockResponse().setBody(jsonResponse).setResponseCode(200))

            val response = client.getAuction(profile = "ac29411d-0826-412f-98c0-dd14b334c1fa")
            assertEquals(true, response.success)

            val recordedRequest = server.takeRequest()
            assertEquals("/skyblock/auction?profile=ac29411d0826412f98c0dd14b334c1fa", recordedRequest.path)
        }
}
