import discord
from discord.ext import commands

from libs import config

class Events(commands.Cog):
    """
    Bot events.
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'We have logged in as {self.bot.user}')
        await self.bot.change_presence(activity=discord.Game(name=config.special_event))
        config.load_config(self.bot)

        print("Session started.")


def setup(bot):
    bot.add_cog(Events(bot))
