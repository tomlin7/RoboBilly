"""
Bot Module
"""

import discord
import asyncio
from discord.ext import commands


class Bot(commands.Cog):
    """
    Commands related to the bot.
    """
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["pong", "latency"])
    async def ping(self, ctx):
        async with ctx.channel.typing():
    	    ping = str(self.bot.latency * 1000)
    	    embed = discord.Embed(title="Pong!", description=f'Latency: {ping} ms', color = discord.Color.dark_theme())
        await ctx.send(embed=embed)
        print("Event: ", ctx.author.name, " checked latency.")
    
    @commands.command()
    async def prefix(self, ctx):
        async with ctx.channel.typing():
            prefix = str(ctx.prefix)
            embed = discord.Embed(title="Prefix", description=f"Bot's prefix is: `{prefix}`", color = discord.Color.dark_theme())
        await ctx.send(embed=embed)
        print("Event: ", ctx.author.name, " checked prefix")
    
    @commands.command(aliases=["src", "sourcecode", "botsrc"])
    async def source(self, ctx):
        async with ctx.channel.typing():
            prefix = str(ctx.prefix)
            embed = discord.Embed(title="/src", description="[source code on github](https://github.com/basement-team/RoboBilly)", color = discord.Color.dark_theme())
        await ctx.send(embed=embed)
        print("Event: ", ctx.author.name, " checked bot src")

	
def setup(bot):
	bot.add_cog(Bot(bot))
