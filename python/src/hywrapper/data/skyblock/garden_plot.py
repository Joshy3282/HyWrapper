from __future__ import annotations

from enum import Enum
from typing import Any, Optional


class GardenPlot(str, Enum):
    BEGINNER_1 = "beginner_1"
    BEGINNER_2 = "beginner_2"
    BEGINNER_3 = "beginner_3"
    BEGINNER_4 = "beginner_4"
    INTERMEDIATE_1 = "intermediate_1"
    INTERMEDIATE_2 = "intermediate_2"
    INTERMEDIATE_3 = "intermediate_3"
    INTERMEDIATE_4 = "intermediate_4"
    ADVANCED_1 = "advanced_1"
    ADVANCED_2 = "advanced_2"
    ADVANCED_3 = "advanced_3"
    ADVANCED_4 = "advanced_4"
    ADVANCED_5 = "advanced_5"
    ADVANCED_6 = "advanced_6"
    ADVANCED_7 = "advanced_7"
    ADVANCED_8 = "advanced_8"
    ADVANCED_9 = "advanced_9"
    ADVANCED_10 = "advanced_10"
    ADVANCED_11 = "advanced_11"
    ADVANCED_12 = "advanced_12"
    EXPERT_1 = "expert_1"
    EXPERT_2 = "expert_2"
    EXPERT_3 = "expert_3"
    EXPERT_4 = "expert_4"

    @property
    def clean_name(self) -> str:
        return _CLEAN_NAMES[self]

    @property
    def id(self) -> int:
        return _IDS[self]

    @classmethod
    def from_id(cls, id: Any) -> Optional[GardenPlot]:
        try:
            return cls(id)
        except ValueError:
            return None


_CLEAN_NAMES = {
    GardenPlot.BEGINNER_1: "Beginner 1",
    GardenPlot.BEGINNER_2: "Beginner 2",
    GardenPlot.BEGINNER_3: "Beginner 3",
    GardenPlot.BEGINNER_4: "Beginner 4",
    GardenPlot.INTERMEDIATE_1: "Intermediate 1",
    GardenPlot.INTERMEDIATE_2: "Intermediate 2",
    GardenPlot.INTERMEDIATE_3: "Intermediate 3",
    GardenPlot.INTERMEDIATE_4: "Intermediate 4",
    GardenPlot.ADVANCED_1: "Advanced 1",
    GardenPlot.ADVANCED_2: "Advanced 2",
    GardenPlot.ADVANCED_3: "Advanced 3",
    GardenPlot.ADVANCED_4: "Advanced 4",
    GardenPlot.ADVANCED_5: "Advanced 5",
    GardenPlot.ADVANCED_6: "Advanced 6",
    GardenPlot.ADVANCED_7: "Advanced 7",
    GardenPlot.ADVANCED_8: "Advanced 8",
    GardenPlot.ADVANCED_9: "Advanced 9",
    GardenPlot.ADVANCED_10: "Advanced 10",
    GardenPlot.ADVANCED_11: "Advanced 11",
    GardenPlot.ADVANCED_12: "Advanced 12",
    GardenPlot.EXPERT_1: "Expert 1",
    GardenPlot.EXPERT_2: "Expert 2",
    GardenPlot.EXPERT_3: "Expert 3",
    GardenPlot.EXPERT_4: "Expert 4",
}

_IDS = {
    GardenPlot.BEGINNER_1: 1,
    GardenPlot.BEGINNER_2: 2,
    GardenPlot.BEGINNER_3: 3,
    GardenPlot.BEGINNER_4: 4,
    GardenPlot.INTERMEDIATE_1: 5,
    GardenPlot.INTERMEDIATE_2: 6,
    GardenPlot.INTERMEDIATE_3: 7,
    GardenPlot.INTERMEDIATE_4: 8,
    GardenPlot.ADVANCED_1: 9,
    GardenPlot.ADVANCED_2: 10,
    GardenPlot.ADVANCED_3: 11,
    GardenPlot.ADVANCED_4: 12,
    GardenPlot.ADVANCED_5: 13,
    GardenPlot.ADVANCED_6: 14,
    GardenPlot.ADVANCED_7: 15,
    GardenPlot.ADVANCED_8: 16,
    GardenPlot.ADVANCED_9: 17,
    GardenPlot.ADVANCED_10: 18,
    GardenPlot.ADVANCED_11: 19,
    GardenPlot.ADVANCED_12: 20,
    GardenPlot.EXPERT_1: 21,
    GardenPlot.EXPERT_2: 22,
    GardenPlot.EXPERT_3: 23,
    GardenPlot.EXPERT_4: 24,
}
