import os, requests

API_KEY = os.environ["API_KEY"]


class User:
  def __init__(self, username):
    uuid = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}").json()["id"]
    profiles = requests.get(
      "https://api.hypixel.net/skyblock/profiles",
      params={"uuid": uuid},
      headers={"Api-Key": API_KEY},
    )
    self.uuid = uuid
    self.profiles = profiles.json()["profiles"][0]

  def get_flips(self):
    ...
