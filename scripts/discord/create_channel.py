# create_server_layout.py — medic8dcloud server autoconfig
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"🔧 Logged in as {bot.user}")
    for guild in bot.guilds:
        await setup_server(guild)
    rotate_status.start()

@tasks.loop(minutes=5)
async def rotate_status():
    statuses = [
        "looping nightmares",
        "waiting for dopamine",
        "404: attention not found",
        "glitched in .cloud",
        "medic8dcloud || !socials"
    ]
    from random import choice
    await bot.change_presence(activity=discord.Game(name=choice(statuses)))

async def setup_server(guild):
    category = await guild.create_category("💊 medic8dcloud")

    # Roles
    visitor = await guild.create_role(name="visitor")
    looped = await guild.create_role(name="looped")
    glitchmod = await guild.create_role(name="glitchmod", permissions=discord.Permissions(manage_messages=True, kick_members=True))

    # Text channels + perms
    text_channels = [
        "start-here",
        "glitch-feed",
        "loops-and-voids",
        "hallucinate",
        "patch-notes",
        "bot-commands",
        "private-loop",
        "loop-samples",
        "bug-report",
        "psyrecords"
    ]

    private = {"private-loop", "loop-samples", "psyrecords"}
    for name in text_channels:
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=name not in private),
            looped: discord.PermissionOverwrite(read_messages=True),
            glitchmod: discord.PermissionOverwrite(read_messages=True)
        }
        chan = await guild.create_text_channel(name, category=category, overwrites=overwrites)

        if name == "start-here":
            pinned_msg = await chan.send("💊 Welcome to **medic8dcloud**. Type `!socials` to get all the links.")
            await pinned_msg.pin()

    # Voice channel
    voice_overwrites = {
        guild.default_role: discord.PermissionOverwrite(connect=False),
        looped: discord.PermissionOverwrite(connect=True),
        glitchmod: discord.PermissionOverwrite(connect=True)
    }
    await guild.create_voice_channel("🩸 the loop", category=category, overwrites=voice_overwrites)

bot.run(TOKEN)
