export interface PlayerInventory {
    bag_contents?: BagContents;
    inv_contents?: InventoryObject;
    ender_chest_contents?: InventoryObject;
    backpack_icons?: Record<string, InventoryObject>;
    inv_armor?: InventoryObject;
    equipment_contents?: InventoryObject;
    personal_vault_contents?: InventoryObject;
    wardrobe_equipped_slot?: number;
    backpack_contents?: Record<string, InventoryObject>;
    /** TODO enum */
    sacks_counts?: Record<string, number>;
    wardrobe_contents?: InventoryObject;
}

export interface BagContents {
    sacks_bag?: InventoryObject;
    potion_bag?: InventoryObject;
    talisman_bag?: InventoryObject;
    fishing_bag?: InventoryObject;
    quiver?: InventoryObject;
}

export interface InventoryObject {
    type?: number;
    data?: string;
}
