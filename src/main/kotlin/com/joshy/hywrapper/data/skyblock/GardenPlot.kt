package com.joshy.hywrapper.data.skyblock

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
enum class GardenPlot(val cleanName: String, val id: Int) {
    @SerialName("beginner_1")
    BEGINNER_1("Beginner 1", 1),

    @SerialName("beginner_2")
    BEGINNER_2("Beginner 2", 2),

    @SerialName("beginner_3")
    BEGINNER_3("Beginner 3", 3),

    @SerialName("beginner_4")
    BEGINNER_4("Beginner 4", 4),

    @SerialName("intermediate_1")
    INTERMEDIATE_1("Intermediate 1", 5),

    @SerialName("intermediate_2")
    INTERMEDIATE_2("Intermediate 2", 6),

    @SerialName("intermediate_3")
    INTERMEDIATE_3("Intermediate 3", 7),

    @SerialName("intermediate_4")
    INTERMEDIATE_4("Intermediate 4", 8),

    @SerialName("advanced_1")
    ADVANCED_1("Advanced 1", 9),

    @SerialName("advanced_2")
    ADVANCED_2("Advanced 2", 10),

    @SerialName("advanced_3")
    ADVANCED_3("Advanced 3", 11),

    @SerialName("advanced_4")
    ADVANCED_4("Advanced 4", 12),

    @SerialName("advanced_5")
    ADVANCED_5("Advanced 5", 13),

    @SerialName("advanced_6")
    ADVANCED_6("Advanced 6", 14),

    @SerialName("advanced_7")
    ADVANCED_7("Advanced 7", 15),

    @SerialName("advanced_8")
    ADVANCED_8("Advanced 8", 16),

    @SerialName("advanced_9")
    ADVANCED_9("Advanced 9", 17),

    @SerialName("advanced_10")
    ADVANCED_10("Advanced 10", 18),

    @SerialName("advanced_11")
    ADVANCED_11("Advanced 11", 19),

    @SerialName("advanced_12")
    ADVANCED_12("Advanced 12", 20),

    @SerialName("expert_1")
    EXPERT_1("Expert 1", 21),

    @SerialName("expert_2")
    EXPERT_2("Expert 2", 22),

    @SerialName("expert_3")
    EXPERT_3("Expert 3", 23),

    @SerialName("expert_4")
    EXPERT_4("Expert 4", 24)
}