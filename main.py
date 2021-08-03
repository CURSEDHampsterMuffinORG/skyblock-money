from flask import Flask, Response
import os

app = Flask(__name__, template_folder=".")


@app.route("/")
def send_index():
  return open("index.html", "rb").read().decode()


@app.route("/index.js")
def send_index_code():
  return Response(
    open("index.js", "rb").read().decode(), mimetype="application/javascript"
  )


@app.route("/index.png")
def send_index_bg():
  return open("index.png", "rb").read()


@app.route("/favicon.png")
def send_icon():
  return open("favicon.png", "rb").read()


app.run(host="0.0.0.0")
