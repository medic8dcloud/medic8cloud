
    __  __          _      _           _     _                
   |  \/  | ___  __| | ___| |__   ___ | |__ (_)_ __ ___  ___  
   | |\/| |/ _ \/ _` |/ _ \ '_ \ / _ \| '_ \| | '__/ _ \/ __| 
   | |  | |  __/ (_| |  __/ | | | (_) | | | | | | |  __/\__ \ 
   |_|  |_|\___|\__,_|\___|_| |_|\___/|_| |_|_|_|  \___||___/ 
                   ⛓ medic8d.cloud ⛓
         looping nightmares | dopamine withdrawals


## medic8dcloud Scripts

This directory contains all bot and automation scripts for the **medic8d.cloud** project.

---

### 📁 discord/

Scripts for managing the Discord server (channel setup, bot commands, etc.)

- `create_channel.py`: Auto-creates text and voice channels under a defined category.
- `social_bot.py`: Listens for chat commands (e.g. `!socials`) and posts brand links.
- `requirements.txt`: Dependencies for all Discord-related functionality.
- `README.md`: This file. Explains layout and usage.

**To run:**
```bash
cd scripts/discord
pip install -r requirements.txt
python social_bot.py  # or create_channel.py once for setup
```

---

### 📁 reddit/

Reddit OAuth + automation tools.

- `reddit_auth.py`: Handles access token retrieval.
- `reddit_auth_test.py`: Verifies Reddit OAuth is working.
- `requirements.txt`: For Reddit automation tools.

---

### 📁 spotify/

Spotify Web API access for pulling saved tracks.

- `spotify_pull.py`: Example script to pull and dump saved tracks.
- `requirements.txt`: Spotipy + dotenv.

---

### 📦 Environment Setup

Each subfolder has its own `.env.example` file. Copy it to `.env` and fill in credentials.

```bash
cp .env.example .env
# then edit with your values
```

---

looping nightmares. dopamine withdrawals. medic8d.cloud
