import os, requests, json, time

API_KEY = os.environ["API_KEY"]
ITEMS = json.load(open("skyblock_items.json"))
ITEMS = {friendly["name"]: id for id, friendly in ITEMS.items()}
PRICES = json.load(open("items_prices.json"))
PRICES = {price["name"]: (price["low"] * 3 + price["hi"]) / 4 for price in PRICES}

NPC = "NPC <img src='/adventurer.png' class='npcIcon'></img>"
BAZAAR = "Bazaar <img src='/bazaar.png' class='npcIcon'></img>"
BIN = "BIN <img src='/auction.png' class='npcIcon'></img>"


class User:
  def __init__(self, username, auctions):
    uuid = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}").json()["id"]
    profiles = requests.get(
      "https://api.hypixel.net/skyblock/profiles",
      params={"uuid": uuid},
      headers={"Api-Key": API_KEY},
    )
    self.uuid = uuid
    if len(profiles.json()["profiles"]) > 1:
    self.profiles = max(
      profiles.json()["profiles"],
      key=lambda prof: prof["members"][uuid]["last_save"],
    )
    else:
      self.profiles = profiles.json()["profiles"][0]
    self.user_data = self.profiles["members"][self.uuid]
    self.bank = self.profiles["banking"]["balance"] + self.user_data["coin_purse"]
    self.bazaar = requests.get(
      "https://api.hypixel.net/skyblock/bazaar",
      headers={"Api-Key": API_KEY},
    ).json()["products"]
    if auctions == "true":
      self.ah = []
      initial_data = requests.get(
        "https://api.hypixel.net/skyblock/auctions",
        headers={"Api-Key": API_KEY},
      ).json()
      self.ah += initial_data["auctions"]
      for i in range(1, min(initial_data["totalPages"], 10)):
        time.sleep(1)
        self.ah += requests.get(
          "https://api.hypixel.net/skyblock/auctions",
          headers={"Api-Key": API_KEY},
          params={"page": i},
        ).json()["auctions"]


class NPCBazaarFlip:
  def __init__(self, friendly_name, id, npc_cost, npc_name):
    self.friendly_name = friendly_name
    self.id = id
    self.npc_cost = npc_cost
    self.npc_name = npc_name

  def checkFlip(self, user):
    bank = user.bank
    bazaar = user.bazaar
    if bank >= self.npc_cost:
      amount_available = min(int(bank / self.npc_cost), 640)
      cost = round(self.npc_cost * amount_available)
      money = round(bazaar[self.id]["quick_status"]["sellPrice"] * amount_available)
      return {
        "item": self.friendly_name,
        "profit": "{:,}".format(money - cost),
        "buying": {
          "source": NPC,
          "cost": "{:,}".format(cost),
          "details": f"{amount_available}x {self.friendly_name} from {self.npc_name}",
        },
        "selling": {
          "source": BAZAAR,
          "cost": "{:,}".format(money),
          "details": f"{amount_available}x {self.friendly_name}",
        },
      }
    else:
      print(self.friendly_name, "is unaffordable")


class BazaarNPCFlip:
  def __init__(self, friendly_name, npc_sell, id=None):
    self.friendly_name = friendly_name
    if id is None:
      if friendly_name in ITEMS:
        id = ITEMS[friendly_name]
      else:
        id = friendly_name.upper().replace(" ", "_")
    else:
      if friendly_name in ITEMS and id == ITEMS[friendly_name]:
        print("Remove", friendly_name)
    self.id = id
    self.npc_sell = npc_sell

  def checkFlip(self, user):
    bank = user.bank
    bazaar = user.bazaar
    availableVolume = bazaar[self.id]["quick_status"]["buyVolume"]
    wantedVolume = bazaar[self.id]["quick_status"]["sellVolume"]
    totalVolume = availableVolume + wantedVolume
    if not bazaar[self.id]["sell_summary"]:
      print("Nobody is selling", self.friendly_name)
      return
    bazaar_cost = (
      bazaar[self.id]["quick_status"]["buyPrice"] * wantedVolume / totalVolume
      + bazaar[self.id]["sell_summary"][0]["pricePerUnit"] * availableVolume / totalVolume
    )
    if bank >= bazaar_cost:
      if bazaar_cost == 0:
        print(self.id, bazaar[self.id]["quick_status"]["buyPrice"], totalVolume)
      amount_available = min(int(bank / bazaar_cost), 2240)
      cost = round(bazaar_cost * amount_available)
      money = round(self.npc_sell * amount_available)
      return {
        "item": self.friendly_name,
        "profit": "{:,}".format(money - cost),
        "buying": {
          "source": BAZAAR,
          "cost": "{:,}".format(cost),
          "details": f"{amount_available}x {self.friendly_name}"
          + f" for {round(bazaar_cost, 1)} each",
        },
        "selling": {
          "source": NPC,
          "cost": "{:,}".format(money),
          "details": f"{amount_available}x {self.friendly_name}"
          + f" for {round(self.npc_sell, 1)} each",
        },
      }
    else:
      print(self.friendly_name, "is unaffordable")


#      print(
#        bazaar_cost,
#        self.id,
#        bazaar[self.id]["quick_status"]["buyPrice"],
#        (
#          bazaar[self.id]["sell_summary"]
#          or [
#            bazaar[self.id]["quick_status"]["buyPrice"],
#          ]
#        )[0]["pricePerUnit"],
#      )
#      print(wantedVolume / totalVolume, availableVolume / totalVolume)


class NPCCraftBazaarFlip:
  def __init__(
    self,
    friendly_name,
    crafted_friendly_name,
    craft_req,
    craft_cost,
    id,
    npc_cost,
    npc_name,
  ):
    self.friendly_name = friendly_name
    self.crafted_friendly_name = crafted_friendly_name
    self.craft_req = craft_req
    self.id = id
    self.npc_cost = npc_cost
    self.craft_cost = craft_cost
    self.npc_name = npc_name

  def checkFlip(self, user):
    bank = user.bank
    bazaar = user.bazaar
    collections = user.user_data["unlocked_coll_tiers"]
    if bank >= self.npc_cost and self.craft_req in collections:
      amount_available = min(
        int(bank / self.npc_cost / self.craft_cost), int(640 / self.craft_cost)
      )
      cost = round(self.npc_cost * amount_available * self.craft_cost)
      money = round(bazaar[self.id]["quick_status"]["sellPrice"] * amount_available)
      return {
        "item": self.crafted_friendly_name,
        "profit": "{:,}".format(money - cost),
        "buying": {
          "source": NPC,
          "cost": "{:,}".format(cost),
          "details": f"{amount_available * self.craft_cost}x {self.friendly_name} from {self.npc_name}",
        },
        "selling": {
          "source": BAZAAR,
          "cost": "{:,}".format(money),
          "details": f"{amount_available}x {self.crafted_friendly_name}",
        },
      }
    elif bank >= self.npc_cost:
      print("Cannot craft", self.crafted_friendly_name)
    else:
      print(self.friendly_name, "is unaffordable")


class BazaarCraftBazaarFlip:
  def __init__(
    self,
    source_name,
    craft_cost,
    craft_requirement,
    crafted_name,
    source_id=None,
    crafted_id=None,
    source_name_2=None,
    source_id_2=None,
    craft_cost_2=0,
    source_name_3=None,
    source_id_3=None,
    craft_cost_3=0,
  ):
    self.source_name = source_name
    self.source_name_2 = source_name_2
    self.source_name_3 = source_name_3
    self.crafted_name = crafted_name

    if source_id is None:
      if source_name in ITEMS:
        source_id = ITEMS[source_name]
      else:
        source_id = source_name.upper().replace(" ", "_")

    if source_id_2 is None and source_name_2 is not None:
      if source_name_2 in ITEMS:
        source_id_2 = ITEMS[source_name_2]
      else:
        source_id_2 = source_name_2.upper().replace(" ", "_")

    if source_id_3 is None and source_name_3 is not None:
      if source_name_3 in ITEMS:
        source_id_3 = ITEMS[source_name_3]
      else:
        source_id_3 = source_name_3.upper().replace(" ", "_")

    if crafted_id is None:
      if crafted_name in ITEMS:
        crafted_id = ITEMS[crafted_name]
      else:
        crafted_id = crafted_name.upper().replace(" ", "_")

    self.source_id = source_id
    self.source_id_2 = source_id_2
    self.source_id_3 = source_id_3
    self.crafted_id = crafted_id
    self.craft_cost = craft_cost
    self.craft_cost_2 = craft_cost_2
    self.craft_cost_3 = craft_cost_3
    self.craft_requirement = craft_requirement

  def checkFlip(self, user):
    bank = user.bank
    bazaar = user.bazaar
    collections = user.user_data["unlocked_coll_tiers"]
    # Calculate buy cost
    availableVolume = bazaar[self.source_id]["quick_status"]["buyVolume"]
    wantedVolume = bazaar[self.source_id]["quick_status"]["sellVolume"]
    totalVolume = availableVolume + wantedVolume
    bazaar_source_cost = (
      bazaar[self.source_id]["quick_status"]["buyPrice"] * wantedVolume / totalVolume
      + (
        bazaar[self.source_id]["sell_summary"]
        or [
          bazaar[self.source_id]["quick_status"]["buyPrice"],
        ]
      )[0]["pricePerUnit"]
      * availableVolume
      / totalVolume
    )
    if self.source_id_2 is not None:
      availableVolume = bazaar[self.source_id_2]["quick_status"]["buyVolume"]
      wantedVolume = bazaar[self.source_id_2]["quick_status"]["sellVolume"]
      totalVolume = availableVolume + wantedVolume
      bazaar_source_cost_2 = (
        bazaar[self.source_id_2]["quick_status"]["buyPrice"] * wantedVolume / totalVolume
        + (
          bazaar[self.source_id_2]["sell_summary"]
          or [
            bazaar[self.source_id_2]["quick_status"]["buyPrice"],
          ]
        )[0]["pricePerUnit"]
        * availableVolume
        / totalVolume
      )
    else:
      bazaar_source_cost_2 = 0
    if self.source_id_3 is not None:
      availableVolume = bazaar[self.source_id_3]["quick_status"]["buyVolume"]
      wantedVolume = bazaar[self.source_id_3]["quick_status"]["sellVolume"]
      totalVolume = availableVolume + wantedVolume
      bazaar_source_cost_3 = (
        bazaar[self.source_id_3]["quick_status"]["buyPrice"] * wantedVolume / totalVolume
        + (
          bazaar[self.source_id_3]["sell_summary"]
          or [
            bazaar[self.source_id_3]["quick_status"]["buyPrice"],
          ]
        )[0]["pricePerUnit"]
        * availableVolume
        / totalVolume
      )
    else:
      bazaar_source_cost_3 = 0
    # Calculate sell cost
    availableVolume = bazaar[self.crafted_id]["quick_status"]["buyVolume"]
    wantedVolume = bazaar[self.crafted_id]["quick_status"]["sellVolume"]
    totalVolume = availableVolume + wantedVolume
    bazaar_crafted_cost = (
      bazaar[self.crafted_id]["quick_status"]["buyPrice"] * availableVolume / totalVolume
      + (
        bazaar[self.crafted_id]["sell_summary"]
        or [
          bazaar[self.crafted_id]["quick_status"]["buyPrice"],
        ]
      )[0]["pricePerUnit"]
      * wantedVolume
      / totalVolume
    )
    # Actually calculate
    if bank >= bazaar_source_cost and self.craft_requirement in collections:
      # if bank >= bazaar_source_cost:
      amount_available = min(
        int(
          bank
          / (
            bazaar_source_cost * self.craft_cost
            + bazaar_source_cost_2 * self.craft_cost_2
            + bazaar_source_cost_3 * self.craft_cost_3
          )
        ),
        int(
          21760 / (self.craft_cost + self.craft_cost_2 + self.craft_cost_3)
        ),  # Equivalent of 10 almost-full inventories
      )
      cost = round(bazaar_source_cost * amount_available * self.craft_cost)
      money = round(bazaar_crafted_cost * amount_available)
      return {
        "item": self.crafted_name,
        "profit": "{:,}".format(money - cost),
        "buying": {
          "source": BAZAAR,
          "cost": "{:,}".format(cost),
          "details": (
            f"{amount_available * self.craft_cost}x {self.source_name}"
            + f" for {round(bazaar_source_cost, 1)} each"
          )
          + (
            ""
            if self.source_id_2 is None
            else f"<br>{amount_available * self.craft_cost_2}x {self.source_name_2}"
            + f" for {round(bazaar_source_cost_2, 1)} each"
          )
          + (
            ""
            if self.source_id_3 is None
            else f"<br>{amount_available * self.craft_cost_3}x {self.source_name_3}"
            + f" for {round(bazaar_source_cost_3, 1)} each"
          ),
        },
        "selling": {
          "source": BAZAAR,
          "cost": "{:,}".format(money),
          "details": f"{amount_available}x {self.crafted_name}"
          + f" for {'{:,}'.format(round(bazaar_crafted_cost, 1))} each",
        },
      }
    elif bank >= bazaar_source_cost:
      print("Cannot craft", self.crafted_name)
    else:
      print(self.source_name, "is unaffordable")

class BINBINFlip:
  def __init__(self, auction_data):
    self.item_name = auction_data["item_name"]
    self.auction_id = auction_data["uuid"]
    item_id = self.item_name.lower().replace(" ", "_").replace("'", "")
    self.purchase_for = auction_data["starting_bid"]
    self.real_price = PRICES[item_id] if item_id in PRICES else None
    self.real_price_minus_tax = self.real_price
    # Correct for tax
    if self.real_price_minus_tax:
      self.real_price_minus_tax *= 0.95
      self.real_price_minus_tax -= 100
  def checkFlip(self, user):
    if self.real_price and self.purchase_for <= user.bank:
      return {
        "item": self.item_name,
        "profit": "{:,}".format(round(self.real_price_minus_tax - self.purchase_for)),
        "buying": {
          "source": BIN,
          "cost": "{:,}".format(self.purchase_for),
          "details": f"Type <span class='auction-id' onclick='document.execCommand(\"copy\")'>/viewauction {self.auction_id}</span>",
        },
        "selling": {
          "source": BIN,
          "cost": "{:,}".format(self.real_price_minus_tax),
          "details": f"Sell the item as a BIN with a starting bid of {'{:,}'.format(round(self.real_price))} for 12 hours",
        },
      }

def construct_bin_flips(user):
  bin_flips = []
  for auction in user.ah:
    if "bin" in auction:
      bin_flips.append(BINBINFlip(auction))
  return bin_flips
