import discord, os
from discord.ext import commands
import imgkit

# install wkhtmltopdf
os.system("sudo apt install wkhtmltopdf")


# config imgkit

# path_wkthmltoimage = "/app/wkhtmltoimage.exe"
# config = imgkit.config(wkhtmltoimage=path_wkthmltoimage)



class Html(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group(name="html")
    async def html(self, ctx):
        pass
    
    @html.command(name="html_to_img", aliases=["html", "-h", "--html"])
    async def html_to_img(self, *, code):
        with open("html_img.html", "w") as f:
            f.write(str(code))

        options = {
            'format': 'png'
        }
        imgkit.from_file('html_img.html', 'out.png', options=options) #, config=config)

        print("File created: out.png")
        await ctx.send(file=discord.File("out.png"))

    @html.command(name="url_to_img", aliases=["url", "-u", "--url"])
    async def url_to_img(self, url):
        options = {
            'format': 'png',
            'encoding': "UTF-8",
        }
        imgkit.from_url(str(url), 'out.png', options=options) #, config=config)

        print("File created: out.png")
        await ctx.send(file=discord.File("out.png"))
        
        
def setup(bot):
    bot.add_cog(Html(bot))
