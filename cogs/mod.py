
############## MODERATION MODULE ##############

import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ext.commands.cooldowns import BucketType
import requests, json 
from datetime import datetime
import pymongo
from pymongo import MongoClient

with open("./config.json", "r") as f:
    config = json.load(f)
    mongo_url = config['mongo_url']
cluster = MongoClient(mongo_url)
repdb = cluster["ReputationData"]

# functions:
def rsetup(col):
    col = str(col)
    return repdb[col]

def reputation(userid, collection):
    query = {"_id": userid}
    user = collection.find(query)
    for result in user:
        return result["reputation"]

def getEmbed(Title, msg):
    embed = discord.Embed(title=Title, description=msg, color=discord.Color.blue())
    return embed

def does_not_exist(userid, collection):
    check_query = { "_id": userid }
    return (collection.count_documents(check_query) == 0)


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
        log_channel = discord.utils.get(guild.text_channels, name="billy-logs")
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
    
    @commands.command(name='slowmode')
    @has_permissions(manage_messages=True)
    async def slowmode(self, ctx, seconds: int):
        try:
            await ctx.channel.edit(slowmode_delay=seconds)
            embed = discord.Embed(title="Slowmode", description=f"Set the slowmode delay in this channel to {seconds} seconds!", color=discord.Color.blue())
        except:
            embed = discord.Embed(title="Slowmode", description="Couldn't set slowmode!", color=discord.Color.red())
        await ctx.send(embed=embed)
	
    @commands.command(name="rep", aliases=['reputation'])
    @has_permissions(manage_messages=True)
    async def rep(self, ctx, userr: discord.Member, score: int = None):
        """check/give reputation"""
        await ctx.trigger_typing()
        await ctx.message.delete()

        collection = rsetup(ctx.guild.id)
        user = userr.id
        username = str(userr)
        score = score

        # data doesn't exist
        if (does_not_exist(userr.id, collection)):
            if not score:
                post = {
                    '_id': user,
                    'name': username,
                    'reputation': 10
                }
                collection.insert_one(post)
                
                current_reputation = reputation(user, collection)
                message = f"{userr.name} has {current_reputation} reputation in this server."
                embed = getEmbed("Reputation", message)
                await ctx.send(embed=embed)
            else:
                post = {
                    '_id': user,
                    'name': username,
                    'reputation': score
                }
                collection.insert_one(post)

                current_reputation = reputation(user, collection)
                message = f"{userr.name} has currently {current_reputation} reputation."
                embed = getEmbed("Reputation", message)
                await ctx.send(embed=embed)
        # data do exist
        else:
            if not score:
                current_reputation = reputation(user, collection)
                message = f"{userr.name} has {current_reputation} reputation in this server."
                embed = getEmbed("Reputation", message)
                await ctx.send(embed=embed)
            else:
                current_reputation = reputation(user, collection)
                current_reputation += score
                collection.update_one({"_id":user}, {"$set":{"name": username,"reputation": current_reputation}})

                current_reputation = reputation(user, collection)
                message = f"{userr.name} now has {current_reputation} reputation."
                embed = getEmbed("Reputation", message)
                await ctx.send(embed=embed)
        await self.log(
            ctx,
            f"{user.name}'s reputation data has been updated by {ctx.author.name}.",
            '**Reputation**',
            showauth=True
        )

    @commands.command(name="reset", aliases=['r', 'Reset'])
    @has_permissions(manage_messages=True)
    async def reset(self, ctx, userr: discord.Member):
        user = userr.id
        collection = rsetup(ctx.guild.id)
        current_reputation = 10
        collection.update_one({"_id":user}, {"$set":{"reputation": current_reputation}})
        message = f"{user.name}'s reputation data has been cleaned."
        embed = getEmbed("User Data Reset", message)
        await ctx.send(embed=embed)

        await self.log(
            ctx,
            f"{user.name}'s reputation data has been cleaned by {ctx.author.name}.",
            '**User Data Reset**',
            showauth=True
        )

    @commands.command(name="thanks", aliases=['thx', 'thnx'])
    @commands.guild_only()
    @commands.cooldown(rate=1, per=600, type=BucketType.user)
    async def Thanks(self, ctx, user: discord.Member):
        if ctx.author.id == user.id:
            return
        collection = rsetup(ctx.guild.id)
        user = user.id
        username = str(user)
        check_query = { "_id": user }


        if (collection.count_documents(check_query) == 0):
            post = {
                '_id': user,
                'name': username,
                'reputation': 11
            }
            collection.insert_one(post)
        else:
            current_reputation = reputation(user, collection)
            current_reputation += 1
            collection.update_one({"_id":user}, {"$set":{"reputation": current_reputation}})
        await self.log(
            ctx,
            f"{user.name}'s got thanked by {ctx.author.name}.",
            '**Thanks Reputation**',
            showauth=True
        )

#===================================== ADD COG ======================================#

def setup(bot):
	bot.add_cog(mod(bot))
