export class UuidUtils {
    static undash(uuid: string): string {
        return uuid.replace(/-/g, "").toLowerCase();
    }

    static dash(uuid: string): string {
        const undashed = this.undash(uuid);
        if (undashed.length !== 32) return uuid;

        return (
            undashed.substring(0, 8) +
            "-" +
            undashed.substring(8, 12) +
            "-" +
            undashed.substring(12, 16) +
            "-" +
            undashed.substring(16, 20) +
            "-" +
            undashed.substring(20, 32)
        );
    }

    static isValid(uuid: string): boolean {
        const undashed = this.undash(uuid);
        return undashed.length === 32 && /^[0-9a-f]+$/.test(undashed);
    }
}
