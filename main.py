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


@app.route("/flips-for/<username>")
def get_flips(username):
  # Init
  user = api.User(username)
  calculated_flips = []
  # Check code
  userid = ""
  if "token" in request.cookies:
    userid = discord.check_code(request.cookies["token"])
  verified_discord = userid in ["794377681331945524", "811220121620054016"]
  if not verified_discord:
    print(username, "is not approved")
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
  for flip in flips.flips:
    flip_data = flip.checkFlip(user)
    profit_amount = int(flip_data["profit"].replace(",", "")) if flip_data else None
    if (
      flip_data is not None
      and profit_amount > 0
      and (profit_amount < 100000 or verified_discord)
    ):
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


@app.route("/favicon.png")
def send_icon():
  return open("favicon.png", "rb").read()


app.run(host="0.0.0.0")
