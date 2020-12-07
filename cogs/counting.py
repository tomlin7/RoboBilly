import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, BadArgument
import requests, json
from datetime import timedelta, datetime

count = 1

class counting(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.count = count

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.channel.name == "count" and message.author != self.bot.user:
			if message.content == str(self.count):
				self.count += 1
				await message.channel.send(str(self.count))
				self.count += 1
	
	@commands.command(name="setcount", aliases=["setCount", "set_count", "countingset"])
	@has_permissions(manage_messages=True)
	async def setcount(self, ctx, number: int):
		self.count = int(number)
		await ctx.trigger_typing()
		embed = discord.Embed(title="Counting", description=f"Current count is set to {self.count}", color=discord.Color.blue())
		await ctx.send(embed=embed)

	@setcount.error
	async def setcount_error(self, ctx, error):
		if isinstance(error, commands.BadArgument):
			await ctx.trigger_typing()
			embed = discord.Embed(title="Syntax Error", description="check the arguments given. \n> <prefix>setcount [number]", color=discord.Color.red())
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(counting(bot))