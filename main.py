import os
from discord.ext import commands
from dotenv import load_dotenv
from settings import *

load_dotenv()

bot = commands.Bot(command_prefix="!")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f"cogs.{filename[:-3]}")


bot.run(os.getenv("DISCORD_BOT_TOKEN"))
