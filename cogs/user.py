"""
User module
"""

import discord
import random
import asyncio
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, BadArgument

import requests, json, pyfiglet
from datetime import timedelta, datetime


class User(commands.Cog):
    api_key = "bbde6a19c33fb4c3962e36b8187abbf8"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    def __init__(self, bot):
        self.bot = bot
    
    def get_embed(self, _title, _description, icon):
        embed = discord.Embed(title=_title, description=_description, color= discord.Color.dark_theme())
        embed.set_thumbnail(url=icon)
        return embed


    def get_weather(self, city_name):
        complete_url = self.base_url + "appid=" + self.api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()

        if x["cod"] != "404":
            # store the value of "main" 
            # key in variable y
            y = x["main"] 

            # store the value corresponding 
            # to the "temp" key of y 
            current_temperature = y["temp"] 

            # store the value corresponding 
            # to the "pressure" key of y 
            current_pressure = y["pressure"] 

            # store the value corresponding 
            # to the "humidity" key of y 
            current_humidiy = y["humidity"] 

            # store the value of "weather" 
            # key in variable z 
            z = x["weather"] 

            # store the value corresponding 
            # to the "description" key at 
            # the 0th index of z 
            weather_description = z[0]["description"] 

            # print following values 
            result = ("Temperature (in kelvin unit) = " + str(current_temperature) + "\natmospheric pressure (in hPa unit) = " + str(current_pressure) + "\nhumidity (in percentage) = " + str(current_humidiy) + "\ndescription = " + str(weather_description))
            return result
        else:
            print(" City Not Found : " + city_name)
            return "That city might be in moon"


    @commands.command()
    async def say(self, ctx, *, arg):
        async with ctx.channel.typing():
            thing = arg
        await (ctx.channel).send(thing)
        print("Event: Repeated {ctx.author.name}: ", arg)


    @commands.command()
    async def hi(self, ctx):
        async with ctx.channel.typing():
            thing = "hello human!"
        await (ctx.channel).send(thing)
        print("Event: I said Hi to ", ctx.author.name)


    @commands.command()
    async def info(self, ctx, *, member: discord.Member):
        async with ctx.channel.typing():
            await asyncio.sleep(2)
            avatar = member.avatar_url
            fmt = 'Joined basement on {0.joined_at} \njoined Discord on {0.created_at} \nThis member has {1} roles.'
            msg = self.get_embed("Info of {0.display_name}".format(member), fmt.format(member, len(member.roles)), avatar)
        await ctx.send(embed=msg)
        print(ctx.author.name, " checked info of ", member.name)


    @info.error
    async def info_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('I could not find that member...')


    @commands.command(pass_context=True)
    async def weather(self, ctx, a: str):
        async with ctx.channel.typing():
            msg = self.get_weather(a)
            await asyncio.sleep(2)
        await ctx.send(embed=discord.Embed(title=f"Weather status at {a}", description=msg, color=discord.Color.dark_theme()))
        print("Event. weather checked on user's command: ", ctx.author.name, ", location: ", a)


    @commands.command()
    async def bing(self, ctx):
        async with ctx.channel.typing():
            thing = discord.Embed(title="Bong!", description="Sounds like something " + "https://www.bing.com/"+" would know!", color=discord.Color.dark_theme())
        await (ctx.channel).send(embed=thing)
        print("Event. I binged, bong! :  ", ctx.author.name)
        
    @commands.command()
    async def google(self, ctx):
        await ctx.send("It is quite important that you **google your problems before asking** someone. Most of your questions have already been answered at least once online because you are definitely not the only one with this particular question. Additionally, each programming language, API, or program should be well documented in its official documentation. \nRefer to this page: https://duck-dev.github.io/general/how-to-google/")
        print("Event. how to google! :  ", ctx.author.name)


    @commands.command()
    async def dontasktoask(self, ctx):
        async with ctx.channel.typing():
            thing = discord.Embed(title="Don't ask to ask, Just ask!", description="Ask your question, instead of asking to help \nhttps://dontasktoask.com/", color=discord.Color.dark_theme())
        await (ctx.channel).send(embed = thing)
        print("Event. ", ctx.author.name, " did ask to ask!")
    
    @commands.command(name='goodnight', aliases=['night', 'gn'])
    async def goodnight(self, ctx, *, args = "nothing"):
        async with ctx.channel.typing():
            thing = discord.Embed(title="Good Night", description="Sleep tight", color= discord.Color.dark_theme())
        await (ctx.channel).send(embed=thing)
        print(f"Event. {ctx.author.name}  said good night")
    
    @commands.command(name='goodmorning', aliases=['morning', 'gm'])
    async def goodmorning(self, ctx, *, args = "nothing"):
        async with ctx.channel.typing():
            thing = discord.Embed(title="Good Morning", description="Wishing you a good day", color= discord.Color.dark_theme())
        await (ctx.channel).send(embed=thing)
        print(f"Event. {ctx.author.name}  said good morning")
    
    @commands.group()
    async def git(self, ctx):
        """
        A set of funny ~~useful~~ git commands.
        """
        if ctx.invoked_subcommand is None:
            await ctx.send('> See: `[]help git`')

    @git.command()
    async def push(self, ctx, remote: str, branch: str):
        await ctx.send('Pushing {} to {}'.format(remote, branch))
    
    @git.command()
    async def blame(self, ctx, branch: str):
        await ctx.send('#blame{}'.format(branch))

    @git.command()
    async def lick(self, ctx, user):
        if random.choice([True, False]):
            await ctx.send('*licks {}, Mmm tastes good*'.format(user))
        else:
            await ctx.send('*licks {}, euh tastes kinda bad*'.format(user))
    
    @git.command()
    async def commit(self, ctx, *, message: str):
        await ctx.send('Commiting {}'.format(message))

    @git.command()
    async def pull(self, ctx, branch: str):
        await ctx.send('Pulling {}'.format(branch))
    
    @git.command()
    async def status(self, ctx, user: discord.Member=None):
        if user:
            await ctx.send("On branch {0}\nYour branch is up to date with 'origin/main'. \nstatus: {1}".format(user.display_name, user.status))
        else:
            await ctx.send("On branch main\nYour branch is up to date with 'origin/main'. \nstatus: {}".format(ctx.author.status))

    @git.command()
    async def merge(self, ctx, thing, anotherthing):
        await ctx.send('Merging {0} to {1}'.format(thing, anotherthing))
    
    @git.command()
    async def add(self, ctx, *, thing):
        msg = await ctx.send('Adding {0}...'.format(thing))
        await asyncio.sleep(2)
        await msg.edit(content='Added {0} to changes.\n`{1} additions and {2} deletions.`'.format(thing, random.randint(10, 1000), random.randint(10, 1000)))
    
    @git.command()
    async def out(self, ctx, *, thing):
        await ctx.send('https://tenor.com/view/the-office-steve-carell-please-leave-get-out-move-gif-3579774')

    @commands.command(name='codeblocks', aliases=['codeblock', 'cb', 'myst'])
    async def codeblocks(self, ctx, *args):
        async with ctx.channel.typing():
            thing = discord.Embed(title="Code Blocks", description="""**__Use codeblocks to send code in a message!__**

To make a codeblock, surround your code with \`\`\`
\`\`\`cs
// your code here
\`\`\`

`In order use C# syntax highlighting add cs after the three back ticks`

To send lengthy code, paste it into <https://paste.myst.rs/> and send the link of the paste into chat.""", color=discord.Color.dark_theme())
        await (ctx.channel).send(embed=thing)
        print(f"Event: {ctx.author.name}  used codeblocks")
    
    @commands.command(name='example', aliases=['Example', 'eg', 'eg.'])
    async def example(self, ctx, *args):
        async with ctx.channel.typing():
            thing = discord.Embed(title="Example", description="""**__How to create a Minimal, Reproducible Example__**

When asking a question, people will be better able to provide help if you provide code that they can easily understand and use to reproduce the problem. This is referred to by community members as creating a minimal, reproducible example (**reprex**), a minimal, complete and verifiable example (**mcve**), or a minimal, workable example (**mwe**). Regardless of how it's communicated to you, it boils down to ensuring your code that reproduces the problem follows the following guidelines:

Your code examples should be…

• …Minimal – Use as little code as possible that still produces the same problem
• …Complete – Provide all parts someone else needs to reproduce your problem in the question itself
• …Reproducible – Test the code you're about to provide to make sure it reproduces the problem
""", color=discord.Color.dark_theme())
        await (ctx.channel).send(embed=thing)
        print(f"Event: {ctx.author.name}  used example")
    
    @commands.command(name='pastemyst', aliases=['pm', 'pastebin', 'PasteMyst', 'paste'])
    async def pastemyst(self, ctx, *, args = "nothing"):
        async with ctx.channel.typing():
            thing = discord.Embed(title="How to use PasteMyst", description="> 1. paste your code in https://paste.myst.rs/\n> 2. copy the link of the website completely\n> 3. send the link into chat.", color=discord.Color.dark_theme())
        await (ctx.channel).send(embed=thing)
        print(f"Event: {ctx.author.name}  used how to use pastemyst")

    @commands.group(name="ascii")
    async def ascii(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.trigger_typing()
            embed = discord.Embed(title="Ascii Modules", description="use []ascii <module>", color = discord.Color.dark_theme())
            embed.add_field(name="Word", value="Shows ascii art of given text.", inline=False)
            embed.add_field(name="Fonts", value="See available Fonts.", inline=False)
            embed.set_footer(text="use  []ascii <module> <args>")
            await ctx.send(embed=embed)


    @ascii.command(name="word", aliases=["w", "Word", "W"])
    async def word(self, ctx, word:str = "hey", font:str = "standard"):
        try:
            result = pyfiglet.figlet_format(word, font = font)
        except:
            result = f"There is no font called {font}."
        await ctx.send("```\n" + result + "\n```")

    @ascii.command(name="fonts", aliases=["font", "f"])
    async def fonts(self, ctx, page:int=1):
        total_pages = 4
        with open('./cogs/fonts.json', 'r') as f: 
            try:
                data = json.load(f)

                if page == 1:
                    page_data = data['fonts1']
                    page_no = 1
                elif page == 2:
                    page_data = data['fonts2']
                    page_no = 2
                elif page == 3:
                    page_data = data['fonts3']
                    page_no = 3
                elif page == 4:
                    page_data = data['fonts4']
                    page_no = 4
                elif page is None:
                    page_data = data['fonts1']
                    page_no = 1
                else:
                    page_data = "more fonts will be added in future"
                    page_no = 0
            except:
                print("fonts.json loading error")

            if page_data is not None:
                Separator = "\n"
                fields = Separator.join(page_data)

                #embeding
                embed = discord.Embed(color = discord.Color.dark_theme())
                embed.set_author(name='Ascii Art')
                embed.add_field(name='Fonts page', value=fields, inline=False)
                if page_no != 0:
                    embed.set_footer(text=f"page: {page_no}/{total_pages}")
                else:
                    embed.set_footer(text="use  []ascii fonts <page_no>")
                await ctx.send(embed=embed)
            else:
                print("looks like there's a problem with page_data")


#===================================== ADD COG ======================================#

def setup(bot):
    bot.add_cog(User(bot))
