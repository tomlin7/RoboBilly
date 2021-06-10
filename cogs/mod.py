
############## MODERATION MODULE ##############

import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, BadArgument
import requests, json 
from datetime import timedelta, datetime


class mod(commands.Cog):
    ## MAIN
    def __init__(self, bot):
        self.bot = bot
    
    ## subclasses
    class count_num:
        def __init__(self, client):
            client.value = 0

        def __ge__(self, other: int):
            return client.value >= other

        def add(self, client):
            client.value += 1
            return client.value
    
    # ROOT FUNCTIONS
    async def get_muted_role(self, guild):
        muted_role = discord.utils.get(guild.roles, name='Muted')
        if muted_role is None:
            muted_permissions = discord.Permissions()
            muted_permissions.send_messages = False
            muted_permissions.add_reactions = False
            muted_role = await guild.create_role(
                name='Muted',
                permissions=muted_permissions,
                color=discord.Color.dark_red()
            )

        return muted_role

    async def log(
        self,
        ctx,
        desc,
        title='**Moderation**',
        color=0xff0000,
        **kwargs
    ):

        guild = ctx.guild
        log_embed = discord.Embed(
            title=title,
            description=desc,
            color=color
        )
        for key, value in kwargs.items():
            if key == 'fields':
                for field in value:
                    if len(field) == 2:
                        log_embed.add_field(
                            name=field[0],
                            value=field[1]
                        )
                    else:
                        log_embed.add_field(
                            name=field[0],
                            value=field[1],
                            inline=field[2]
                        )
            if key == 'showauth':
                if value:
                    author = ctx.author
                    disp_name = author.display_name
                    icon_url = author.avatar_url
                    log_embed.set_author(
                        name=disp_name,
                        icon_url=icon_url
                    )
                    log_embed.set_thumbnail(
                        url=icon_url
                    )
        now = datetime.now()
        log_embed.timestamp = now
        log_channel = discord.utils.get(guild.text_channels, name="mod-logs")
        await log_channel.send(embed=log_embed)
    
    ## MOD COMMANDS
    @commands.command(name='kick', aliases=['k'])
    @has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *_):
        '''Kick a user.
        Example Usage: <prefix>kick <user> [reason] // Kicks <user> reason'''
        msg = ctx.message
        author = ctx.author
        try:
            reason = msg.content.split(None, 1)[1]
            found_reason = True
        except IndexError:
            found_reason = False
        if found_reason:
            await self.log(
                ctx,
                f'<@{author.id} kicked <@{user.id}>',
                fields=[
                    ('**Reason:**', reason)
                ]
            )
            await user.kick(reason=reason)
        else:
            await self.log(
                ctx,
                f'<@{author.id}> kicked <@{user.id}>'
            )
            await user.kick()
        print("Event. ", user, " kicked! by ", author)


    @commands.command(name='ban')
    @has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *argv):
        '''Ban a user.
        Example Usage:
        <prefix>ban <user> [reason]]// Bans <user> from the guild for the reason [reason]'''
        fields = []
        guild = ctx.guild
        argv = list(argv)

        author = ctx.author
        if len(argv) > 0:
            reason = ' '.join(argv)
            fields.append(
                ('**Reason:**', reason, True)
            )

        await self.log(
            ctx,
            f'<@{author.id}> banned <@{user.id}>',
            fields=fields,
            showauth=True
        )
        embed = discord.Embed(
            title='**Ban**',
            description=f'<@{user.id}> has been banned.',
            color=0xff0000
        )
        await user.ban()
        await ctx.send(embed=embed)
        print("Event. ", user, " banned! by ", author)


    @commands.command(name='mute', aliases=['silence'])
    @has_permissions(kick_members=True)
    async def mute(self, ctx, user: discord.Member, time=None, *argv):
        '''Mute a user so that they cannot send messages anymore.
        Example Usage:
        <prefix>mute <user> [reason] // Mutes <user> permanately for reason [reason]'''

        fields = []
        guild = ctx.guild
        argv = list(argv)
        argv.insert(0, time)

        author = ctx.author
        if len(argv) > 0:
            reason = ' '.join(argv)
            fields.append(
                ('**Reason:**', reason, True)
            )
        else:
            fields.append(
                ('**Reason:**', "for some reason", True)
            )


        await self.log(
            ctx,
            f'<@{author.id}> muted <@{user.id}>',
            fields=fields,
            showauth=True
        )
        muted_role = await self.get_muted_role(guild)
        await user.add_roles(muted_role)
        embed = discord.Embed(
            title='**Mute**',
            description=f'<@{user.id}> has been muted.',
            color=0xff0000
        )
        await ctx.send(embed=embed)
        print("Event. ", user, " muted! by ", author, ' Reason: ', reason)


    @commands.command(name='unmute')
    @has_permissions(kick_members=True)
    async def unmute(self, ctx, user: discord.Member, *argv):
        '''Unmute a user.
        Example usage:
        <prefix>unmute <user> oops wrong person // Unbans <user> for the reason oops wrong person.'''
        fields = []
        guild = ctx.guild

        author = ctx.author
        try:
            reason = ' '.join(argv)
            fields.append(
                ('**Reason:**', reason, True)
            )
        except IndexError:
            pass

        await self.log(
            ctx,
            f'<@{author.id}> unmuted <@{user.id}>',
            fields=fields,
            showauth=True
        )
        muted_role = await self.get_muted_role(guild)
        await user.remove_roles(muted_role)
        print("Event. ", user, " unmuted! by ", author, ' Reason: ', reason)


    @commands.command(name='purge')
    @has_permissions(manage_messages=True)
    async def purge(self, ctx, ammount: int, user: discord.Member = None):
        '''
        Bulk delete messages in a channel.
        Example Usage:
        <prefix>purge 20 // Purges the last 20 messages in the channel
        <prefix>purge 20 @baduser#1234 // Purge the last 20 messages by @baduser#1234 in the channel.'''
        channel = ctx.channel
        if ammount > 200:
            await ctx.send("You can't delete more than 200 messages at at time.")

        def check_user(message):
            return message.author == user

        msg = await ctx.send('Purging messages.')
        if user is not None:
            msg_number = self.bot.count_num()

            def msg_check(x):

                if msg_number >= ammount:
                    return False
                if x.id != msg.id and x.author == user:
                    msg_number.add()
                    return True
                return False

            msgs = await channel.purge(
                limit=100,
                check=msg_check,
                bulk=True
            )
            await self.log(
                ctx,
                f"{len(msgs)} of <@{user.id}>'s messages were "
                f"deleted by <@{ctx.author.id}>",
                '**Message Purge**',
                showauth=True
            )
            print("Event.  #Message Purge ", len(msgs), " of ", user.name,'s messages were deleted by ', ctx.author.name)
            # print(msg in msgs, len(msgs))
        else:

            msgs = await channel.purge(
                limit=ammount + 2,
                check=lambda x: x.id != msg.id,
                bulk=True
            )
            await self.log(
                ctx,
                f'{len(msgs)} messages were deleted by <@{ctx.author.id}>',
                '**Message Purge**',
                showauth=True
            )
            print("Event.  #Message Purge ", len(msgs), 'messages were deleted by ', ctx.author.name)
            # print(msg in msgs)

        await msg.edit(content='Deleted messages.')
        await asyncio.sleep(2)
        await msg.delete()
    
    @commands.command(name='slowmode',  aliases=['slow', 'slowmo','Slow', 'Slowmo'])
    @has_permissions(manage_messages=True)
    async def slowmode(self, ctx, seconds: int):
        try:
            await ctx.channel.edit(slowmode_delay=seconds)
            embed = discord.Embed(title="Slowmode", description=f"Set the slowmode delay in this channel to {seconds} seconds!", color=discord.Color.blue())
        except:
            embed = discord.Embed(title="Slowmode", description="Couldn't set slowmode!", color=discord.Color.red())
        await ctx.send(embed=embed)

#===================================== ADD COG ======================================#

def setup(bot):
	bot.add_cog(mod(bot))
