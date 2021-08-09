from flask import session, request, make_response
import os, json
from requests_oauthlib import OAuth2Session

OAUTH2_CLIENT_ID = os.environ["CLIENT_ID"]
OAUTH2_CLIENT_SECRET = os.environ["CLIENT_SECRET"]
OAUTH2_REDIRECT_URI = "http://localhost:5000/callback"


def token_updater(token):
  session["oauth2_token"] = token


def make_session(token=None, state=None, scope=None):
  return OAuth2Session(
    client_id=OAUTH2_CLIENT_ID,
    token=token,
    state=state,
    scope=scope,
    redirect_uri=OAUTH2_REDIRECT_URI,
    auto_refresh_kwargs={
      "client_id": OAUTH2_CLIENT_ID,
      "client_secret": OAUTH2_CLIENT_SECRET,
    },
    auto_refresh_url="https://discordapp.com/api/oauth2/token",
    token_updater=token_updater,
  )


def make_auth_url():
  discord = make_session(scope=["identify"])
  auth_url, state = discord.authorization_url(
    "https://discordapp.com/api/oauth2/authorize"
  )
  session["oauth2_state"] = state
  return auth_url


def handle_callback():
  if request.values.get("error"):
    return request.values["error"]
  discord = make_session(state=session.get("oauth2_state"))
  try:
      token = discord.fetch_token(
        "https://discordapp.com/api/oauth2/token",
        client_secret=OAUTH2_CLIENT_SECRET,
        authorization_response=request.url,
      )
  except Exception as e:
      return "<p style='font-family: sans-serif'>Error authing. Try clearing your cookies.</p>"
  resp = make_response(
    "<p style='font-family: sans-serif'>Token has been saved. <a href='/'>Get flips</a></p>"
  )
  resp.set_cookie("token", json.dumps(token))
  return resp


def check_code(token):
  discord = make_session(token=json.loads(token))
  user = discord.get("https://discordapp.com/api/users/@me").json()
  print(user)
  return user["id"]
