import * as zlib from "zlib";

export class NbtUtils {
    static decodeInventoryData(base64Encoded: string): Buffer {
        const cleanedBase64 = this.unescapeUnicode(base64Encoded);
        const compressed = Buffer.from(cleanedBase64, "base64");
        return zlib.gunzipSync(compressed);
    }

    private static unescapeUnicode(input: string): string {
        if (!input.includes("\\u")) return input;

        return input.replace(/\\u([0-9a-fA-F]{4})/g, (_, group) => {
            return String.fromCharCode(parseInt(group, 16));
        });
    }
}
