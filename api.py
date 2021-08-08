import os, requests, math, json

API_KEY = os.environ["API_KEY"]
ITEMS = json.load(open("skyblock_items.json"))
ITEMS = {friendly["name"]: id for id, friendly in ITEMS.items()}


class User:
  def __init__(self, username):
    uuid = requests.get(
      f"https://api.mojang.com/users/profiles/minecraft/{username}"
    ).json()["id"]
    profiles = requests.get(
      "https://api.hypixel.net/skyblock/profiles",
      params={"uuid": uuid},
      headers={"Api-Key": API_KEY},
    )
    self.uuid = uuid
    self.profiles = max(
      profiles.json()["profiles"], key=lambda prof: prof["members"][uuid]["last_save"]
    )
    self.bank = (
      self.profiles["banking"]["balance"]
      + self.profiles["members"][self.uuid]["coin_purse"]
    )
    self.bazaar = requests.get(
      "https://api.hypixel.net/skyblock/bazaar",
      headers={"Api-Key": API_KEY},
    ).json()["products"]

  def get_flips(self):
    ...


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
      amount_available = min(math.floor(bank / self.npc_cost), 640)
      cost = round(self.npc_cost * amount_available)
      money = round(bazaar[self.id]["quick_status"]["sellPrice"] * amount_available)
      return {
        "item": self.friendly_name,
        "profit": "{:,}".format(money - cost),
        "buying": {
          "source": "NPC",
          "cost": "{:,}".format(cost),
          "details": f"{amount_available}x {self.friendly_name} from {self.npc_name}",
        },
        "selling": {
          "source": "Bazaar",
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
    bazaar_cost = (
      bazaar[self.id]["quick_status"]["buyPrice"] * wantedVolume / totalVolume
      + (
        bazaar[self.id]["sell_summary"]
        or [
          bazaar[self.id]["quick_status"]["buyPrice"],
        ]
      )[0]["pricePerUnit"]
      * availableVolume
      / totalVolume
    )
    if bank >= bazaar_cost:
      amount_available = min(math.floor(bank / bazaar_cost), 2240)
      cost = round(bazaar_cost * amount_available)
      money = round(self.npc_sell * amount_available)
      return {
        "item": self.friendly_name,
        "profit": "{:,}".format(money - cost),
        "buying": {
          "source": "Bazaar",
          "cost": "{:,}".format(cost),
          "details": f"{amount_available}x {self.friendly_name}"
          + f" for {round(bazaar_cost, 1)} each",
        },
        "selling": {
          "source": "NPC",
          "cost": "{:,}".format(money),
          "details": f"{amount_available}x {self.friendly_name}"
          + f" for {round(self.npc_sell, 1)} each",
        },
      }
    else:
      print(self.friendly_name, "is unaffordable")
