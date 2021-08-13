import random
import discord
from discord import AllowedMentions, Embed, Forbidden
from discord.ext import commands

cats = ["ᓚᘏᗢ", "ᘡᘏᗢ", "🐈", "ᓕᘏᗢ", "ᓇᘏᗢ", "ᓂᘏᗢ", "ᘣᘏᗢ", "ᕦᘏᗢ", "ᕂᘏᗢ"]

NEGATIVE_REPLIES = [
    "Noooooo!!",
    "Nope.",
    "I'm sorry Dave, I'm afraid I can't do that.",
    "I don't think so.",
    "Not gonna happen.",
    "Out of the question.",
    "Huh? No.",
    "Nah.",
    "Naw.",
    "Not likely.",
    "No way, José.",
    "Not in a million years.",
    "Fat chance.",
    "Certainly not.",
    "NEGATORY.",
    "Nuh-uh.",
    "Not in my house!",
]

class Catify(commands.Cog):
    """Cog for the catify command."""
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(aliases=("ᓚᘏᗢify", "ᓚᘏᗢ"))
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def catify(self, ctx) -> None:
        """
        Convert the provided text into a cat themed sentence by interspercing cats throughout text.

        If no text is given then the users nickname is edited.
        """
        display_name = ctx.author.display_name

        if len(display_name) > 26:
            embed = Embed(
                title=random.choice(NEGATIVE_REPLIES),
                description=(
                    "Your display name is too long to be catified! "
                    "Please change it to be under 26 characters."
                ),
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            return
        else:
            display_name += f" | {random.choice(cats)}"

            await ctx.send(f"Your catified nickname is: `{display_name}`", allowed_mentions=AllowedMentions.none())
            await ctx.author.edit(nick=display_name)


def setup(bot) -> None:
    bot.add_cog(Catify(bot))
