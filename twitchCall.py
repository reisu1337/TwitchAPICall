import os
import requests

URL = "https://id.twitch.tv/oauth2/token"
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
GRANT_TYPE = "client_credentials"
PARAMS = {
  "client_id": CLIENT_ID,
  "client_secret": CLIENT_SECRET,
  "grant_type": GRANT_TYPE
}

r1 = requests.post(url = URL, params = PARAMS)

token = r1.json()["access_token"]
print(token)

URL2 = "https://api.twitch.tv/helix/search/channels?query=reisu1337"
PARAMS2 = {
  "client-id": CLIENT_ID,
  "Authorization": f"Bearer {token}"
}

r2 = requests.post(url = URL2, params = PARAMS2)

data = r2.json()

print(data)
