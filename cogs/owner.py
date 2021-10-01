import discord
from discord.ext import commands

from libs import httpsession

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="closehttp", aliases=["closesession"])
    @commands.is_owner()
    async def close_http_session(self, ctx):
        await httpsession.close_session()
        await ctx.send("> Closed HTTP session.")

def setup(bot):
	bot.add_cog(Owner(bot))