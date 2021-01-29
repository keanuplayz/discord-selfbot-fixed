import datetime
import discord
from discord.ext import commands
import praw
from cogs.utils.config import get_config_value

'''Module for Reddit commands.'''

r = praw.Reddit(client_id=str(get_config_value("reddit", "clientid")), client_secret=str(get_config_value(
    "reddit", "clientsecret")), user_agent=str(get_config_value("reddit", "useragent")))


class Reddit(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def reddit(self, ctx, sub):
        submission = r.subreddit(sub).random()
        redditembed = discord.Embed()

        posttime = submission.created_utc
        realtime = datetime.datetime.utcfromtimestamp(
            posttime).strftime("%Y-%m-%d %H:%M:%S")
        redditembed.title = submission.title
        redditembed.color = 0x7ac5c9
        redditembed.set_footer(
            text="r/" + submission.subreddit.display_name + " | " + realtime)
        redditembed.title = submission.title
        redditembed.url = submission.url
        redditembed.set_image(url=submission.url)

        await ctx.message.delete()
        await ctx.send(embed=redditembed)


def setup(bot):
    bot.add_cog(Reddit(bot))
