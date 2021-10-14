import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType


rules = [
    "Refrain from being rude to other members.",
    "Please avoid controversial topics!",
    "Use collaboration channel for recruiting teams.",
    "Keep it clean.",
    "Don't ask to ask, Just ask.",
    "Use the template for collaboration Posts.",
    "Follow the Discord Terms of Services!",
    "Advertise only in Promotion channel ",
    "Space out your Ads.",
    "Google/Bing before asking.",
    "English only.",
    "Follow Wheaton's law."
]

ruleinfo = [
    "They're people too! If you have an issue with someone, call for a staff member or continue talking with that person in DMs. Discriminatory jokes and language, hate speech (which calls out a group by their age, race, gender), etc. are strictly prohibited. Any kind of verbal abuse, insults, or threats towards others is strictly prohibited.",
    "Avoid controversial topics such as Religion, Politics, Suicide, etc. This is a programmers' server. There is a time and place for everything and this server ain't the place!",
    "If you want work done for you, you can find people to work with you in  #collaboration channel.",
    "Displaying offensive, derogatory, or sexually explicit content is not allowed.",
    "Don't ask 'can someone help me', don't ping random users, don't ask for DMs. We are here to help! If you're asking in the Development & Help category, you can skip the needless introductions. We'd much rather you just ask your question outright.",
    "When posting in #collaboration channel, please try to follow the format provided.(check pinned messages).",
    "This includes no piracy links, although discussions are fine.",
    "Advertise gamedev-programming-related content in #promotion channel. Showcase your works in progress in #showcase. Any non-programmer-gamedev-related content will be deleted. (NOTE: Discord server links are not allowed, please reach out to the staff if you'd like to have partnerships).",
    "Space out your posts in #promotion and #showcase channels. Give other people a chance to be seen.",
    "Before asking for help, please google/bing your issue first, attempt to solve it yourself, and then ask. You learn more this way than being spoon-fed!",
    "We are an English community around English content with English speaking moderation team. Everyone here understands English, other languages not so much. You are only allowed to speak other languages in the spam/misc category.",
    "Do not be a idiot."
]


class Rules(commands.Cog):
    """
    This cog provides server rules related commands, such as showing nth rule, sending all rules, etc.
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="rule", aliases=["ruleno"])
    @commands.guild_only()
    @commands.cooldown(rate=1, per=3, type=BucketType.default)
    async def _rule(self, ctx, n: int=None):
        """
        Displays the nth rule, if exits
        """

        await ctx.trigger_typing()

        embed = None
        
        if n is not None:
            try:
                embed = discord.Embed(title=f'Rule {n}', color = discord.Color.dark_theme())
                embed.add_field(name=rules[n - 1], value=ruleinfo[n - 1])
            except:
                embed = discord.Embed(color = discord.Color.dark_theme())
                embed.add_field(name="Rule Not Found", value=f"Rule with index {n} doesn't exist.")
        else:
            embed = discord.Embed(title='Rule N', color = discord.Color.dark_theme())
            embed.add_field(name="Usage", value="Pass the index of the rule to be shown as an argument as follows:\n > ```[]rule [number]```")
        
        await ctx.send(embed=embed)

    @commands.command(name="rules", aliases=["all_rules", "allrules"])
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(rate=1, per=3, type=BucketType.default)
    async def _rules(self, ctx):
        """
        Displays all rules.
        """
        
        await ctx.trigger_typing()
        
        embed = discord.Embed(title=f"#Rules", color = discord.Color.dark_theme())

        for i in range(len(rules)):
            description = ("**{0}**\n```{1}```".format(rules[i], ruleinfo[i]))
            embed.add_field(name=f"Rule {i + 1}", value=description, inline=False)
        
        embed.set_footer(text=f"Currently have {len(rules)} rules.")
        await ctx.send(embed=embed)
        

def setup(bot):
    bot.add_cog(Rules(bot))
