from flask import Flask, Response
import os, json
import api, flips

app = Flask(__name__, template_folder=".")


@app.route("/")
def send_index():
  return open("index.html", "rb").read().decode()


@app.route("/index.js")
def send_index_code():
  return Response(
    open("index.js", "rb").read().decode(), mimetype="application/javascript"
  )


@app.route("/flips-for/<username>")
def get_flips(username):
  user = api.User(username)
  calculated_flips = []
  for flip in flips.flips:
    if isinstance(flip, api.NPCBazaarFlip):
      flip_data = flip.checkFlip(user)
      if flip_data is not None and int(flip_data["profit"].replace(",", "")) > 0:
        calculated_flips.append(flip_data)
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
