import os, requests, math

API_KEY = os.environ["API_KEY"]


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
    self.profiles = profiles.json()["profiles"][0]
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
