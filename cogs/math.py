"""
Math Module
"""

import discord
import asyncio
from discord.ext import commands

from libs import config
from cogs.libs.math import evaluate

class Math(commands.Cog):
    """
    Commands related to the bot.
    """
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='math', aliases=['Math', 'eval', 'e'])
    async def math(self, ctx, *, source=None):
        """
        Math Interpreter
        """
        await ctx.trigger_typing()
        if source is None:
            await ctx.send(f"> You need provide some input. see `{config.prefix}help math`")
            return
        
        result = evaluate(source)
        embed = discord.Embed(title="💡 Billy's Math Interpreter", color = discord.Color.dark_theme())
        
        if result is not None:
            embed.add_field(name='Output:', value=f"> {result}\n")
        else:
            embed.add_field(name='Runtime Error', value="> Recheck what you typed.\n")
        
        embed.set_footer(text="Copyright (c) 2021 Basement Team")
        await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Math(bot))
