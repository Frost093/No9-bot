import discord
import os

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents, case_insensitive=True)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

    #later
    #await bot.load_extension("cogs.general")
    #await bot.load_extension("cogs.admin")
    #await bot.load_extension("cogs.dev")
    #print("Cogs loaded successfully.")
bot.run(TOKEN)
