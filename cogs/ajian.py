from discord.ext import commands
import discord
import random


def find_in_message(content, target):
    info = ""
    for x in content:
        if x[0:len(target)] == target:
            info = x[len(target) + 1:]
    return info


def colour(_random=False):
    if _random:
        return random.randint(0x100000, 0xFFFFFF)
    else:
        return 55807


class Ajian(commands.Cog):
    """
    Commands related to the bot.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def ajian(self, ctx):
        """
        >.<
        """
        if ctx.invoked_subcommand is None:
            await ctx.send("no u")

    @ajian.command()
    async def bonk(self, ctx):
        if random.choice([True, False]):
            await ctx.send(f"*bonks ajian {('like hell wtf', '**gently**')[bool(random.randint(0, 10) == 5)]}*")
        else:
            await ctx.send("You got bonked by ajian, get got!")

    @ajian.command()
    async def hug(self, ctx):
        await ctx.send("*ajian hugs back*  🤍")

    @ajian.command()
    async def owo(self, ctx):
        await ctx.send("UwU")

    @ajian.command()
    async def embed(self, ctx, *args):
        await ctx.message.delete()
        args = list(args)
        title = find_in_message(args, "title")
        description = find_in_message(args, "description")
        try:
            _embed_colour = int(find_in_message(args, "colour"))
        except ValueError:
            _embed_colour = colour()
        if ctx.message.attachments:
            image_url = ctx.message.attachments[0].url
        else:
            image_url = find_in_message(args, "image_url")

        final = discord.Embed(
            title=title,
            description=description,
            colour=_embed_colour
        )
        final.set_image(url=image_url)
        final.set_footer(text=f"Submitted by <@{ctx.message.author.id}>")

        await ctx.send(embed=final)


def setup(bot):
    bot.add_cog(Ajian(bot))
