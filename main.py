import os
import discord
from discord.ext import commands

from libs import config
from libs import help
from libs import httpsession

client = commands.Bot(command_prefix=commands.when_mentioned_or(config.prefix), intents = discord.Intents.all())

# Load cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.load_extension('jishaku')

client.help_command = help.HelpCommand()
client.run(config.DISCORD_TOKEN)
