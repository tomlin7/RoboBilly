"""
News Module
"""

import random
import json

import discord
from discord.ext import commands, tasks

from libs.httpsession import http_session
from libs import config


FAILED_ALERTS = [
    "What the hell man, {0}",
    "Ayo {0}, what have you done idiot, news no workey!",
    "Sorry peeps, its because of that dumb {0}, no news today sadly.",
    "Everyone blame {0} for this 🏃🏻‍♂️",
    "Smhmhmhmh {0}, why news no workey ⁉",
    "You better fix news {0}, or imma come to yer house",
    "For god sake {0} will you ever fix news",
    "Yo {0}, looks like news not workin'",
    "Naw {0}, news is down",
    "Sorry everyone, no news today #blame{0}",
    "baka {0}, your news thing is not working again",
    "{0} can you please fix news.",
    "Looks like i need to visit {0} today, FIX NEWS YOU IDIOT!",
    "You better fix news {0}, or imma break yer cookie jar",
]

# TODO: remove api key, add it as a secret
NEWS_WORLD = f"https://api.nytimes.com/svc/topstories/v2/world.json?api-key={config.NYT_TOKEN}"

def base_embed():
    return discord.Embed(
        title=f"📰 Basement Daily",
        description="Hows it going everyone ☕ Here is your todays newspaper",
        color=discord.Color.dark_theme()
    )

color = False
debug = False

def rand(s, e, c):
    ns = []
    while True:
        if len(ns) > c:
            return ns
        n = (random.randint(s, e))
        if n not in ns:
            ns.append(n)

def bullet():
    global color
    color = not color
    if color:
        return '🔸'
    else:
        return '🔹'

class News(commands.Cog):
    """
    NYT News
    """
    def __init__(self, bot):
        self.bot = bot

        self.news.start()

    @tasks.loop(hours=24)
    async def news(self):
        """
        NYT News
        """
        await self.send_news()

    # @commands.command(name="news")
    async def send_news(self, ctx):
        # news channel not configured
        if config.news_channel is None:
            return

        # Fetch Data
        # ----
        async with http_session.get(url=NEWS_WORLD) as response:
            if response.status == 200:
                data = await response.json()
            else:
                print(f'Status code is not 200, it is {response.status}')
                if debug:
                    err = discord.Embed(
                        title="ERROR",
                        color=Color.dark_theme()
                    )
                    await config.news_channel.send(embed=err)
                return

        # Data Extraction
        # ----
        num_results = int(data['num_results'])
        results = data['results']
        selected = rand(0, num_results - 1, 5)
        date = data['last_updated'][:10]

        if debug:
            print(f"Number of results: {num_results}\nSelected: {selected}")

        # Prepare Embed
        # ----
        embed = base_embed()
        for selection in selected:
            result = results[selection]
            title = result['title']
            des = result['abstract']
            if debug:
                print(f"length: {len(des)}")
            embed.add_field(name=f"{bullet()} {title}", value=f" {des} " if len(des) < 200 else f" {des}... ", inline=False)

        embed.set_footer(text=data['copyright'])

        try:
            await config.news_channel.send(f"☕ __**{date}**__")
            await config.news_channel.send(embed=embed)
        except Exception as e:
            if debug:
                bad = discord.Embed(
                    title="BAD",
                    description=e,
                    color=discord.Color.dark_theme()
                )
                await config.news_channel.send(embed=bad)
            print(e)

            # embed = Embed(
            #     title="News Failure",
            #     description=f"```py\n{e}\n```",
            #     color=discord.Color.dark_theme()
            # )
            # await ctx.send(embed=embed)
            await config.news_channel.send(f"{random.choice(FAILED_ALERTS).format(config.owner.mention)}")

def setup(bot):
	bot.add_cog(News(bot))
