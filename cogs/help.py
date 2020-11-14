##### HELP MODULE ######
import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, BadArgument
import requests, json
from datetime import timedelta, datetime

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #variables
    right = '✅'
    wrong = '❌'

    #because help+embed = hembed, lol
    def hembed(self, st: bool):
        if st:
            embed = discord.Embed(
                color = discord.Color.blue()
            )
        else:
            embed = discord.Embed(
                color = discord.Color.red()
            )
        return embed
    
#=================================================MAIN ==================================================#

    @commands.group()
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.trigger_typing()
            await asyncio.sleep(2)
            embed = discord.Embed(color = discord.Color.blue())
            embed.set_author(name='Help - Modules')
            embed.add_field(name='Mod', value='Moderation commands (staff only)', inline=False)
            embed.add_field(name='User', value='commands available for all members', inline=False)
            embed.add_field(name='Bot', value='Bot related commands', inline=False)
            embed.add_field(name='ModMail', value='Manage modmails (staff only)', inline=False)
            embed.set_footer(text="use  []help <module> ")
            mhelp = await ctx.send(embed=embed)
            emoji = self.right
            await mhelp.add_reaction(emoji)
    
#========================================== HELP MODULES =================================================#


    @help.command(name='mod', aliases=['Mod', 'MOD'])
    async def mod(self, ctx, page: int=1):
        await ctx.trigger_typing()
        total_pages = 1
        if page == 1 or page is None:
            embed = self.hembed(True)
            embed.set_author(name='Help')

            # fields
            embed.add_field(name='kick', value='Kick a member from server', inline=False)
            embed.add_field(name='ban', value='ban a member from server', inline=False)
            embed.add_field(name='mute', value='mute a member', inline=False)
            embed.add_field(name='unmute', value='unmute a muted Member', inline=False)
            embed.add_field(name='purge', value='bulk delete message', inline=False)
            
            # details
            embed.set_footer(text=f'page {page}/{total_pages}')
            emoji = self.right
        else:
            embed = self.hembed(False)
            embed.set_author(name='Help')

            # fields
            embed.add_field(name='Page not found', value="For this module that page doesn't exist", inline=False)
            
            # details
            embed.set_footer(text=f'Total pages - {total_pages}')
            emoji = self.wrong
        await asyncio.sleep(2)
        mhelp = await ctx.send(embed=embed)
        await mhelp.add_reaction(emoji)
    
    @help.command(name='user', aliases=['User', 'USER'])
    async def user(self, ctx, page: int = 1):
        await ctx.trigger_typing()
        total_pages = 2
        if page == 1:
            embed = self.hembed(True)
            embed.set_author(name='Help')

            # fields
            embed.add_field(name='say', value='Repeats you', inline=False)
            embed.add_field(name='hi', value='say hi ( ~~for some reason~~ )', inline=False)
            embed.add_field(name='info', value='Get to ~~spy~~ know about a user.', inline=False)
            embed.add_field(name='weather', value='description', inline=False)
            embed.add_field(name='brainfuck', value='The BrainFuck Interpreter!', inline=False)
            embed.add_field(name='jb', value='The JB Interpreter! ', inline=False)
            
            # details
            embed.set_footer(text=f'page {page}/{total_pages}')
            emoji = self.right
        elif page == 2:
            embed = self.hembed(True)
            embed.set_author(name='Help')

            # fields
            embed.add_field(name='goodmorning', value='Wish Good Morning', inline=False)
            embed.add_field(name='goodnight', value='Wish Good night', inline=False)
            embed.add_field(name='google', value='description', inline=False)
            embed.add_field(name='bing', value='description', inline=False)
            embed.add_field(name='dontasktoask', value="don't ask to ask, Just ask!", inline=False)
            embed.add_field(name='ascii', value='Ascii art', inline=False)
            
            # details
            embed.set_footer(text=f'page {page}/{total_pages}')
            emoji = self.right
        elif page is None:
            embed = self.hembed(True)
            embed.set_author(name='Help')

            # fields
            embed.add_field(name='say', value='Repeats you', inline=False)
            embed.add_field(name='hi', value='say hi ( ~~for some reason~~ )', inline=False)
            embed.add_field(name='info', value='Get to ~~spy~~ know about a user.', inline=False)
            embed.add_field(name='weather', value='description', inline=False)
            embed.add_field(name='brainfuck', value='The BrainFuck Interpreter!', inline=False)
            embed.add_field(name='jb', value='The JB Interpreter! ', inline=False)
            
            # details
            embed.set_footer(text=f'page {page}/{total_pages}')
            emoji = self.right
        else:
            embed = self.hembed(False)
            embed.set_author(name='Help')

            # fields 
            embed.add_field(name='Page not found', value="For this module that page doesn't exist", inline=False)
            
            # details
            embed.set_footer(text=f'Total pages - {total_pages}')
            emoji = self.wrong
        await asyncio.sleep(2)
        mhelp = await ctx.send(embed=embed)
        await mhelp.add_reaction(emoji)
    
    @help.command(name='bot', aliases=['Bot', 'BOT'])
    async def bot(self, ctx, page: int=1):
        await ctx.trigger_typing()
        total_pages = 1
        if page == 1 or page is None:
            embed = self.hembed(True)
            embed.set_author(name='Help')

            # fields
            embed.add_field(name='ping', value='get the latency of  the bot', inline=False)
            embed.add_field(name='prefix', value='get the prefix of the bot', inline=False)
            embed.add_field(name='help', value="what you are lookin' at.\nuse without arguments for seeing available modules", inline=False)
            
            # details
            embed.set_footer(text=f'page {page}/{total_pages}')
            emoji = self.right
        else:
            embed = self.hembed(False)
            embed.set_author(name='Help')

            # fields
            embed.add_field(name='Page not found', value="For this module that page doesn't exist", inline=False)
            
            # details
            embed.set_footer(text=f'Total pages - {total_pages}')
            emoji = self.wrong
        await asyncio.sleep(2)
        mhelp = await ctx.send(embed=embed)
        await mhelp.add_reaction(emoji)
    
    @help.command(name='modmail', aliases=['ModMail', 'Modmail', 'modMail', 'MODMAIL'])
    async def modmail(self, ctx, page: int=1):
        await ctx.trigger_typing()
        total_pages = 1
        if page == 1 or page is None:
            embed = self.hembed(True)
            embed.set_author(name='Help')

            # fields
            embed.add_field(name='reply', value='reply to modmails', inline=False)
            embed.add_field(name='setup', value='setup modmails channel', inline=False)

            # details
            embed.set_footer(text=f'page {page}/{total_pages}')
            emoji = self.right
        else:
            embed = self.hembed(False)
            embed.set_author(name='Help')

            # fields
            embed.add_field(name='Page not found', value="For this module that page doesn't exist", inline=False)

            # details
            embed.set_footer(text=f'Total pages - {total_pages}')
            emoji = self.wrong
        await asyncio.sleep(2)
        mhelp = await ctx.send(embed=embed)
        await mhelp.add_reaction(emoji)
    
#================================ ERROR MANAGEMENT ===================================#

    @modmail.error
    async def modmail_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.trigger_typing()
            embed = discord.Embed(title="Syntax Error", description="check the arguments given. \n> <prefix>help modmail [page]", color=discord.Color.red())
            await ctx.send(embed=embed)
    @bot.error
    async def bot_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.trigger_typing()
            embed = discord.Embed(title="Syntax Error", description="check the arguments given. \n> <prefix>help bot [page]", color=discord.Color.red())
            await ctx.send(embed=embed)
    @user.error
    async def user_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.trigger_typing()
            embed = discord.Embed(title="Syntax Error", description="check the arguments given. \n> <prefix>help user [page]", color=discord.Color.red())
            await ctx.send(embed=embed)
    @mod.error
    async def mod_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.trigger_typing()
            embed = discord.Embed(title="Syntax Error", description="check the arguments given. \n> <prefix>help mod [page]", color=discord.Color.red())
            await ctx.send(embed=embed)

#===================================== ADD COG ======================================#

def setup(bot):
	bot.add_cog(help(bot))