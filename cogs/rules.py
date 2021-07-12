import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType


class crules(object):
    rules = [
        "Follow the Discord Terms of Service and the Community Guidelines",
        "Don't be an asshole",
        "No discord invite links",
        "NSFW content is not allowed to any degree",
        "Keep it english in every chat",
        "No Political, religious, racial or highly depressive discussions",
        "Keep content in their respective channels",
        "No Promotion outside of #🔰│promotion",
        "Do not share personal information about others without their consent",
        "Staff will always have the last word",
        "Do not minimod",
        "Keep chat clean"
    ]

    ruleinfo = [
        "You can find the TOS here and the Community Guidelines at https://discord.com/terms.",
        "This includes things spamming, spoiling and being disrespectful.",
        "This includes sending invite links to server members without it being previously discussed.",
        "This also means any memes that are NSFW are not allowed.",
        "You are only allowed to speak a different language in #🤠│spam-east.",
        "If you feel like anyone is overstepping this rule, ping a staff member.",
        "Read channel descriptions and names.",
        "This includes telling people to check out #🔰│promotion.",
        "Respect each others privacy.",
        "If you feel like you’ve been treated unfairly, contact a staff member of higher power.",
        "This means if someone is breaking the rules, do not personally tell them not to, instead DM or ping staff about it and let the staff handle it.",
        "This mean no full caps, no copypastas or tYpInG LiKE tHIs."
    ]


class rules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # variables
    right = '✅'
    wrong = '❌'

    def hembed(self, st: bool):
        if st:
            embed = discord.Embed(
                color=discord.Color.blue()
            )
        else:
            embed = discord.Embed(
                color=discord.Color.red()
            )
        return embed

    @commands.command(name="rule")
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(rate=1, per=3, type=BucketType.default)
    async def _rule(self, ctx, n: int=None):
        '''Displays the nth rule, if exits'''
        await ctx.message.delete()

        await ctx.trigger_typing()
        if n is not None:
            try:
                # deciding values
                rulenumber = 'Rule {0}'.format(n)
                rule = crules.rules[n - 1]
                ruleinfo = crules.ruleinfo[n - 1]

                # sending information
                embed = self.hembed(True)
                embed.set_author(name=rulenumber)

                # fields
                embed.add_field(name=rule, value=ruleinfo, inline=False)

                # indication
                emoji = self.right
            except:
                embed = self.hembed(False)

                # fields
                embed.add_field(name="syntax error", value="Rule doesn't exist", inline=False)

                # indication
                emoji = self.wrong
        else:
            # sending information
            embed = self.hembed(False)
            embed.set_author(name="Server Rules Command")

            # fields
            embed.add_field(name="How to use it?", value="Add the Number of rule you want to see/show as an argument \n > []rule [number]", inline=False)

            # indication
            emoji = self.right
        sent = await ctx.send(embed=embed)

        # indication
        await sent.add_reaction(emoji)

    @commands.command(name="rules")
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(rate=1, per=3, type=BucketType.default)
    async def _rules(self, ctx):
        '''Displays all rules in one command'''
        await ctx.message.delete()

        ctx.trigger_typing()
        embed = self.hembed(True)
        embed.set_author(name='Server Rules!')
        if len(crules.rules) != 0:
            # indication
            emoji = self.right

            # fields
            for i in range(len(crules.rules)):
                # deciding values in each loop
                rulenumber = 'Rule {0}'.format(i+1)
                description = ("**{0}**\n{1}".format(crules.rules[i], crules.ruleinfo[i]))

                # adding field
                embed.add_field(name=rulenumber, value=description, inline=False)
        else:
            # indication
            emoji = self.wrong

            # fields
            embed.add_field(name="No Server Rules", value="This server currently has no rules set", inline=False)
        embed.set_footer(text='use []rule [number] to view each rules*')

        # indication
        sent = await ctx.send(embed=embed)
        await sent.add_reaction(emoji)

# =========================================================================================== #
def setup(bot):
    bot.add_cog(rules(bot))