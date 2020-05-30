from discord.ext import commands
from pypresence import Presence
import time

client_id = "716223577220972584"
RPC = Presence(client_id)
RPC.connect()

class RPC(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def setrpc(self, ctx, *, msg):
        await RPC.update(state=msg)
        await ctx.send(f"Updated presence to `{msg}`")
        while True:
            time.sleep(15)

def setup(bot):
    bot.add_cog(RPC(bot))
