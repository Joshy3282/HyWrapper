import { HypixelResponse } from "../../types";
import { MuseumItem as MuseumItemEnum } from "../../data/skyblock/MuseumItem";

export interface MuseumResponse extends HypixelResponse {
    members?: Record<string, MuseumMember>;
}

export interface MuseumMember {
    value?: number;
    appraisal?: boolean;
    items?: Record<MuseumItemEnum, MuseumItemInfo>;
    special?: SpecialItemInfo[];
}

export interface MuseumItemInfo {
    donated_time?: number;
    featured_slot?: string;
    borrowing?: boolean;
    items?: MuseumItemData;
}

export interface SpecialItemInfo {
    donated_time?: number;
    items?: MuseumItemData;
}

export interface MuseumItemData {
    type?: number;
    data?: string;
}
