import os
import asyncio
import discord
import requests, json 
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument
from datetime import timedelta, datetime
from cogs.libs import brainfuck   # BrainFu*k Interpreter
from cogs.libs import getch
from libs import httpsession
# from cogs.libs.JB import jbin     #JB Interpreter - JB language is in beta

#===================================== ROOT =========================================#

with open('./config.json') as f:
  data = json.load(f)
  token = data['Token']
  prefix = data['Prefix']
print(f"Prefix is {prefix}, you can change it in config.json")

client = commands.Bot(command_prefix=commands.when_mentioned_or(prefix), intents = discord.Intents.all())

os.environ.setdefault("JISHAKU_NO_UNDERSCORE", "1")

#================================ COGS & EXTENSIONS =================================#

client.load_extension('jishaku')
client.load_extension('cogs.anisearch')
# client.load_extension('cogs.emojify')
# client.load_extension('cogs.counting')
client.load_extension('cogs.mod')
client.load_extension('cogs.user')
client.load_extension('cogs.catify')
client.load_extension('cogs.latex')
client.load_extension('cogs.cheatsheet')
client.load_extension('cogs.githubinfo')
client.load_extension('cogs.Bot')
client.load_extension('cogs.minecraft')
client.load_extension('cogs.modmail')
client.load_extension('cogs.rules')
client.load_extension('cogs.fun')
client.load_extension('cogs.chess')
client.load_extension('cogs.events')
client.load_extension('cogs.error_handling')

#===================================== EVENTS =======================================#

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="Beanson"))

#=================================== INTERPRETERS =======================================#

@client.command(name='bf', aliases=['brainfuck', 'BrainFuck'])
async def bf(ctx, *, thing: str = None):
    """Brainfuck Interpreter"""
    await ctx.trigger_typing()
    sourcecode = thing
    result = brainfuck.evaluate(sourcecode)
    if result is not None:
        embed = discord.Embed(color = discord.Color.blue())
        embed.set_author(name="Billy's BrainFuck Interpreter")
        embed.add_field(name='Output', value=f"> {result}")
    else:
        embed = discord.Embed(color = discord.Color.red())
        embed.set_author(name="Billy's BrainFuck Interpreter")
        embed.add_field(name='Syntax Error', value="> No result for you, shoo shoo")
    await ctx.send(embed=embed)

# @client.command(name='jb', aliases=['jB', 'Jb', 'JB'])
# async def jb(ctx, *, thing):
#     """JB Interpreter"""
#     await ctx.trigger_typing()
#     result = jbin(thing)
#     if result is not None:
#         embed = discord.Embed(color = discord.Color.blue())
#         embed.set_author(name="JB Interpreter")
#         embed.add_field(name='Output', value=f"> {result}")
#     else:
#         embed = discord.Embed(color = discord.Color.red())
#         embed.set_author(name="JB Interpreter")
#         embed.add_field(name='Syntax Error', value="> No result for you, shoo shoo")
#     await ctx.send(embed=embed)
# @jb.error
# async def jb_error(ctx, error):
#     if isinstance(error, MissingRequiredArgument):
#         await ctx.trigger_typing()
#         embed = discord.Embed(color = discord.Color.red())
#         embed.set_author(name="JB Interpreter")
#         embed.add_field(name='Syntax Error', value="> I think you need to put smthn, lol")
#         await ctx.send(embed=embed)

class NewHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        e = discord.Embed(color=discord.Color.dark_theme(), description='')
        for page in self.paginator.pages:
            e.description += page
        await destination.send(embed=e)

client.help_command = NewHelpCommand()
        
#=================================== bot start =====================================#

client.run(os.getenv("DISCORD_TOKEN"))
