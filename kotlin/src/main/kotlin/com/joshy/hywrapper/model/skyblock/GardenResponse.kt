package com.joshy.hywrapper.model.skyblock

import com.joshy.hywrapper.data.skyblock.GardenPlot
import com.joshy.hywrapper.data.skyblock.GardenResource
import com.joshy.hywrapper.data.skyblock.GardenUpgrade
import com.joshy.hywrapper.data.skyblock.Visitor
import com.joshy.hywrapper.model.HypixelResponse
import com.joshy.hywrapper.model.RateLimit
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient
import kotlinx.serialization.json.JsonElement

/**
 * Information about a player's Garden.
 *
 * @property success Whether the request was successful.
 * @property cause The cause of the error, if the request failed.
 * @property garden Information about the Garden.
 * */
@Serializable
data class GardenResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val garden: Garden? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

/**
 * Information about a player's Garden.
 *
 * @property uuid Garden UUID.
 * @property unlockedPlots A list of [GardenPlot] that have been unlocked.
 * @property commissionData Information about visitor commissions.
 * @property resourcesCollected The amount of each [GardenResource] collected
 * @property gardenExperience The amount of garden experience gained
 * @property activeCommissions A list of active visitor commissions
 * @property composterData Information about the Garden's composter.
 * @property selectedBarnSkin The current selected Barn skin
 * @property cropUpgradeLevels The upgrade level of each [GardenResource].
 * @property gardenUpgrades The upgrade level of each [GardenUpgrade].
 * @property unlockedBarnSkins A list of all unlocked Barn skins.
 * @property greenhouseSlots Unknown.
 * @property lastGrowthStageTime Timestamp of the last Greenhouse growth.
 * */
@Serializable
data class Garden(
    val uuid: String? = null,
    @SerialName("unlocked_plots_ids")
    val unlockedPlots: List<GardenPlot>? = null,
    @SerialName("commission_data")
    val commissionData: CommissionData? = null,
    @SerialName("resources_collected")
    val resourcesCollected: Map<GardenResource, Long>? = null,
    @SerialName("garden_experience")
    val gardenExperience: Double? = null,
    @SerialName("active_commissions")
    val activeCommissions: List<JsonElement>? = null, // TODO empty in tests
    @SerialName("composter_data")
    val composterData: ComposterData? = null,
    @SerialName("selected_barn_skin")
    val selectedBarnSkin: String? = null, // TODO change to enum
    @SerialName("crop_upgrade_levels")
    val cropUpgradeLevels: Map<GardenResource, Int>? = null,
    @SerialName("garden_upgrades")
    val gardenUpgrades: Map<GardenUpgrade, Int>? = null,
    @SerialName("unlocked_barn_skins")
    val unlockedBarnSkins: List<String>? = null, // TODO change to enum
    @SerialName("greenhouse_slots")
    val greenhouseSlots: List<GreenhouseCoordinate>? = null, // TODO unknown
    @SerialName("last_growth_stage_time")
    val lastGrowthStageTime: Long? = null,
)

/**
 * Information about visitor commissions.
 *
 * @property visits A list of how many times each visitor has visited.
 * @property completed A list of how many times each visitor's commission has been completed.
 * @property totalCompleted Total amount of visitor commissions completed.
 * @property uniqueVisitorsServed How many unique visitors' commissions have been completed.
 * */
@Serializable
data class CommissionData(
    val visits: Map<Visitor, Int>? = null,
    val completed: Map<Visitor, Int>? = null,
    @SerialName("total_completed")
    val totalCompleted: Int? = null,
    @SerialName("unique_npcs_served")
    val uniqueVisitorsServed: Int? = null,
)


/**
 * Information about the Garden's composter.
 *
 * @property organicMatter The amount of organic matter currently in the composter.
 * @property fuel The amount of fuel currently in the composter.
 * @property compostUnits Either this or composteItems are the amount of compost in the composter, the other is unknown.
 * @property compostItems Either this or composteUnits are the amount of compost in the composter, the other is unknown.
 * @property conversionTicks Unknown.
 * @property lastSave The timestamp the composter was last modified (eg; fuel put in, compost taken).
 * @property upgrades Upgrades levels for the composter.
 * */
@Serializable
data class ComposterData(
    @SerialName("organic_matter")
    val organicMatter: Double? = null,
    @SerialName("fuel_units")
    val fuel: Double? = null,
    @SerialName("compost_units")
    val compostUnits: Int? = null,
    @SerialName("compost_items")
    val compostItems: Int? = null,
    @SerialName("conversion_ticks")
    val conversionTicks: Int? = null,
    @SerialName("last_save")
    val lastSave: Long? = null,
    val upgrades: ComposterUpgrades? = null,
)

/**
 * Upgrade levels for the composter.
 *
 * @property speed The speed upgrade of the composter.
 * @property multiDrop The multi drop upgrade of the composter.
 * @property fuelCap The fuel cap upgrade of the composter.
 * @property organicMatterCap The organic matter cap of the composter.
 * @property costReduction The cost reduction cap of the composter.
 * */
@Serializable
data class ComposterUpgrades(
    val speed: Int? = null,
    @SerialName("multi_drop")
    val multiDrop: Int? = null,
    @SerialName("fuel_cap")
    val fuelCap: Int? = null,
    @SerialName("organic_matter_cap")
    val organicMatterCap: Int? = null,
    @SerialName("cost_reduction")
    val costReduction: Int? = null,
)

@Serializable
data class GreenhouseCoordinate(
    val x: Int? = null,
    val y: Int? = null,
)
