import os
import requests
from dotenv import load_dotenv
from flask import Flask, request, redirect

# Load credentials from .env
load_dotenv()
CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
USER_AGENT = os.getenv('REDDIT_USER_AGENT')
REDIRECT_URI = os.getenv('REDDIT_REDIRECT_URI')  # e.g. http://localhost:3000/callback

STATE = "random_state_123"
app = Flask(__name__)

@app.route('/')
def home():
    return redirect('/login')

def generate_auth_url():
    base_url = "https://www.reddit.com/api/v1/authorize"
    params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "state": STATE,
        "redirect_uri": REDIRECT_URI,
        "duration": "permanent",
        "scope": "identity read submit"
    }
    param_str = '&'.join([f"{k}={requests.utils.quote(v)}" for k, v in params.items()])
    return f"{base_url}?{param_str}"

@app.route('/login')
def login():
    return redirect(generate_auth_url())

@app.route('/callback')
def callback():
    code = request.args.get('code')
    state = request.args.get('state')

    if not code or state != STATE:
        return "Invalid code or state", 400

    token_url = "https://www.reddit.com/api/v1/access_token"
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI
    }
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    headers = {'User-Agent': USER_AGENT}

    r = requests.post(token_url, data=data, auth=auth, headers=headers)

    if r.ok:
        token_data = r.json()
        access_token = token_data['access_token']
        refresh_token = token_data['refresh_token']

        with open('tokens.txt', 'w') as f:
            f.write(f"Access Token: {access_token}\n")
            f.write(f"Refresh Token: {refresh_token}\n")

        return "✅ Tokens saved to tokens.txt. You can close this window."
    else:
        return f"❌ Failed to get tokens: {r.text}", 400

if __name__ == '__main__':
    app.run(port=3000)
