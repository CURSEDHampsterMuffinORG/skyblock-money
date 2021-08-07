from flask import Flask, Response
import os, json
import api, flips, codes

app = Flask(__name__, template_folder=".")


@app.route("/")
def send_index():
  date = str(codes.check_date())
  return open("index.html", "rb").read().decode().replace("[date]", date)


@app.route("/index.js")
def send_index_code():
  return Response(
    open("index.js", "rb").read().decode(), mimetype="application/javascript"
  )


@app.route("/flips-for/<username>/", defaults={"code": 0})
@app.route("/flips-for/<username>/<code>")
def get_flips(username, code):
  # Init
  user = api.User(username)
  calculated_flips = []
  # Check code
  hash = codes.check_code(float(code))
  verified_discord = hash in [
    "2e3d927e64159e7ff30d8daa9099202f",
    "665a74080cd608f4e29301a458f0a142",
    "0fcf267abdf76807354be887040668b2",
    "cb1ccc7a1a5035a978164efa9ca15432",
    "8a728c89b167d6ea972f4d8d1a0e7cd4",
    "eae906d51979a402ac99fd73aa70da24",
    "aefd9e0dca2fd7a4664dcd4940efad08",
  ]
  print(f"{username} is verified for op flips: {verified_discord}")
  if not verified_discord:
    calculated_flips.append(
      {
        "item": "Invalid code.",
        "profit": "100,000",
        "buying": {
          "source": "Discord",
          "cost": "0.0",
          "details": "Join the <a href='https://discord.gg/Pzd2GEREEz'>Discord</a> for free.",
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
      #print(
      #flip_data["item"],
      #f"is not profitable",
      #f"({flip_data['buying']['cost']} to {flip_data['selling']['cost']})",
      #)
      ...
  return json.dumps(
    sorted(
      calculated_flips,
      key=lambda flip_data: int(flip_data["profit"].replace(",", "")),
      reverse=True,
    )
  )


@app.route("/index.png")
def send_index_bg():
  return open("index.png", "rb").read()


@app.route("/favicon.png")
def send_icon():
  return open("favicon.png", "rb").read()


app.run(host="0.0.0.0")
