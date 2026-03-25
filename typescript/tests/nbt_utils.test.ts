import * as zlib from "zlib";
import { NbtUtils } from "../src/utils/nbt_utils";

describe("NbtUtils", () => {
    test("decodeInventoryData should correctly decode GZIP'd base64 data", () => {
        const testData = "Hello, Hypixel!";
        const compressed = zlib.gzipSync(Buffer.from(testData));
        const base64 = compressed.toString("base64");

        const decoded = NbtUtils.decodeInventoryData(base64);
        expect(decoded.toString()).toBe(testData);
    });

    test("decodeInventoryData should handle escaped unicode correctly", () => {
        const testData = "Unicode test";
        const compressed = zlib.gzipSync(Buffer.from(testData));
        const base64 = compressed.toString("base64");

        const escapedBase64 = base64.replace(/=/g, "\\u003d");

        const decoded = NbtUtils.decodeInventoryData(escapedBase64);
        expect(decoded.toString()).toBe(testData);
    });
});
