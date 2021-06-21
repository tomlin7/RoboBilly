from discord.ext import commands
from discord import Embed, Color


class Minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.command(name="ip")
    async def _ip(self, ctx, x=0, y=0, z=0):
        await ctx.send(embed=Embed(title="", description=f"X: **{x}**, Y: **{y}**, Z: **{z}**", color=Color.dark_theme()))
        
def setup(bot):
    bot.add_cog(Minecraft(bot))
