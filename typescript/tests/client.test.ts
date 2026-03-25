import axios from "axios";
import MockAdapter from "axios-mock-adapter";
import { HypixelClient } from "../src/client";
import { InvalidApiKeyException, RateLimitException } from "../src/types";

describe("HypixelClient", () => {
    let mock: MockAdapter;
    let client: HypixelClient;
    const apiKey = "test-api-key";

    beforeEach(() => {
        mock = new MockAdapter(axios);
        client = new HypixelClient({ api_key: apiKey });
    });

    afterEach(() => {
        mock.restore();
    });

    test("getPlayer should return player data on success", async () => {
        const uuid = "550e8400-e29b-41d4-a716-446655440000";
        const undashedUuid = uuid.replace(/-/g, "");
        const mockResponse = {
            success: true,
            player: {
                displayname: "TestPlayer",
                uuid: undashedUuid,
            },
        };

        mock.onGet("/player", { params: { uuid: undashedUuid } }).reply(200, mockResponse, {
            "ratelimit-limit": "120",
            "ratelimit-remaining": "119",
            "ratelimit-reset": "60",
        });

        const result = await client.getPlayer(uuid);
        expect(result.success).toBe(true);
        expect(result.player?.displayname).toBe("TestPlayer");
        expect(client.lastRateLimit).toEqual({
            limit: 120,
            remaining: 119,
            reset: 60,
        });
    });

    test("should throw InvalidApiKeyException on 403", async () => {
        mock.onGet("/player").reply(403, {
            success: false,
            cause: "Invalid API key",
        });

        await expect(client.getPlayer("uuid")).rejects.toThrow(InvalidApiKeyException);
    });

    test("should throw RateLimitException on 429", async () => {
        mock.onGet("/player").reply(
            429,
            {
                success: false,
                cause: "Rate limit reached",
                global: false,
            },
            {
                "retry-after": "5",
            },
        );

        try {
            await client.getPlayer("uuid");
            fail("Should have thrown RateLimitException");
        } catch (error: any) {
            expect(error).toBeInstanceOf(RateLimitException);
            expect(error.retryAfter).toBe(5);
            expect(error.isGlobal).toBe(false);
        }
    });

    test("getGames should work without authentication (authenticated: false)", async () => {
        const mockResponse = {
            success: true,
            games: {
                MAIN: { name: "Main Lobby" },
            },
        };

        mock.onGet("/resources/games").reply(200, mockResponse);

        const result = await client.getGames();
        expect(result.success).toBe(true);
        expect(result.games?.MAIN?.name).toBe("Main Lobby");

        expect(mock.history.get[0].headers?.["API-Key"]).toBeUndefined();
    });
});
