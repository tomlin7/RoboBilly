"""
the main economy-management file.
"""
import discord
from discord.ext import commands
from discord.ext.commands import Bot, BucketType

from .economy import fn as fn
from .economy.emoji import setup_emojis
from .economy.data import sync_data

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        sync_data()


    @commands.command(name="top", aliases=['leaderboard', 'rich'])
    async def leaderboard(self, ctx):
        """
        shows the leaderboard based on amount of wallet money.
        """
        await fn.leaderboard(ctx=ctx)


    # noinspection SpellCheckingInspection
    @commands.command(name="work")
    @commands.cooldown(1, 3600, BucketType.user)
    async def work(self, ctx):
        """
        The main work category
        """
        await fn.work(ctx=ctx)


    # noinspection SpellCheckingInspection
    @commands.command(name="worklist", aliases=["jobs", "work_list"])
    async def work_list(self, ctx):
        """
        shows the list of available jobs and their respected salary
        """
        await fn.work_list(ctx)


    @commands.command(name="apply", aliases=['workas', 'apply for', 'workapply', 'join', 'work_as', 'work_apply'])
    async def apply(self, ctx, *, job=None):
        """
        apply for a job, which is in work list.
        :param ctx:
        :param job:
        """
        await fn.apply(ctx, job)


    @commands.command(name="beg", aliases=["Beg"])
    async def beg(self, ctx):
        """
        check for donations.
        """
        await fn.beg(ctx=ctx)


    @commands.command(name="balance", aliases=['bal', 'Balance'])
    async def balance(self, ctx, _member: discord.Member = None):
        """
        check the balance of the specified user, or the context author.
        :param _member:
        """
        await fn.balance(ctx=ctx, _member=_member)


    @work.error
    async def work_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            cool_down_message = "You need to wait **1 hour** until you can work again!"
            await ctx.send(cool_down_message)
        else:
            pass


    @commands.command(name="steal", aliases=["rob", "Rob", "Steal"])
    async def steal(self, ctx, _member: discord.Member = None):
        """
        steal from other users.
        :param _member:
        :param ctx:
        """
        await fn.steal(ctx, _member)


    # TODO: make deposit command
    # TODO: make withdraw
    @commands.command(name="deposit", aliases=["dep", "Dep", "Deposit"])
    async def deposit(self, ctx, amount: int = None, part: str = None):
        """
        deposit money to bank account.
        :param ctx:
        :param amount:
        :param part:
        """
        await fn.deposit(ctx=ctx)

def setup(bot):
	bot.add_cog(Economy(bot))

