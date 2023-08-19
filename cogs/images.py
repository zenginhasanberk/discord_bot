from discord.ext import commands
import aiohttp
import discord
import praw
import random
from settings import REDDIT_APP_ID, REDDIT_APP_SECRET, REDDIT_ENABLED_MEME_SUBREDDITS, REDDIT_ENABLED_NSFW_SUBREDDITS


class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = None
        if REDDIT_APP_ID and REDDIT_APP_SECRET:
            self.reddit = praw.Reddit(client_id=REDDIT_APP_ID, client_secret=REDDIT_APP_SECRET, user_agent="Zephyrus_Discord_Bot:{id}:1.0".format(id=REDDIT_APP_ID))

    @commands.command()
    async def random(self, ctx, subreddit: str=""):
        async with ctx.channel.typing():
            if self.reddit:
                nsfw_flag = False
                chosen_subreddit = REDDIT_ENABLED_MEME_SUBREDDITS[0]
                if subreddit:
                    if subreddit in REDDIT_ENABLED_MEME_SUBREDDITS:
                        chosen_subreddit = subreddit
                    elif subreddit in REDDIT_ENABLED_NSFW_SUBREDDITS:
                        chosen_subreddit = subreddit
                        nsfw_flag = True

                    else:
                        await ctx.send("Please choose a subreddit of the following list: \"{}\" (or) NSFW: \"{}\"  ".format(", ".join(REDDIT_ENABLED_MEME_SUBREDDITS), ", ".join(REDDIT_ENABLED_NSFW_SUBREDDITS)))
                        return

                if nsfw_flag:
                    if not ctx.channel.is_nsfw():
                        await ctx.send("This is not allowed here")
                        return
    
                submissions = self.reddit.subreddit(chosen_subreddit).hot()
                post_to_pick = random.randint(1,10)
                for i in range(0, post_to_pick):
                    submission = next(x for x in submissions if not x.stickied)
                await ctx.send(submission.url)

            else:
                await ctx.send("Currently not available")

    @commands.command()
    async def cat(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://aws.random.cat/meow") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Cat")
                    embed.set_image(url=data["file"])
                    embed.set_footer(text="https://random.cat/")

                    await ctx.send(embed=embed)

    @commands.command()
    async def dog(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://dog.ceo/api/breeds/image/random") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Dog")
                    embed.set_image(url=data["message"])
                    embed.set_footer(text="https://dog.ceo/dog-api/")

                    await ctx.send(embed=embed)                

def setup(bot):
    bot.add_cog(Images(bot))