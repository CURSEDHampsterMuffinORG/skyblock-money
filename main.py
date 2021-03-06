from flask import Flask, Response, request
import os, json
import api, flips, discord


app = Flask(__name__, template_folder=".")
app.config["SECRET_KEY"] = discord.OAUTH2_CLIENT_SECRET
if "http://" in discord.OAUTH2_REDIRECT_URI:
  os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "true"


@app.route("/")
def send_index():
  return open("index.html", "rb").read().decode()


@app.route("/index.js")
def send_index_code():
  discord_url = discord.make_auth_url()
  return Response(
    open("index.js", "rb").read().decode().replace("[discord url here]", discord_url),
    mimetype="application/javascript",
  )


app.add_url_rule("/callback", "callback", discord.handle_callback)


@app.route("/flips-for/<username>/<auctions>")
def get_flips(username, auctions):
  # Init
  user = api.User(username, auctions)
  calculated_flips = []
  # Check code
  userid = ""
  if "token" in request.cookies:
    userid = discord.check_code(request.cookies["token"])
  verified_discord = userid in [
    # Close admins/frens
    "794377681331945524", # KTibow
    "811220121620054016", # Coder_Ultimate
    "708004210368839692", # BlueTacoMan
    "783464370520195072", # Gunsling3r
    "693834425766641735", # SwiftEagle
    "715566599872053280", # IdiotDev
    # Beta testers
    "715811392090800201", # Coconut BS
    "358342926851637249", # TheMVAmad
    "493886910146543616", # Young Joben (OG)
    "373539975687307266", # Drew
    "650756055390879757", # Mankifg
    "726685339082817608", # The1And0nlyKevin
    "873369373002309723", # BluerockHomeland
    "216353124221190144", # JuSStin
    "297601921286406156", # Decodaz
    "396315822500478976", # Lakia
    "698189280090259476", # CuteWarriorLover
    "791114486270263317", # gamersheep
    "875107433540894820", # yoooosuop
    "590428408090198016", # Foxxy
    "508935139171106816", # CrazyNinjaCan15
    "535805599414484992", # Alkif
    "706886804028260363", # casual_gamer_256
    "712257445912903721", # TheMultiTasker
    "160664736332120065", # Cubic
    "225944599452057600", # Raymond
    "687888328611332118", # Duck
  ]
  if not verified_discord:
    print(username, "is not approved")
    if userid != "":
      print(userid)
    calculated_flips.append(
      {
        "item": "This user is not approved yet.",
        "profit": "100,000",
        "buying": {
          "source": "Discord",
          "cost": "0.0",
          "details": "Join the <a href='https://discord.gg/Pzd2GEREEz'>Discord</a>,"
          + " and get your account approved, either for free or by donating.",
        },
        "selling": {
          "source": "Bazaar Money",
          "cost": "100,000",
          "details": "Unlock OP flips with more than 100k profit.",
        },
      }
    )
  available_flips = flips.flips.copy()
  if auctions == "true":
    available_flips += api.construct_bin_flips(user)
  for flip in available_flips:
    flip_data = flip.checkFlip(user)
    profit_amount = int(flip_data["profit"].replace(",", "")) if flip_data else None
    if flip_data is not None and profit_amount > 0 and (profit_amount < 100000 or verified_discord):
      calculated_flips.append(flip_data)
    elif flip_data is not None and (profit_amount < 100000 or verified_discord):
      # print(
      # flip_data["item"],
      # f"is not profitable",
      # f"({flip_data['buying']['cost']} to {flip_data['selling']['cost']})",
      # )
      ...
    elif flip_data is not None:
      print("Skipping over flip because user is not verified")
  data = json.dumps(
    sorted(
      calculated_flips,
      key=lambda flip_data: int(flip_data["profit"].replace(",", "")),
      reverse=True,
    )
  )
  return Response(data, mimetype="application/json")


@app.route("/index.png")
def send_index_bg():
  return open("index.png", "rb").read()


@app.route("/index-dark.png")
def send_index_bg_dark():
  return open("index-dark.png", "rb").read()


@app.route("/favicon.png")
def send_icon():
  return open("favicon.png", "rb").read()


@app.route("/bazaar.png")
def send_bazaar_icon():
  return open("bazaar.png", "rb").read()


@app.route("/adventurer.png")
def send_adventurer_icon():
  return open("adventurer.png", "rb").read()


@app.route("/auction.png")
def send_auction_icon():
  return open("auction.png", "rb").read()


app.run(host="0.0.0.0")
