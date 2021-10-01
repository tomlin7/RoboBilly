import discord
from discord.ext import commands

class HelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        e = discord.Embed(color=discord.Color.dark_theme(), description='')
        for page in self.paginator.pages:
            e.description += page
        await destination.send(embed=e)