from api import NPCBazaarFlip

flips = [
  # Adventurer
  NPCBazaarFlip("Rotten Flesh", "ROTTEN_FLESH", 8, "Adventurer in Bazaar Alley"),
  NPCBazaarFlip("Bone", "BONE", 8, "Adventurer in Bazaar Alley"),
  NPCBazaarFlip("Gunpowder", "SULPHUR", 10, "Adventurer in Bazaar Alley"),
  NPCBazaarFlip("String", "STRING", 10, "Adventurer in Bazaar Alley"),
  NPCBazaarFlip("Slimeball", "SLIME_BALL", 14, "Adventurer in Bazaar Alley"),
  NPCBazaarFlip("Oak Wood", "LOG", 5, "Lumber Merchant in Bazaar Alley"),
  NPCBazaarFlip("Dark Oak Wood", "LOG_2:1", 5, "Lumber Merchant in Bazaar Alley"),
  NPCBazaarFlip("Jungle Wood", "LOG:3", 5, "Lumber Merchant in Bazaar Alley"),
  NPCBazaarFlip("Acacia Wood", "LOG_2", 5, "Lumber Merchant in Bazaar Alley"),
  NPCBazaarFlip("Spruce Wood", "LOG:1", 5, "Lumber Merchant in Bazaar Alley"),
  NPCBazaarFlip("Birch Wood", "LOG:2", 5, "Lumber Merchant in Bazaar Alley"),
  # you start here
  NPCBazaarFlip("Coal", "COAL", 4, "Mine Merchant in Bazaar Alley"),
  NPCBazaarFlip("Iron Ingot", "IRON_INGOT", 5.5, "Mine Merchant in Bazaar Alley"),
  NPCBazaarFlip("Melon Slice", "MELON", 3, "Farm Merchant in the Central Hub"),
  # NPCBazaarFlip("Wheat", "SLIMEBALL", 55555555, "Farm Merchant in the Central Hub"),
  # NPCBazaarFlip("Potato", "SLIMEBALL", 55555555, "Farm Merchant in the Central Hub"),
  # NPCBazaarFlip("Carrot", "SLIMEBALL", 55555555, "Farm Merchant in the Central Hub"),
  # NPCBazaarFlip("Sand", "SLIMEBALL", 55555555, "Farm Merchant in the Central Hub"),
  # NPCBazaarFlip("Cocoa Beans", "SLIMEBALL", 55555555, "Farm Merchant in the Central Hub"),
  # NPCBazaarFlip("Sugar Cane", "SLIMEBALL", 55555555, "Farm Merchant in the Central Hub"),
  # NPCBazaarFlip("Pumpkin", "SLIMEBALL", 55555555, "Farm Merchant in the Central Hub"),
  # i continue here
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
]
