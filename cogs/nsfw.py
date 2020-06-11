import os
import random
import requests
import json
import discord
from discord.ext import commands

'''Module for NSFW commands.'''


class NSFW(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def atinm(self, ctx, folder="default"):
        if folder == "yes":
            image = random.choice([x for x in os.listdir("./media/yes") if os.path.isfile(os.path.join("media", "yes", x))])
            print(image)
            imagepath = os.path.abspath(os.path.join("media", "yes", image))
            await ctx.send(file=discord.File(imagepath, filename=image))
        elif folder == "damn":
            image = random.choice([x for x in os.listdir("./media/yes/damn") if os.path.isfile(os.path.join("./media/yes/damn", x))])
            print(image)
            imagepath = os.path.abspath(os.path.join("media", "yes", "damn", image))
            await ctx.send(file=discord.File(imagepath, filename=image))
        elif folder == "default":
            image = random.choice([x for x in os.listdir("./media") if os.path.isfile(os.path.join("./media", x))])
            print(image)
            imagepath = os.path.abspath(os.path.join("media", image))
            await ctx.send(file=discord.File(imagepath, filename=image))

    @commands.command(pass_context=True)
    async def r34(self, ctx, term):
        base_url = "https://r34-json-api.herokuapp.com/posts?limit=1"
        complete_url = base_url + "&tags=" + str(term)
        try:
            response = requests.get(complete_url)
        except BaseException:
            await ctx.send("Error")
        res = response.json()

        r34embed = discord.Embed(title="Result for " + term)
        r34embed.add_field(name=res.height,value=res.height)
        await ctx.send(embed=r34embed)


def setup(bot):
    bot.add_cog(NSFW(bot))
