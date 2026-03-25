import { UuidUtils } from "../src/utils/uuid_utils";

describe("UuidUtils", () => {
    const dashed = "550e8400-e29b-41d4-a716-446655440000";
    const undashed = "550e8400e29b41d4a716446655440000";

    test("undash should remove dashes and convert to lowercase", () => {
        expect(UuidUtils.undash(dashed)).toBe(undashed);
        expect(UuidUtils.undash(undashed)).toBe(undashed);
    });

    test("dash should add dashes to an undashed UUID", () => {
        expect(UuidUtils.dash(undashed)).toBe(dashed);
        expect(UuidUtils.dash(dashed)).toBe(dashed);
    });

    test("isValid should validate UUIDs correctly", () => {
        expect(UuidUtils.isValid(dashed)).toBe(true);
        expect(UuidUtils.isValid(undashed)).toBe(true);
        expect(UuidUtils.isValid("invalid-uuid")).toBe(false);
        expect(UuidUtils.isValid("550e8400-e29b-41d4-a716-44665544000g")).toBe(false);
    });
});
