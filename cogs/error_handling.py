import discord
from discord.ext import commands

import difflib, math

QUESTION_MARK_ICON = "https://cdn.discordapp.com/attachments/822420465250861096/893413947061964860/question.png"

class ErrorHandling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """Command error handler"""
        embed = discord.Embed(color=discord.Color.red())
        if isinstance(error, commands.CommandNotFound):
            await self.send_command_suggestion(ctx, ctx.invoked_with)
            return

        elif isinstance(error, commands.CommandOnCooldown):
            embed.title = "Whoops Cooldown!"
            embed.description = f"Command is on cooldown. Try again after {math.ceil(error.retry_after)} seconds!"
            await ctx.send(embed=embed)
        else:
            raise error
    
    async def send_command_suggestion(self, ctx: commands.Context, command_name: str) -> None:
        """Sends user similar commands if any can be found."""
        raw_commands = []
        for cmd in self.bot.walk_commands():
            if not cmd.hidden:
                raw_commands += (cmd.name, *cmd.aliases)
        if similar_command_data := difflib.get_close_matches(command_name, raw_commands, 1):
            similar_command_name = similar_command_data[0]
            similar_command = self.bot.get_command(similar_command_name)

            if not similar_command:
                return

            misspelled_content = ctx.message.content
            e = discord.Embed()
            e.set_author(name="Did you mean:", icon_url=QUESTION_MARK_ICON)
            e.description = misspelled_content.replace(command_name, similar_command_name, 1)
            await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(ErrorHandling(bot))
