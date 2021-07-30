import os
import requests

def isLive(username):
  URL = "https://id.twitch.tv/oauth2/token"
  CLIENT_ID = os.environ['CLIENT_ID']
  CLIENT_SECRET = os.environ['CLIENT_SECRET']
  GRANT_TYPE = "client_credentials"
  PARAMS = {
      "client_id": CLIENT_ID,
      "client_secret": CLIENT_SECRET,
      "grant_type": GRANT_TYPE
  }

  r1 = requests.post(url=URL, params=PARAMS)

  token = r1.json()["access_token"]

  URL2 = "https://api.twitch.tv/helix/search/channels?query="+username
  HEADERS = {"client-id": CLIENT_ID, "Authorization": f"Bearer {token}"}

  r2 = requests.get(url=URL2, headers=HEADERS)

  data = r2.json()

  for i in range(len(data["data"])):
    if (data["data"][i]["broadcaster_login"]) == username or (data["data"][i]["display_name"]) == username:
      return (data["data"][i]["is_live"])

print(isLive("reisu1337"))