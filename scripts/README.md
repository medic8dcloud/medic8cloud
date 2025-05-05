# medic8dcloud - Scripts Directory
 __  __          _      _           _     _                
|  \/  | ___  __| | ___| |__   ___ | |__ (_)_ __ ___  ___ 
| |\/| |/ _ \/ _` |/ _ \ '_ \ / _ \| '_ \| | '__/ _ \/ __|
| |  | |  __/ (_| |  __/ | | | (_) | | | | | | |  __/\__ \
|_|  |_|\___|\__,_|\___|_| |_|\___/|_| |_|_|_|  \___||___/
                 ⛓ medic8d.cloud ⛓
      looping nightmares | dopamine withdrawals



      
This directory organizes all automation and bot logic into modular folders by platform.

---

## Structure

```
scripts/
├── discord/
│   ├── create_channel.py    # One-time server setup (channels, roles)
│   ├── social_bot.py        # Ongoing bot commands (e.g. !socials)
│   ├── requirements.txt     # Python deps for discord bot
│   └── README.md            # Discord-specific usage
│
├── reddit/
│   └── ...                  # Reddit automation logic
│
├── spotify/
│   └── ...                  # Spotify metadata + scraping
```

---

## Usage Notes

- Each folder is **self-contained** and should include:
  - its own `README.md` with usage
  - `requirements.txt` (if Python)
  - `.env.example` with required secrets
- All `.env` files are **gitignored**

To set up a folder:

```bash
cd scripts/discord
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # then edit with actual credentials
python create_channel.py  # or python social_bot.py
```

---

## Dev Notes

- Discord scripts use `discord.py` with command/event handlers
- GitHub repo should stay modular: don’t mix platform logic
- Use symlinks or wrappers at root level if needed

---

medic8d.cloud 💊 | looping nightmares | dopamine withdrawals
