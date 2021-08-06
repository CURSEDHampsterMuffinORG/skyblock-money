from api import NPCBazaarFlip, BazaarNPCFlip

flips = [
  # Adventurer
  NPCBazaarFlip("Rotten Flesh", "ROTTEN_FLESH", 8, "Adventurer in Bazaar Alley"),
  NPCBazaarFlip("Bone", "BONE", 8, "Adventurer in Bazaar Alley"),
  NPCBazaarFlip("Gunpowder", "SULPHUR", 10, "Adventurer in Bazaar Alley"),
  NPCBazaarFlip("String", "STRING", 10, "Adventurer in Bazaar Alley"),
  NPCBazaarFlip("Slimeball", "SLIME_BALL", 14, "Adventurer in Bazaar Alley"),
  NPCBazaarFlip("Oak Wood", "LOG", 5, "Lumber Merchant in Bazaar Alley"),
  # Lumber merchant
  NPCBazaarFlip("Dark Oak Wood", "LOG_2:1", 5, "Lumber Merchant in Bazaar Alley"),
  NPCBazaarFlip("Jungle Wood", "LOG:3", 5, "Lumber Merchant in Bazaar Alley"),
  NPCBazaarFlip("Acacia Wood", "LOG_2", 5, "Lumber Merchant in Bazaar Alley"),
  NPCBazaarFlip("Spruce Wood", "LOG:1", 5, "Lumber Merchant in Bazaar Alley"),
  NPCBazaarFlip("Birch Wood", "LOG:2", 5, "Lumber Merchant in Bazaar Alley"),
  # Mine merchant
  NPCBazaarFlip("Cobblestone", "COBBLESTONE", 3, "Mine Merchant nearby the Coal Mine"),
  NPCBazaarFlip("Coal", "COAL", 4, "Mine Merchant nearby the Coal Mine"),
  # Farm merchant
  NPCBazaarFlip("Melon Slice", "MELON", 3, "Farm Merchant in the Central Hub"),
  NPCBazaarFlip("Wheat", "WHEAT", 2.33, "Farm Merchant in the Central Hub"),
  NPCBazaarFlip("Potato", "POTATO_ITEM", 2.33, "Farm Merchant in the Central Hub"),
  NPCBazaarFlip("Carrot", "CARROT_ITEM", 2.33, "Farm Merchant in the Central Hub"),
  NPCBazaarFlip("Cocoa Beans", "INK_SACK:3", 5, "Farm Merchant in the Central Hub"),
  NPCBazaarFlip("Sugar Cane", "SUGAR_CANE", 5, "Farm Merchant in the Central Hub"),
  NPCBazaarFlip("Pumpkin", "PUMPKIN", 8, "Farm Merchant in the Central Hub"),
  NPCBazaarFlip("Red Mushroom", "RED_MUSHROOM", 12, "Farm Merchant in the Central Hub"),
  NPCBazaarFlip(
    "Brown Mushroom", "BROWN_MUSHROOM", 12, "Farm Merchant in the Central Hub"
  ),
  # Alchemist
  NPCBazaarFlip("Nether Wart", "NETHER_STALK", 10, "Alchemist in the Purple House"),
  NPCBazaarFlip("Rabbit's Foot", "RABBIT_FOOT", 10, "Alchemist in the Purple House"),
  NPCBazaarFlip("Spider Eye", "SPIDER_EYE", 12, "Alchemist in the Purple House"),
  NPCBazaarFlip("Magma Cream", "MAGMA_CREAM", 20, "Alchemist in the Purple House"),
  NPCBazaarFlip("Ghast Tear", "GHAST_TEAR", 200, "Alchemist in the Purple House"),
  # Fish
  NPCBazaarFlip("Raw Fish", "RAW_FISH", 20, "Fish Merchant nearby the Pond"),
  NPCBazaarFlip("Pufferfish", "RAW_FISH:3", 40, "Fish Merchant nearby the Pond"),
  NPCBazaarFlip("Raw Salmon", "RAW_FISH:1", 30, "Fish Merchant nearby the Pond"),
  NPCBazaarFlip("Clownfish", "RAW_FISH:2", 100, "Fish Merchant nearby the Pond"),
  # Builder
  NPCBazaarFlip("Sand", "SAND", 1, "Builder in the Builder's House"),
  NPCBazaarFlip("Ice", "ICE", 1, "Builder in the Builder's House"),
  NPCBazaarFlip("Packed Ice", "PACKED_ICE", 9, "Builder in the Builder's House"),
  # Pat
  NPCBazaarFlip("Gravel", "GRAVEL", 4.33, "Pat in the Graveyard House"),
  NPCBazaarFlip("Flint", "FLINT", 6, "Pat in the Graveyard House"),
  # Gold Mine
  NPCBazaarFlip("Iron Ingot", "IRON_INGOT", 5, "Iron Forger outside the Gold Mine"),
  NPCBazaarFlip("Gold Ingot", "GOLD_INGOT", 5.5, "Gold Forger outside the Gold Mine"),
  # The End # TODO: Account for if user has unlocked End
  NPCBazaarFlip("End Stone", "ENDER_STONE", 10, "Pearl Dealer on the End Island"),
  NPCBazaarFlip("Obsidian", "OBSIDIAN", 50, "Pearl Dealer on the End Island"),
  # Season of Jerry
  NPCBazaarFlip("Ice Bait", "ICE_BAIT", 12, "Sherry on the Season of Jerry Island"),
  # ===================================================================================
  # |                                Bazaar to NPC                                    |
  # ===================================================================================
  # Wheat
  BazaarNPCFlip("Wheat", "WHEAT", 1.0),
  BazaarNPCFlip("Enchanted Bread", "ENCHANTED_BREAD", 60.0),
  BazaarNPCFlip("Hay Bale", "HAY_BLOCK", 9.0),
  BazaarNPCFlip("Enchanted Hay Bale", "ENCHANTED_HAY_BLOCK", 1300.0),
  BazaarNPCFlip("Tightly-Tied Hay Bale", "TIGHTLY_TIED_HAY_BALE", 187200.0),
  BazaarNPCFlip("Seeds", "SEEDS", 0.5),
  BazaarNPCFlip("Enchanted Seeds", "ENCHANTED_SEEDS", 80.0),
  # Carrots
  BazaarNPCFlip("Carrot", "CARROT_ITEM", 1.0),
  BazaarNPCFlip("Enchanted Carrot", "ENCHANTED_CARROT", 160.0),
  BazaarNPCFlip("Enchanted Carrot on a Stick", "ENCHANTED_CARROT_STICK", 10240.0),
  BazaarNPCFlip("Enchanted Golden Carrot", "ENCHANTED_GOLDEN_CARROT", 20608.0),
  # Potatoes and pumpkins
  BazaarNPCFlip("Potato", "POTATO_ITEM", 1.0),
  BazaarNPCFlip("Enchanted Potato", "ENCHANTED_POTATO", 160.0),
  BazaarNPCFlip("Enchanted Baked Potato", "ENCHANTED_BAKED_POTATO", 25600.0),
  BazaarNPCFlip("Pumpkin", "PUMPKIN", 4.0),
  BazaarNPCFlip("Enchanted Pumpkin", "ENCHANTED_PUMPKIN", 640.0),
  # Melons
  BazaarNPCFlip("Melon", "MELON", 0.5),
  BazaarNPCFlip("Enchanted Melon", "ENCHANTED_MELON", 160.0),
  BazaarNPCFlip("Enchanted Glistering Melon", "ENCHANTED_GLISTERING_MELON", 1024.0),
  BazaarNPCFlip("Enchanted Melon Block", "ENCHANTED_MELON_BLOCK", 25600.0),
  # Red mushrooms
  BazaarNPCFlip("Red Mushroom", "RED_MUSHROOM", 4),
  BazaarNPCFlip("Enchanted Red Mushroom", "ENCHANTED_RED_MUSHROOM", 640.0),
  BazaarNPCFlip("Red Mushroom Block", "HUGE_MUSHROOM_2", 4.0),
  BazaarNPCFlip("Enchanted Red Mushroom Block", "ENCHANTED_HUGE_MUSHROOM_2", 2300.0),
  # Brown mushrooms
  BazaarNPCFlip("Brown Mushroom", "BROWN_MUSHROOM", 4),
  BazaarNPCFlip("Enchanted Brown Mushroom", "ENCHANTED_BROWN_MUSHROOM", 640.0),
  BazaarNPCFlip("Brown Mushroom Block", "HUGE_MUSHROOM_1", 4.0),
  BazaarNPCFlip("Enchanted Brown Mushroom Block", "ENCHANTED_HUGE_MUSHROOM_1", 2300.0),
]
