import discord
from discord.ext import commands


class ErrorHandling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """Command error handler"""
        embed = discord.Embed(color=discord.Color.red())
        if isinstance(error, commands.CommandNotFound):
            embed.title = "Command not Found"
            embed.description = "Recheck what you've typed."
            await ctx.send(embed=embed)

        elif isinstance(error, commands.CommandOnCooldown):
            embed.title = "Whoa chill with it"
            embed.description = "Command is on cooldown."
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(ErrorHandling(bot))
