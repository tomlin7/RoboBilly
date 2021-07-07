from discord.ext import commands
from discord import Embed, Color

from mcstatus import MinecraftServer


class Minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group(name="mc")
    async def mc(self, ctx):
        pass
    
    @commands.command(name="coord", aliases=["coordinates", "pos", "coords"])
    async def coord(self, ctx, x=0, y=0, z=0):
        await ctx.send(embed=Embed(title="", description=f"X: **{x}**, Y: **{y}**, Z: **{z}**", color=Color.dark_theme()))
        
    @mc.command(name="ip", aliases=["serverip", "mcip"])
    async def ip(self, ctx):
        embed = Embed(title="Basement Minecraft Servers", description="__**Info**__\nYour Minecraft version should match **1.17**.", color=Color.dark_theme())
        embed.add_field(name="Server 1", value="**IP Address**:`billysbasement.aternos.me`\n**OP**:<@!621397007332016145>", inline=False)
        embed.add_field(name="Server 2", value="**IP Address**:`147.135.71.70:25592`\n**OP**:<@!517998886141558786>", inline=False)
        await ctx.send(embed=embed)
    
    
    
    @mc.command(name="serverinfo", aliases=["sinfo", "mcinfo"])
    async def serverinfo(self, ctx):
        status1 = None
        status2 = None
        try:
            server1 = MinecraftServer.lookup("billysbasement.aternos.me:54987")
            status1 = server1.status()
        except:
            pass
        try:
            server2 = MinecraftServer.lookup("147.135.71.70:25592")
            status2 = server2.status()
        except:
            pass
        
        embed = Embed(title="Basement Minecraft Servers Info", description="__**Info**__\nAsk the OP's for help if you can't join the server.\nPing them if the server is offline and you want to join, they will help you.", color=Color.dark_theme())
        
        if status1 is None and status2 is None:
            embed.add_field(name="Servers are Offline", value="Sorry both of the servers are offline at the moment. Please Try asking server OP's.", inline=False)
        
        if status1 is not None:
            embed.add_field(name="Server 1", value="**IP Address**: `billysbasement.aternos.me`\n**OP**: <@!621397007332016145>\n**Status**: 🟢 Online\n**Players Online**: {0}\n**Minecraft Version:** {1}\n**Latency**: {2}".format(status1.players.online, status1.version.name, status1.latency), inline=False)
        else:
            embed.add_field(name="Server 1", value="IP Address: `billysbasement.aternos.me`\nOP: <@!621397007332016145>\nStatus: ⚫ Offline\n".format(), inline=False)
        
        if status2 is not None:
            embed.add_field(name="Server 2", value="**IP Address**: `147.135.71.70:25592`\n**OP**: <@!517998886141558786>\n**Status**: 🟢 Online\n**Players Online**: {0}\n**Minecraft Version:** {1}\n**Latency**: {2}".format(status2.players.online, status2.version.name, status2.latency), inline=False)
        else:
            embed.add_field(name="Server 2", value="IP Address: `147.135.71.70:25592`\nOP: <@!517998886141558786>\nStatus: ⚫ Offline\n".format(), inline=False)
        
        embed.set_footer(text = f"Requested by {ctx.author.name}", icon_url = ctx.author.avatar_url)
        
        await ctx.send(embed=embed)
        
@mc.command(aliases=['players', 'onlineplayers'])
async def serverplayers(ctx):
    status = None
    status1 = None
    msg = ""
    msg1 = ""
    try:
        server = MinecraftServer.lookup("billysbasement.aternos.me")
        status = server1.status()
    except:
        pass
    try:
        server1 = MinecraftServer.lookup("147.135.71.70:25592")
        status1 = server1.status()
    except:
        pass
    if status1 is not None and status1.players.sample is not None:
        for x in status1.players.sample:
            msg1 += f"{x.name}\n"
    elif status1 is None:
        msg1 += "Server Offline!"
    elif status1.players.sample is None:
        msg1 += "There are no players online!"
    if status is not None and status.players.sample is not None:
        for x in status.players.sample:
            msg += f"{x.name}\n"
    elif status is None:
        msg += "Server Offline!"
    elif status.players.sample is None:
        msg += "There are no players online!"
        
    em = discord.Embed(title="Online Players", color=discord.Color.dark_theme())
    em.add_field(name="billysbasement.aternos.me", value=msg)
    em.add_field(name="147.135.71.70:25592", value=msg1, inline=False)
    await ctx.send(embed=em)
        
def setup(bot):
    bot.add_cog(Minecraft(bot))
