from discord.ext import commands
from discord import Embed, Color


class Minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.command(name="coord", aliases=["coordinates", "pos"])
    async def coord(self, ctx, x=0, y=0, z=0):
        await ctx.send(embed=Embed(title="", description=f"X: **{x}**, Y: **{y}**, Z: **{z}**", color=Color.dark_theme()))
        
    @commands.command(name="ip", aliases=["serverip", "mcip"])
    async def ip(self, ctx):
        embed = Embed(title="Basement Minecraft Servers", description="__**Info**__\nYour Minecraft version should match **1.17**.\nCracked accounts are allowed to join.", color=Color.dark_theme())
        embed.add_field(name="Server 1", value="**IP Address**:`billysbasement.aternos.me`\n**OP**:<@!621397007332016145>", inline=False)
        embed.add_field(name="Server 2", value="**IP Address**:`147.135.71.70:25592`\n**OP**:<@!517998886141558786>", inline=False)
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Minecraft(bot))
