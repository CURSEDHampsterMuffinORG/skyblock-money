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
  NPCBazaarFlip(
    "Redstone",
    "REDSTONE",
    4,
    "Mad Redstone Engineer in the Basement of the Builder's House",
  ),
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
  BazaarNPCFlip("Wheat", 1.0),
  BazaarNPCFlip("Enchanted Bread", 60.0),
  BazaarNPCFlip("Hay Bale", 9.0),
  BazaarNPCFlip("Enchanted Hay Bale", 1300.0),
  BazaarNPCFlip("Tightly-Tied Hay Bale", 187200.0, id="TIGHTLY_TIED_HAY_BALE"),
  BazaarNPCFlip("Seeds", 0.5),
  BazaarNPCFlip("Enchanted Seeds", 80.0),
  # Carrots
  BazaarNPCFlip("Carrot", 1.0),
  BazaarNPCFlip("Enchanted Carrot", 160.0),
  BazaarNPCFlip("Enchanted Carrot on a Stick", 10240.0),
  BazaarNPCFlip("Enchanted Golden Carrot", 20608.0),
  # Potatoes and pumpkins
  BazaarNPCFlip("Potato", 1.0),
  BazaarNPCFlip("Enchanted Potato", 160.0),
  BazaarNPCFlip("Enchanted Baked Potato", 25600.0),
  BazaarNPCFlip("Pumpkin", 4.0),
  BazaarNPCFlip("Enchanted Pumpkin", 640.0),
  BazaarNPCFlip("Polished Pumpkin", 102400.0, id="POLISHED_PUMPKIN"),
  # Melons
  BazaarNPCFlip("Melon", 0.5),
  BazaarNPCFlip("Enchanted Melon", 160.0),
  BazaarNPCFlip("Enchanted Glistering Melon", 1024.0),
  BazaarNPCFlip("Enchanted Melon Block", 25600.0),
  # Red mushrooms
  BazaarNPCFlip("Red Mushroom", 4.0),
  BazaarNPCFlip("Enchanted Red Mushroom", 640.0),
  BazaarNPCFlip("Red Mushroom Block", 4.0),
  BazaarNPCFlip("Enchanted Red Mushroom Block", 2300.0),
  # Brown mushrooms
  BazaarNPCFlip("Brown Mushroom", 4.0),
  BazaarNPCFlip("Enchanted Brown Mushroom", 640.0),
  BazaarNPCFlip("Brown Mushroom Block", 4.0),
  BazaarNPCFlip("Enchanted Brown Mushroom Block", 2300.0),
  # Cocoa and cactus
  BazaarNPCFlip("Cocoa Beans", 3.0),
  BazaarNPCFlip("Enchanted Cocoa Beans", 480.0, id="ENCHANTED_COCOA"),
  BazaarNPCFlip("Enchanted Cookie", 61472.0),
  BazaarNPCFlip("Cactus", 1.0),
  BazaarNPCFlip("Enchanted Cactus Green", 160.0),
  BazaarNPCFlip("Enchanted Cactus", 25600.0),
  # Sugar cane
  BazaarNPCFlip("Sugar Cane", 2.0),
  BazaarNPCFlip("Enchanted Sugar", 320.0),
  BazaarNPCFlip("Enchanted Paper", 384.0),
  BazaarNPCFlip("Enchanted Sugar Cane", 51200.0),
  # Leather and beef
  BazaarNPCFlip("Leather", 3.0),
  BazaarNPCFlip("Enchanted Leather", 1700.0),
  BazaarNPCFlip("Raw Beef", 4.0),
  BazaarNPCFlip("Enchanted Raw Beef", 640.0),
  # Pork
  BazaarNPCFlip("Raw Porkchop", 5.0),
  BazaarNPCFlip("Enchanted Pork", 800.0),
  BazaarNPCFlip("Enchanted Grilled Pork", 128000.0),
  # Cluck bois
  BazaarNPCFlip("Raw Chicken", 4.0),
  BazaarNPCFlip("Enchanted Raw Chicken", 640.0),
  BazaarNPCFlip("Enchanted Egg", 432.0),
  BazaarNPCFlip("Enchanted Cake", 2700.0),
  BazaarNPCFlip("Feather", 3.0),
  BazaarNPCFlip("Enchanted Feather", 480.0),
  # Mutton
  BazaarNPCFlip("Mutton", 5.0),
  BazaarNPCFlip("Enchanted Mutton", 800.0),
  BazaarNPCFlip("Enchanted Cooked Mutton", 128000.0),
  # Stupid jump bois
  BazaarNPCFlip("Raw Rabbit", 4.0),
  BazaarNPCFlip("Enchanted Raw Rabbit", 640.0),
  BazaarNPCFlip("Rabbit's Foot", 5.0),
  BazaarNPCFlip("Enchanted Rabbit Foot", 800.0),
  BazaarNPCFlip("Rabbit Hide", 5.0),
  BazaarNPCFlip("Enchanted Rabbit Hide", 2880.0),
  # Wart
  BazaarNPCFlip("Nether Wart", 3.0),
  BazaarNPCFlip("Enchanted Nether Wart", 480.0),
  BazaarNPCFlip("Mutant Nether Wart", 76800.0, id="MUTANT_NETHER_STALK"),
  # Mining time
  # Cobble
  BazaarNPCFlip("Cobblestone", 1.0),
  BazaarNPCFlip("Enchanted Cobblestone", 160.0),
  # Coal
  BazaarNPCFlip("Coal", 2.0),
  BazaarNPCFlip("Enchanted Coal", 320.0),
  BazaarNPCFlip("Enchanted Charcoal", 320.0),
  BazaarNPCFlip("Enchanted Block of Coal", 51000.0),
  # Iron
  BazaarNPCFlip("Iron Ingot", 3.0),
  BazaarNPCFlip("Enchanted Iron", 480.0),
  BazaarNPCFlip("Enchanted Iron Block", 76800.0),
  # Gold
  BazaarNPCFlip("Gold Ingot", 4.0),
  BazaarNPCFlip("Enchanted Gold", 640.0),
  BazaarNPCFlip("Enchanted Gold Block", 102000.0),
  # Diamond
  BazaarNPCFlip("Diamond", 8.0),
  BazaarNPCFlip("Enchanted Diamond", 1280.0),
  BazaarNPCFlip("Enchanted Diamond Block", 204800.0),
  BazaarNPCFlip("Refined Diamond", 4096.0),
  # Lapis
  BazaarNPCFlip("Lapis Lazuli", 1.0),
  BazaarNPCFlip("Enchanted Lapis Lazuli", 160.0),
  BazaarNPCFlip("Enchanted Lapis Block", 25600.0),
  # Gemstone time; im gonna be kinda lazy
]
gemstone_types = ["RUBY", "AMETHYST", "JADE", "SAPPHIRE", "AMBER", "TOPAZ", "JASPER"]
for type in gemstone_types:
  flips.append(
    BazaarNPCFlip(f"Rough {type.capitalize()} Gemstone", 8, id=f"ROUGH_{type}_GEM")
  )
  flips.append(
    BazaarNPCFlip(f"Flawed {type.capitalize()} Gemstone", 640, id=f"FLAWED_{type}_GEM")
  )
  flips.append(
    BazaarNPCFlip(f"Fine {type.capitalize()} Gemstone", 25600, id=f"FINE_{type}_GEM")
  )
  flips.append(
    BazaarNPCFlip(
      f"Flawless {type.capitalize()} Gemstone", 512000, id=f"FLAWLESS_{type}_GEM"
    )
  )
  # Tell me in the Discord if you know how much Perfect sells to NPCs for
more_flips = [
  # Emerald
  BazaarNPCFlip("Emerald", 6.0),
  BazaarNPCFlip("Enchanted Emerald", 960.0),
  BazaarNPCFlip("Enchanted Emerald Block", 153600.0),
  # Redstone
  BazaarNPCFlip("Redstone", 1.0),
  BazaarNPCFlip("Enchanted Redstone", 160.0),
  BazaarNPCFlip("Enchanted Redstone Block", 25600.0),
  # Quartz
  BazaarNPCFlip("Quartz", 4.0),
  BazaarNPCFlip("Enchanted Quartz", 640.0),
  BazaarNPCFlip("Enchanted Quartz Block", 102000.0),
  # Obby
  BazaarNPCFlip("Obsidian", 9.0),
  BazaarNPCFlip("Enchanted Obsidian", 1920.0),
  # Glowstone
  BazaarNPCFlip("Glowstone Dust", 2.0),
  BazaarNPCFlip("Enchanted Glowstone Dust", 320.0),
  BazaarNPCFlip("Enchanted Glowstone", 61000.0),
  BazaarNPCFlip("Enchanted Redstone Lamp", 30720.0),
  # Flint
  BazaarNPCFlip("Flint", 4.0),
  BazaarNPCFlip("Enchanted Flint", 640.0),
  BazaarNPCFlip("Gravel", 3.0),
  # Hard Stone
  BazaarNPCFlip("Hard Stone", 1.0),
  BazaarNPCFlip("Enchanted Hard Stone", 576.0),
  BazaarNPCFlip("Concentrated Stone", 331776.0),
  # Ice
  BazaarNPCFlip("Ice", 0.5),
  BazaarNPCFlip("Packed Ice", 4.5),
  BazaarNPCFlip("Enchanted Ice", 80.0),
  BazaarNPCFlip("Enchanted Packed Ice", 12800.0),
  # Netherrack
  BazaarNPCFlip("Netherrack", 1.0),
  BazaarNPCFlip("Enchanted Netherrack", 160.0),
  # Sand
  BazaarNPCFlip("Sand", 2.0),
  BazaarNPCFlip("Enchanted Sand", 320.0),
  # Snow
  BazaarNPCFlip("Snowball", 1.0),
  BazaarNPCFlip("Snow Block", 4.0),
  BazaarNPCFlip("Enchanted Snow Block", 600.0),
  # Mithril
  BazaarNPCFlip("Mithril", 10, id="MITHRIL_ORE"),
  BazaarNPCFlip("Enchanted Mithril", 1600.0),
  BazaarNPCFlip("Refined Mithril", 256000.0),
  BazaarNPCFlip("Titanium", 20, id="TITANIUM_ORE"),
  BazaarNPCFlip("Enchanted Titanium", 3200.0),
  BazaarNPCFlip("Refined Titanium", 51200.0),
  BazaarNPCFlip("Starfall", 15.0),
  BazaarNPCFlip("Treasurite", 5000.0),
]
flips += more_flips
