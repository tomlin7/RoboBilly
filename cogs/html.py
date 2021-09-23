import discord
from discord.ext import commands
import imgkit


class Html(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group(name="html")
    async def html(self, ctx):
        pass
    
    @commands.command(name="html", aliases=["html_to_img"])
    async def html(self, *, code):
        with open("html_img.html", "w") as f:
            f.write(str(code))

        options = {
            'format': 'png'
        }
        imgkit.from_file('html_img.html', 'out.png', options=options)

        await ctx.send(file=discord.File("out.png"))

    @commands.command(name="url_to_img", aliases=["url_img"])
    async def url_to_img(self, url):
        options = {
            'format': 'png',
            'encoding': "UTF-8",
        }
        imgkit.from_url(str(url), 'out.png', options=options)
        await ctx.send(file=discord.File("out.png"))
        
        
def setup(bot):
    bot.add_cog(Html(bot))
