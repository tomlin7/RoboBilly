import discord
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
        embed.add_field(name="Server 2", value="**IP Address**:`51.79.163.221:25583`\n**OP**:<@!517998886141558786>", inline=False)
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
            embed.add_field(name="Server 2", value="**IP Address**: `51.79.163.221:25583`\n**OP**: <@!517998886141558786>\n**Status**: 🟢 Online\n**Players Online**: {0}\n**Minecraft Version:** {1}\n**Latency**: {2}".format(status2.players.online, status2.version.name, status2.latency), inline=False)
        else:
            embed.add_field(name="Server 2", value="IP Address: `51.79.163.221:25583`\nOP: <@!517998886141558786>\nStatus: ⚫ Offline\n".format(), inline=False)
        
        embed.set_footer(text = f"Requested by {ctx.author.name}", icon_url = ctx.author.avatar_url)
        
        await ctx.send(embed=embed)
        
    @mc.command(name="playerlist", aliases=['players', 'onlineplayers', 'playerslist'])
    async def playerlist(self, ctx):
        status1 = None
        status2 = None
        
        msg1 = ""
        msg2 = ""
        
        try:
            server = MinecraftServer.lookup("billysbasement.aternos.me")
            status1 = server.status()
        except Exception as e:
            print(e)
            # await ctx.send(e)
        
        try:
            server1 = MinecraftServer.lookup("147.135.71.70:25592")
            status2 = server1.status()
        except Exception as e:
            print(e)
            # await ctx.send(e)

        try:
            if status1 is None:
                msg1 += "Server Offline!"
            else:
                try:
                    for x in status1.players.sample:
                        msg1 += f"🔸 {x.name}\n"
                except:
                    msg1 += "\nThere are no players online!"
            print(msg1)
        except:
             msg1 += "..."
        
        try:
            if status2 is None:
                msg2 += "Server Offline!"
            else:
                try:
                    for x in status2.players.sample:
                        msg2 += f"🔹 {x.name}\n"
                except:
                    msg2 += "\nThere are no players online!"
            print(msg2)
        except:
             msg2 += "..."
        
        if msg1 == "" or msg1 is None:
            msg1 += "..."
        if msg2 == "" or msg2 is None:
            msg2 += "..."
        
        # await ctx.send(msg1)
        # await ctx.send(msg2)
        em = discord.Embed(title="Online Players", color=discord.Color.dark_theme())
        em.add_field(name="billysbasement.aternos.me", value=msg1, inline=False)
        em.add_field(name="147.135.71.70:25592", value=msg2, inline=False)
        await ctx.send(embed=em)
        
def setup(bot):
    bot.add_cog(Minecraft(bot))
