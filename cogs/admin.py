import discord
from discord.ext import commands
import datetime 
from settings import MODERATOR_ROLE_NAME

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, cog: str):
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send("Could not unload Cog (format: !unload cogs.<cogname>")
            return
        await ctx.send("Cog unloaded")

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, cog: str):
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send("Could not load Cog (format: !load cogs.<cogname>")
            return
        await ctx.send("Cog loaded")

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, cog: str):
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send("Could not reload Cog (format: !reload cogs.<cogname>")
            return
        await ctx.send("Cog reloaded")
    

    @commands.command()
    @commands.is_owner()
    async def status(self, ctx):
        guild = ctx.guild

        num_voice_channels = len(guild.voice_channels)
        num_text_channels = len(guild.text_channels)

        embed = discord.Embed(description="Server Status", colour=discord.Colour.dark_gold())

        embed.add_field(name="Server Name", value=guild.name, inline=False)
        embed.add_field(name="# Voice Channels", value=num_voice_channels)
        embed.add_field(name="# Text Channels", value=num_text_channels)

        embed.set_thumbnail(url="https://miro.medium.com/max/1000/0*3DmIAAh5gJ2Q-pvU.jpg")
        embed.set_image(url="https://akm-img-a-in.tosshub.com/sites/btmt/images/stories/pubg_game_660_141020121948.jpg")
        embed.set_author(name=self.bot.user.name)
        embed.set_footer(text=datetime.datetime.now())

        emoji_string = ""
        for e in guild.emojis:
            if e.is_usable():
                emoji_string += str(e)

        embed.add_field(name="Custom emojis", value=emoji_string or "No emojis available", inline=False)

        embed.add_field(name="AFK Channel", value=guild.afk_channel)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Admin(bot))  