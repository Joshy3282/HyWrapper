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

@Serializable
data class GardenResponse(
    override val success: Boolean = false,
    override val cause: String? = null,

    val garden: Garden? = null

) : HypixelResponse {
    @Transient
    override var rateLimit: RateLimit? = null
}

@Serializable
data class Garden(
    val uuid: String = "",
    @SerialName("unlocked_plots_ids")
    val unlockedPlots: List<GardenPlot> = emptyList(),
    @SerialName("commission_data")
    val commissionData: CommissionData? = null,
    @SerialName("resources_collected")
    val resourcesCollected: Map<GardenResource, Long> = emptyMap(),
    @SerialName("garden_experience")
    val gardenExperience: Double = 0.0,
    // TODO active_commissions
    @SerialName("composter_data")
    val composterData: ComposterData? = null,
    @SerialName("selected_barn_skin")
    val selectedBarnSkin: String = "",
    @SerialName("crop_upgrade_levels")
    val cropUpgradeLevels: Map<GardenResource, Int> = emptyMap(),
    @SerialName("garden_upgrades")
    val gardenUpgrades: Map<GardenUpgrade, Int> = emptyMap(),
    @SerialName("unlocked_barn_skins")
    val unlockedBarnSkins: List<String> = emptyList(), // TODO enum?
    @SerialName("greenhouse_slots")
    val greenhouseSlots: List<GreenhouseCoordinate> = emptyList(),
    @SerialName("last_growth_stage_time")
    val lastGrowthStageTime: Long = 0L
)

@Serializable
data class CommissionData(
    val visits: Map<Visitor, Int> = emptyMap(),
    val completed: Map<Visitor, Int> = emptyMap(),
    @SerialName("total_completed")
    val totalCompleted: Int = 0,
    @SerialName("unique_npcs_served")
    val uniqueNpcsServed: Int = 0
)

@Serializable
data class ComposterData(
    @SerialName("organic_matter")
    val organicMatter: Double = 0.0,
    @SerialName("fuel_units")
    val fuelUnits: Double = 0.0,
    @SerialName("compost_units")
    val compostUnits: Int = 0,
    @SerialName("compost_items")
    val compostItems: Int = 0,
    @SerialName("conversion_ticks")
    val conversionTicks: Int = 0,
    @SerialName("last_save")
    val lastSave: Long? = 0,
    val upgrades: ComposterUpgrades? = null,
)

@Serializable
data class ComposterUpgrades(
    val speed: Int = 0,
    @SerialName("multi_drop")
    val multiDrop: Int = 0,
    @SerialName("fuel_cap")
    val fuelCap: Int = 0,
    @SerialName("organic_matter_cap")
    val organicMatterCap: Int = 0,
    @SerialName("cost_reduction")
    val costReduction: Int = 0
)

@Serializable
data class GreenhouseCoordinate(
    val x: Int = 0,
    val y: Int = 0
)