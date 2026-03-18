package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import com.joshy.hywrapper.model.skyblock.profile.Rift
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class ProfileResponse(
    override val success: Boolean = false,
    override val cause: String? = null,
    val items: List<NewsItem> = emptyList(),
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class Profile(
    @SerialName("profile_id")
    val profileId: String = "",
    @SerialName("community_upgrades")
    val communityUpgrades: CommunityUpgrades? = null,
    val members: Map<String, MemberData> = emptyMap(),
    val banking: Banking? = null,
)

@Serializable
data class MemberData(
    val rift: Rift? = null,
)

@Serializable
data class CommunityUpgrades(
    @SerialName("currently_upgrading")
    val currentlyUpgrading: String = "",
    @SerialName("upgrade_states")
    val upgradeStates: List<UpgradeState> = emptyList(),
)

@Serializable
data class UpgradeState(
    val upgrade: String = "",
    val tier: Int = 1,
    @SerialName("started_ms")
    val startedMs: Long = 0L,
    @SerialName("started_by")
    val startedBy: String = "",
    @SerialName("claimed_by")
    val claimedBy: String = "",
)

@Serializable
data class Banking(
    val balance: Double = 0.0,
    val transactions: List<Transaction> = emptyList(),
)

@Serializable
data class Transaction(
    val amount: Double = 0.0,
    val timestamp: Long = 0L,
    val action: String = "",
    @SerialName("initiator_name")
    val initiatorName: String = "",
)
