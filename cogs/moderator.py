from discord.ext import commands
import discord

from utils import mods_or_owner

class Moderator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @mods_or_owner()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member=None, reason: str="Because"):
        if member is not None:
            await ctx.guild.kick(member, reason=reason)
            await ctx.send(f"User was kicked because: {reason}")
        else:
            await ctx.send("Please specify the user to kick via mention.")

    
    @commands.command()
    @mods_or_owner()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member=None, reason: str="Because"):
        if member is not None:
            await ctx.guild.ban(member, reason=reason)
            await ctx.send(f"User was banned because: {reason}")
        else:
            await ctx.send("Please specify the user to ban via mention.")

    @commands.command()
    @mods_or_owner()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member: str = "", reason: str="Because"):
        if member == "":
            await ctx.send("Please specify username as text.")
            return
        
        bans = await ctx.guild.bans()
        for ban in bans:
            if ban.user.name == member:
                await ctx.guild.unban(ban.user, reason=reason)
                await ctx.send(f"User was unbanned because: {reason}.")
                return
        await ctx.send("User was not found in the ban list.")

def setup(bot):
    bot.add_cog(Moderator(bot))