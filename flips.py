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
  BazaarNPCFlip("Wheat", None, 1.0),
  BazaarNPCFlip("Enchanted Bread", None, 60.0),
  BazaarNPCFlip("Hay Bale", "HAY_BLOCK", 9.0),
  BazaarNPCFlip("Enchanted Hay Bale", "ENCHANTED_HAY_BLOCK", 1300.0),
  BazaarNPCFlip("Tightly-Tied Hay Bale", "TIGHTLY_TIED_HAY_BALE", 187200.0),
  BazaarNPCFlip("Seeds", None, 0.5),
  BazaarNPCFlip("Enchanted Seeds", None, 80.0),
  # Carrots
  BazaarNPCFlip("Carrot", "CARROT_ITEM", 1.0),
  BazaarNPCFlip("Enchanted Carrot", None, 160.0),
  BazaarNPCFlip("Enchanted Carrot on a Stick", "ENCHANTED_CARROT_STICK", 10240.0),
  BazaarNPCFlip("Enchanted Golden Carrot", None, 20608.0),
  # Potatoes and pumpkins
  BazaarNPCFlip("Potato", "POTATO_ITEM", 1.0),
  BazaarNPCFlip("Enchanted Potato", None, 160.0),
  BazaarNPCFlip("Enchanted Baked Potato", None, 25600.0),
  BazaarNPCFlip("Pumpkin", None, 4.0),
  BazaarNPCFlip("Enchanted Pumpkin", None, 640.0),
  BazaarNPCFlip("Polished Pumpkin", "POLISHED_PUMPKIN", 102400.0),
  # Melons
  BazaarNPCFlip("Melon", None, 0.5),
  BazaarNPCFlip("Enchanted Melon", None, 160.0),
  BazaarNPCFlip("Enchanted Glistering Melon", None, 1024.0),
  BazaarNPCFlip("Enchanted Melon Block", None, 25600.0),
  # Red mushrooms
  BazaarNPCFlip("Red Mushroom", None, 4.0),
  BazaarNPCFlip("Enchanted Red Mushroom", None, 640.0),
  BazaarNPCFlip("Red Mushroom Block", "HUGE_MUSHROOM_2", 4.0),
  BazaarNPCFlip("Enchanted Red Mushroom Block", "ENCHANTED_HUGE_MUSHROOM_2", 2300.0),
  # Brown mushrooms
  BazaarNPCFlip("Brown Mushroom", None, 4.0),
  BazaarNPCFlip("Enchanted Brown Mushroom", None, 640.0),
  BazaarNPCFlip("Brown Mushroom Block", "HUGE_MUSHROOM_1", 4.0),
  BazaarNPCFlip("Enchanted Brown Mushroom Block", "ENCHANTED_HUGE_MUSHROOM_1", 2300.0),
  # Cocoa and cactus
  BazaarNPCFlip("Cocoa Beans", "INK_SACK:3", 3.0),
  BazaarNPCFlip("Enchanted Cocoa Beans", "ENCHANTED_COCOA", 480.0),
  BazaarNPCFlip("Enchanted Cookie", None, 61472.0),
  BazaarNPCFlip("Cactus", None, 1.0),
  BazaarNPCFlip("Enchanted Cactus Green", None, 160.0),
  BazaarNPCFlip("Enchanted Cactus", None, 25600.0),
  # Sugar cane
  BazaarNPCFlip("Sugar Cane", None, 2.0),
  BazaarNPCFlip("Enchanted Sugar", None, 320.0),
  BazaarNPCFlip("Enchanted Paper", None, 384.0),
  BazaarNPCFlip("Enchanted Sugar Cane", None, 51200.0),
  # Leather and beef
  BazaarNPCFlip("Leather", None, 3.0),
  BazaarNPCFlip("Enchanted Leather", None, 1700.0),
  BazaarNPCFlip("Raw Beef", None, 4.0),
  BazaarNPCFlip("Enchanted Raw Beef", None, 640.0),
  # Pork
  BazaarNPCFlip("Raw Porkchop", "PORK", 5.0),
  BazaarNPCFlip("Enchanted Pork", None, 800.0),
  BazaarNPCFlip("Enchanted Grilled Pork", None, 128000.0),
  # Cluck bois
  BazaarNPCFlip("Raw Chicken", None, 4.0),
  BazaarNPCFlip("Enchanted Raw Chicken", None, 640.0),
  BazaarNPCFlip("Enchanted Egg", None, 432.0),
  BazaarNPCFlip("Enchanted Cake", None, 2700.0),
  BazaarNPCFlip("Feather", None, 3.0),
  BazaarNPCFlip("Enchanted Feather", None, 480.0),
  # Mutton
  BazaarNPCFlip("Mutton", None, 5.0),
  BazaarNPCFlip("Enchanted Mutton", None, 800.0),
  BazaarNPCFlip("Enchanted Cooked Mutton", None, 128000.0),
  # Stupid jump bois
  BazaarNPCFlip("Raw Rabbit", "RABBIT", 4.0),
  BazaarNPCFlip("Enchanted Raw Rabbit", "ENCHANTED_RABBIT", 640.0),
  BazaarNPCFlip("Rabbit's Foot", "RABBIT_FOOT", 5.0),
  BazaarNPCFlip("Enchanted Rabbit Foot", None, 800.0),
  BazaarNPCFlip("Rabbit Hide", None, 5.0),
  BazaarNPCFlip("Enchanted Rabbit Hide", None, 2880.0),
  # Wart
  BazaarNPCFlip("Nether Wart", "NETHER_STALK", 3.0),
  BazaarNPCFlip("Enchanted Nether Wart", "ENCHANTED_NETHER_STALK", 480.0),
  BazaarNPCFlip("Mutant Nether Wart", "MUTANT_NETHER_STALK", 76800.0),
  # Mining time
  # Cobble
  BazaarNPCFlip("Cobblestone", None, 1.0),
  BazaarNPCFlip("Enchanted Cobblestone", None, 160.0),
  # Coal
  BazaarNPCFlip("Coal", None, 2.0),
  BazaarNPCFlip("Enchanted Coal", None, 320.0),
  BazaarNPCFlip("Enchanted Charcoal", None, 320.0),
  BazaarNPCFlip("Enchanted Block of Coal", "ENCHANTED_COAL_BLOCK", 51000.0),
  # Iron
  BazaarNPCFlip("Iron Ingot", None, 3.0),
  BazaarNPCFlip("Enchanted Iron", None, 480.0),
  BazaarNPCFlip("Enchanted Iron Block", None, 76800.0),
  # Gold
  BazaarNPCFlip("Gold Ingot", None, 4.0),
  BazaarNPCFlip("Enchanted Gold", None, 640.0),
  BazaarNPCFlip("Enchanted Gold Block", None, 102000.0),
  # Diamond
  BazaarNPCFlip("Diamond", None, 8.0),
  BazaarNPCFlip("Enchanted Diamond", None, 1280.0),
  BazaarNPCFlip("Enchanted Diamond Block", None, 204800.0),
  BazaarNPCFlip("Refined Diamond", None, 4096.0),
  # Lapis
  BazaarNPCFlip("Lapis Lazuli", "INK_SACK:4", 1.0),
  BazaarNPCFlip("Enchanted Lapis Lazuli", None, 160.0),
  BazaarNPCFlip("Enchanted Lapis Block", "ENCHANTED_LAPIS_LAZULI_BLOCK", 25600.0),
]
