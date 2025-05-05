# medic8dcloud Discord Bot

Automates setup and moderation of the **medic8dcloud** Discord server. Includes:

* `create_channel.py`: Creates custom server layout (text/voice channels, roles).
* `social_bot.py`: Responds to `!socials` with medic8dcloud links.

## Requirements

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r scripts/discord/requirements.txt
```

## Setup

1. **Create `.env` file**:

```env
DISCORD_TOKEN=your_bot_token_here
```

2. **Invite bot to server with correct permissions**:
   Use this format:

```
https://discord.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&scope=bot&permissions=8
```

Make sure you enable these:

* Manage Roles
* Manage Channels
* Send Messages
* Read Messages
* Use Slash Commands
* View Channels
* Manage Messages

## Run Scripts

### 1. Create Server Layout

```bash
python scripts/discord/create_channel.py
```

* Creates `medic8dcloud` category
* Sets up text/voice channels
* Creates roles like `looped`, `visitor`

### 2. Launch Bot for Commands

```bash
python scripts/discord/social_bot.py
```

* Responds to `!socials` in any channel with platform links

## Notes

* Run `create_channel.py` once per server setup.
* Keep `social_bot.py` running continuously for interaction.
* `.env` token must be the same bot added to the server.

---

💊 looping nightmares | dopamine withdrawals
[https://medic8d.cloud](https://medic8d.cloud)
