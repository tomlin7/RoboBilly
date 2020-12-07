import discord
import asyncio
from discord.ext import commands
import json

# emoji reference : 🇦 🇧 🇨 🇩 🇪 🇫 🇬 🇭 🇮 🇯 🇰 🇱 🇲 🇳 🇴 🇵 🇶 🇷 🇸 🇹 🇺 🇻 🇼 🇽 🇾 🇿 
# these aren't letters, but emojis 😉

emojis = {
    "a": "🇦",
    "b": "🇧",
    "c":"🇨",
    "d":"🇩",
    "e":"🇪",
    "f":"🇫",
    "g":"🇬",
    "h":"🇭",
    "i":"🇮",
    "j":"🇯",
    "k":"🇰",
    "l":"🇱",
    "m":"🇲",
    "n":"🇳",
    "o":"🇴",
    "p":"🇵",
    "q":"🇶",
    "r":"🇷",
    "s":"🇸",
    "t":"🇹",
    "u":"🇺",
    "v":"🇻",
    "w":"🇼",
    "x":"🇽",
    "y":"🇾",
    "z":"🇿"
}

class emojify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="emojify", aliases=["Emojify", "emify"])
    async def _emojify(self, ctx, *, text):
        emoji_text = []
        for i in text.lower():
            emoji_text.append(emojis[i])
        space = " "
        message = space.join(emoji_text)
        await ctx.send(message)
        
        


def setup(bot):
	bot.add_cog(emojify(bot))