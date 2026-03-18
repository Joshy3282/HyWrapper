package com.joshy.hywrapper

import kotlinx.coroutines.runBlocking
import okhttp3.mockwebserver.MockResponse
import okhttp3.mockwebserver.MockWebServer
import org.junit.jupiter.api.AfterEach
import org.junit.jupiter.api.BeforeEach
import org.junit.jupiter.api.Test
import kotlin.test.assertEquals
import kotlin.test.assertFailsWith

class RateLimitRetryTest {
    private lateinit var server: MockWebServer

    @BeforeEach
    fun setup() {
        server = MockWebServer()
        server.start()
    }

    @AfterEach
    fun tearDown() {
        server.shutdown()
    }

    @Test
    fun `test auto retry on 429`() = runBlocking {
        val client = HypixelClient(
            "test-api-key",
            baseUrl = server.url("/").toString().removeSuffix("/"),
            autoRetry = true,
            maxRetries = 2
        )

        val rateLimitResponse = MockResponse()
            .setResponseCode(429)
            .setBody("""{"success": false, "cause": "Rate limit reached"}""")
            .addHeader("RateLimit-Limit", "300")
            .addHeader("RateLimit-Remaining", "0")
            .addHeader("RateLimit-Reset", "1")

        val successResponse = MockResponse()
            .setResponseCode(200)
            .setBody("""{"success": true, "name": "Bingo"}""")

        server.enqueue(rateLimitResponse)
        server.enqueue(successResponse)

        val response = client.getBingo()
        assertEquals(true, response.success)
        assertEquals("Bingo", response.name)
        assertEquals(2, server.requestCount)
    }

    @Test
    fun `test auto retry with Retry-After header`() = runBlocking {
        val client = HypixelClient(
            "test-api-key",
            baseUrl = server.url("/").toString().removeSuffix("/"),
            autoRetry = true,
            maxRetries = 2
        )

        val rateLimitResponse = MockResponse()
            .setResponseCode(429)
            .setBody("""{"success": false, "cause": "Rate limit reached"}""")
            .addHeader("Retry-After", "1")

        val successResponse = MockResponse()
            .setResponseCode(200)
            .setBody("""{"success": true, "name": "Bingo"}""")

        server.enqueue(rateLimitResponse)
        server.enqueue(successResponse)

        val response = client.getBingo()
        assertEquals(true, response.success)
        assertEquals(2, server.requestCount)
    }

    @Test
    fun `test max retries exceeded`() = runBlocking {
        val client = HypixelClient(
            "test-api-key",
            baseUrl = server.url("/").toString().removeSuffix("/"),
            autoRetry = true,
            maxRetries = 1
        )

        val rateLimitResponse = MockResponse()
            .setResponseCode(429)
            .setBody("""{"success": false, "cause": "Rate limit reached"}""")
            .addHeader("RateLimit-Reset", "1")

        server.enqueue(rateLimitResponse)
        server.enqueue(rateLimitResponse)
        server.enqueue(rateLimitResponse)

        assertFailsWith<RateLimitException> {
            client.getBingo()
        }
        assertEquals(2, server.requestCount) // Initial call + 1 retry
    }

    @Test
    fun `test no retry when autoRetry is false`() = runBlocking {
        val client = HypixelClient(
            "test-api-key",
            baseUrl = server.url("/").toString().removeSuffix("/"),
            autoRetry = false
        )

        val rateLimitResponse = MockResponse()
            .setResponseCode(429)
            .setBody("""{"success": false, "cause": "Rate limit reached"}""")

        server.enqueue(rateLimitResponse)

        assertFailsWith<RateLimitException> {
            client.getBingo()
        }
        assertEquals(1, server.requestCount)
    }
}
