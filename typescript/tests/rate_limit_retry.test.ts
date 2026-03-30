import axios from "axios";
import MockAdapter from "axios-mock-adapter";
import { HypixelClient } from "../src/client";
import { RateLimitException } from "../src/types";

describe("HypixelClient Rate Limit Retry", () => {
    let mock: MockAdapter;
    const apiKey = "test-api-key";

    beforeEach(() => {
        mock = new MockAdapter(axios);
    });

    afterEach(() => {
        mock.restore();
    });

    test("should auto retry on 429", async () => {
        const client = new HypixelClient({
            api_key: apiKey,
            auto_retry: true,
            max_retries: 2
        });

        mock.onGet("/skyblock/bingo").replyOnce(429,
            { success: false, cause: "Rate limit reached" },
            {
                "ratelimit-limit": "300",
                "ratelimit-remaining": "0",
                "ratelimit-reset": "0"
            }
        );

        mock.onGet("/skyblock/bingo").replyOnce(200, { success: true, name: "Bingo" });

        const response = await client.getBingo();
        expect(response.success).toBe(true);
        expect(response.name).toBe("Bingo");
        expect(mock.history.get.length).toBe(2);
    });

    test("should auto retry with retry-after header", async () => {
        const client = new HypixelClient({
            api_key: apiKey,
            auto_retry: true,
            max_retries: 2
        });

        mock.onGet("/skyblock/bingo").replyOnce(429, 
            { success: false, cause: "Rate limit reached" },
            { "retry-after": "0" }
        );

        mock.onGet("/skyblock/bingo").replyOnce(200, { success: true, name: "Bingo" });

        const response = await client.getBingo();
        expect(response.success).toBe(true);
        expect(mock.history.get.length).toBe(2);
    });

    test("should fail after max retries", async () => {
        const client = new HypixelClient({
            api_key: apiKey,
            auto_retry: true,
            max_retries: 1
        });

        mock.onGet("/skyblock/bingo").reply(429, 
            { success: false, cause: "Rate limit reached" },
            { "ratelimit-reset": "0" }
        );

        await expect(client.getBingo()).rejects.toThrow(RateLimitException);
        expect(mock.history.get.length).toBe(2);
    });

    test("should not retry when disabled", async () => {
        const client = new HypixelClient({
            api_key: apiKey,
            auto_retry: false
        });

        mock.onGet("/skyblock/bingo").reply(429, 
            { success: false, cause: "Rate limit reached" }
        );

        await expect(client.getBingo()).rejects.toThrow(RateLimitException);
        expect(mock.history.get.length).toBe(1);
    });
});
