import os
import requests
from dotenv import load_dotenv

load_dotenv()

REDDIT_API_URL = "https://oauth.reddit.com/api/v1/me"
TOKEN_FILE = "tokens.txt"

CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
USER_AGENT = os.getenv("REDDIT_USER_AGENT")

def load_tokens():
    try:
        with open(TOKEN_FILE, 'r') as f:
            lines = f.readlines()
            access_token = lines[0].strip().split(": ")[1]
            refresh_token = lines[1].strip().split(": ")[1]
            return access_token, refresh_token
    except Exception as e:
        print(f"Token load error: {e}")
        return None, None

def save_tokens(access_token, refresh_token):
    with open(TOKEN_FILE, 'w') as f:
        f.write(f"Access Token: {access_token}\n")
        f.write(f"Refresh Token: {refresh_token}\n")

def get_user_data(access_token, refresh_token):
    headers = {
        'Authorization': f'bearer {access_token}',
        'User-Agent': USER_AGENT
    }
    r = requests.get(REDDIT_API_URL, headers=headers)

    if r.status_code == 200:
        print("✅ User Data:")
        print(r.json())
    elif r.status_code == 401:
        print("⚠️ Access token expired. Refreshing...")
        refresh_access_token(refresh_token)
    else:
        print(f"❌ API call failed: {r.status_code} – {r.text}")

def refresh_access_token(refresh_token):
    token_url = "https://www.reddit.com/api/v1/access_token"
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token
    }
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    headers = {'User-Agent': USER_AGENT}

    r = requests.post(token_url, data=data, headers=headers, auth=auth)

    if r.ok:
        token_data = r.json()
        new_access_token = token_data['access_token']
        new_refresh_token = token_data.get('refresh_token', refresh_token)
        save_tokens(new_access_token, new_refresh_token)
        print("🔁 Tokens refreshed.")
        get_user_data(new_access_token, new_refresh_token)
    else:
        print(f"❌ Refresh failed: {r.status_code} – {r.text}")

if __name__ == "__main__":
    access_token, refresh_token = load_tokens()
    if access_token and refresh_token:
        get_user_data(access_token, refresh_token)
    else:
        print("❌ No tokens found. Run the login flow first.")
