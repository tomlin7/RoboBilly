"""
Anime module
"""

import discord
import asyncio

from discord.ext import commands
from mal import *

class AnimeList(commands.Cog):
    """
    Anime module
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def anime(self, ctx, *, arg):
        try:  
            await ctx.trigger_typing()        
            
            search = AnimeSearch(arg)
            result = search.results[0]
            id = search.results[0].mal_id
            anime = Anime(str(id))

            em = discord.Embed(title = f"{result.title} ({anime.title_japanese})", url = result.url, description = f"{result.synopsis}", color = 14834431)
            em.add_field(name = "▬▬▬▬▬▬▬", value = "__**Information**__", inline = False)
            em.add_field(name = ":scroll: | Ratings", value = result.score)
            em.add_field(name = ":military_medal: | Ranking", value = anime.rank)
            em.add_field(name = ":film_frames: | Episodes", value = result.episodes)
            em.add_field(name = ":flags: | Aired", value = anime.aired)
            em.add_field(name = ":ribbon: | Status", value = anime.status, inline = True)
            em.add_field(name = ":clipboard: | Rating", value = anime.rating, inline = True)
            em.add_field(name = ":clock1: | Broadcast", value = anime.broadcast)
            em.add_field(name=  ":eyeglasses: | Source", value = anime.source, inline = True)
            em.add_field(name =  ":classical_building: | Studios", value = anime.studios[0], inline = True)
            em.set_thumbnail(url = result.image_url)
            em.set_footer(text = f"{anime.premiered} • {result.type}")
            await ctx.send(embed = em)    
        except Exception as e:
            embed = discord.Embed(description = e, color = discord.Color.dark_theme())
            await ctx.send(embed = embed)
        
def setup(bot):
	bot.add_cog(AnimeList(bot))
