import axios from "axios";
import { HypixelClient } from "../src/client";

describe("HypixelClient Dependency Injection", () => {
    test("should use custom axios instance", async () => {
        const customInstance = axios.create({
            baseURL: "https://api.hypixel.net/v2",
        });
        const client = new HypixelClient({
            api_key: "test",
            axios_instance: customInstance
        });

        expect((client as any).axiosInstance).toBe(customInstance);
        expect((client as any).baseUrl).toBe("https://api.hypixel.net/v2");
        expect(customInstance.defaults.baseURL).toBe("https://api.hypixel.net/v2");
    });

    test("should use default axios instance if none provided", () => {
        const client = new HypixelClient({
            api_key: "test"
        });
        expect((client as any).axiosInstance).toBeDefined();
        expect((client as any).axiosInstance.defaults.baseURL).toBe("https://api.hypixel.net/v2");
    });
});
