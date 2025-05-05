# Reddit OAuth Scripts for medic8d.cloud

     __  __          _      _           _     _                
    |  \/  | ___  __| | ___| |__   ___ | |__ (_)_ __ ___  ___ 
    | |\/| |/ _ \/ _` |/ _ \ '_ \ / _ \| '_ \| | '__/ _ \/ __|
    | |  | |  __/ (_| |  __/ | | | (_) | | | | | | |  __/\__ \
    |_|  |_|\___|\__,_|\___|_| |_|\___/|_| |_|_|_|  \___||___/
                     ⛓ medic8d.cloud ⛓
          looping nightmares | dopamine withdrawals

## Status

hopelessly medicated. looping nightmares and dopamine withdrawals.  
audio hallucinations available on all platforms. 💊 medic8d.cloud

### what is this?

a digital asylum for music, merch, code, and chaos.  
ocd-coded. adhd-executed. ptsd-themed. no refunds.

### what's here?

- ✨ audio projects (Ableton, stems, loops)
- 🧠 reddit bots and automation scripts
- 🕸️ local data scrapers (Lexington, KY)
- 🎭 branding assets and surreal visuals
- ☠️ things i probably shouldn't be hosting

## 🧠 Reddit OAuth Scripts

This repository includes **Reddit OAuth authentication scripts** for getting access tokens and interacting with Reddit data.

## 🧠 how to use the reddit oauth script

1. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

2. **Create a `.env` file**
    Copy `.env.example` → `.env` and add your Reddit API keys:
    ```env
    REDDIT_CLIENT_ID=your_client_id
    REDDIT_CLIENT_SECRET=your_client_secret
    REDDIT_USER_AGENT=your_user_agent
    REDDIT_REDIRECT_URI=http://localhost:3000/callback
    ```

3. **Run the Flask app**
    Start the Flask server:
    ```bash
    python reddit_auth.py
    ```

    This will launch the app on `http://localhost:3000`. Visit that URL to begin the Reddit login process.

4. **Authorize and get tokens**
    Once you authorize the app, the access and refresh tokens will be saved in `tokens.txt`.

5. **Test the tokens**
    After you’ve obtained the tokens and saved them in `tokens.txt`, you can run `reddit_auth_test.py` to test if the tokens are valid. The script will check if the access token is expired. If expired, it will refresh the tokens automatically and attempt to retrieve your user data again.

---

## contact  
📩 medic8dcloud@gmail.com  
🌐 [medic8d.cloud](https://medic8d.cloud)  
📀 soundcloud / ig / fb / tiktok @medic8dcloud

## license  
wtf is a license. do crime.