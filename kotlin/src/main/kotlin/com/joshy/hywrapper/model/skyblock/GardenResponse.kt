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

@Serializable
data class GardenResponse(
    override val success: Boolean? = null,
    override val cause: String? = null,
    val garden: Garden? = null,
) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

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
    val activeCommissions: List<JsonElement>? = null,
    @SerialName("composter_data")
    val composterData: ComposterData? = null,
    @SerialName("selected_barn_skin")
    val selectedBarnSkin: String? = null,
    @SerialName("crop_upgrade_levels")
    val cropUpgradeLevels: Map<GardenResource, Int>? = null,
    @SerialName("garden_upgrades")
    val gardenUpgrades: Map<GardenUpgrade, Int>? = null,
    @SerialName("unlocked_barn_skins")
    val unlockedBarnSkins: List<String>? = null,
    @SerialName("greenhouse_slots")
    val greenhouseSlots: List<GreenhouseCoordinate>? = null,
    @SerialName("last_growth_stage_time")
    val lastGrowthStageTime: Long? = null,
)

@Serializable
data class CommissionData(
    val visits: Map<Visitor, Int>? = null,
    val completed: Map<Visitor, Int>? = null,
    @SerialName("total_completed")
    val totalCompleted: Int? = null,
    @SerialName("unique_npcs_served")
    val uniqueNpcsServed: Int? = null,
)

@Serializable
data class ComposterData(
    @SerialName("organic_matter")
    val organicMatter: Double? = null,
    @SerialName("fuel_units")
    val fuelUnits: Double? = null,
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
