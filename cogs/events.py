from discord.ext import commands


class Events(commands.Cog):
    """
    Bot events.
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Session Started.")


def setup(bot):
    bot.add_cog(Events(bot))
