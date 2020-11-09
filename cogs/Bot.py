###### BOT MODULE ######

import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, BadArgument

class Bot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        async with ctx.channel.typing():
    	    await asyncio.sleep(2)
    	    ping = str(self.bot.latency * 100)
    	    embed = discord.Embed(title="Pong!", description=f'Ping: {ping} ms', color = discord.Color.blue())
        await ctx.send(embed=embed)
        print("Event. ", ctx.author.name, " pinged! pong!")
    
    @commands.command()
    async def prefix(self, ctx):
        async with ctx.channel.typing():
            await asyncio.sleep(2)
            prefix = str(ctx.prefix)
            embed = discord.Embed(title="Prefix", description=f"Bot's prefix is: `{prefix}`", color = discord.Color.blue())
        await ctx.send(embed=embed)
        print("Event. ", ctx.author.name, " checked Prefix")

#===================================== ADD COG ======================================#

def setup(bot):
	bot.add_cog(Bot(bot))