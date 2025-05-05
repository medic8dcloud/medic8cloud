# bot.py - medic8dcloud Discord bot
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"🤖 Logged in as {bot.user.name}")

@bot.command()
async def socials(ctx):
    links = """
**🌐 medic8dcloud socials:**
🔗 Website: https://medic8d.cloud  
▶️ YouTube: https://www.youtube.com/@medic8dcloud  
🎧 Bandcamp: https://medic8dcloud.bandcamp.com/  
📘 Facebook: https://facebook.com/medic8dcloud  
📸 Instagram: https://instagram.com/medic8dcloud  
🔊 SoundCloud: https://soundcloud.com/medic8dcloud  
📢 Reddit Sub: https://reddit.com/r/medic8dcloud  
👤 Reddit User: https://reddit.com/u/medic8d_cloud  
☕ Buy Me a Coffee: https://buymeacoffee.com/medic8dcloud  
🌲 Linktree: https://linktr.ee/medic8dcloud  
💬 Discord: https://discord.com/invite/gmzEqAFmEZ  
📡 HyperFollow: https://hyperfollow.com/medic8dcloud
"""
    await ctx.send(links)

bot.run(TOKEN)
