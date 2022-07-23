"""
Brainfuck Module
"""

import discord
import asyncio
from discord.ext import commands

from cogs.libs import brainfuck
from libs import config


class BrainFuck(commands.Cog):
    """
    Commands related to the bot.
    """
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='bf', aliases=['brainfuck', 'BrainFuck'])
    async def bf(self, ctx, *, source = None):
        """Brainfuck Interpreter"""
        await ctx.trigger_typing()

        if source is None:
            await ctx.send(f"> You need provide some input. see `{config.prefix}help brainfuck`")
            return
        
        result = brainfuck.evaluate(source)
        embed = discord.Embed(title="🧠 Billy's BrainFuck Interpreter", color = discord.Color.dark_theme())

        if result is not None or result != "":    
            embed.add_field(name='Output', value=f"> {result}")
        else:
            embed.add_field(name='Runtime Error', value="> Recheck what you typed.")
        
        embed.set_footer(text="Copyright (c) 2021 Basement Team")
        await ctx.send(embed=embed)
	
def setup(bot):
	bot.add_cog(BrainFuck(bot))
