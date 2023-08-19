from discord.ext import commands
import discord
from utils import get_momma_jokes

class NSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def insult(self, ctx, member: discord.Member = None):
        insult = await get_momma_jokes()        
        if member is not None:
            await ctx.send("{} eat this {}".format(member.name, insult))
        else:
            await ctx.send("{} joke's on you! {}".format(ctx.message.author, insult))

def setup(bot):
    bot.add_cog(NSFW(bot))