import { HypixelResponse } from "../../types";

export interface PunishmentStatsResponse extends HypixelResponse {
    watchdog_lastMinute?: number;
    staff_rollingDaily?: number;
    watchdog_total?: number;
    watchdog_rollingDaily?: number;
    staff_total?: number;
}
