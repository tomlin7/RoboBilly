from discord.ext import commands
import random

class Ajian(commands.Cog):
    """
    Commands related to the bot.
    """
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group()
    async def ajian(self, ctx):
        """
        >.<
        """
        if ctx.invoked_subcommand is None:
            await ctx.send("no u")
        
    @ajian.command()
    async def bonk(self, ctx):
        if random.choice([True, False]):
            await ctx.send(f"_bonks ajian{('', '**gently**')[bool(random.randint(0, 10) == 5)]}_")
        else:
            await ctx.send("You got bonked by ajian, get got!")


    @ajian.command()
    async def hug(self, ctx):
        await ctx.send("*ajian hugs back* 🤍")

    @ajian.command()
    async def owo(self, ctx):
        await ctx.send("UwU")


def setup(bot):
    bot.add_cog(Ajian(bot))
