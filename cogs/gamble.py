import random
from discord.ext import commands

class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Rolls a random number between 1 and 100")
    async def roll(self, ctx):
        n = random.randint(1,101)
        await ctx.send(n)

    @commands.command(brief="Rolls a random number between 1 and 6")
    async def dice(self, ctx):
        n = random.randint(1,7)
        await ctx.send(n)

    @commands.command(brief="Toss a coin")
    async def coinflip(self, ctx):
        n = random.randint(0,1)
        await ctx.send("Heads" if n == 0 else "Tails")

def setup(bot):
    bot.add_cog(Gamble(bot))