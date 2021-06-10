###### USER MODULE ######
import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, BadArgument
import requests, json
from datetime import timedelta, datetime
import pyfiglet
class user(commands.Cog):
    api_key = "bbde6a19c33fb4c3962e36b8187abbf8"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    def __init__(self, bot):
        self.bot = bot
    
    def get_embed(self, _title, _description, icon):
        embed = discord.Embed(title=_title, description=_description, color= 0xF39C12) #,color=#F39C12
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
        print("Event. said: ", arg, ", puppy repeated: ", ctx.author.name)


    @commands.command()
    async def hi(self, ctx):
        async with ctx.channel.typing():
            thing = "hello human!"
        await (ctx.channel).send(thing)
        print("Event. I said Hi to  ", ctx.author.name)


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
        await ctx.send(embed=self.get_embed(f"Weather status at {a}", msg, "https://i.pinimg.com/564x/77/0b/80/770b805d5c99c7931366c2e84e88f251.jpg"))
        print("Event. weather checked on user's command: ", ctx.author.name, ", location: ", a)


    @commands.command()
    async def bing(self, ctx):
        async with ctx.channel.typing():
            thing = discord.Embed(title="Bong!", description="Sounds like something " + "https://www.bing.com/"+" would know!", color= 0xF39C12)
        await (ctx.channel).send(embed=thing)
        print("Event. I binged, bong! :  ", ctx.author.name)


    @commands.command()
    async def dontasktoask(self, ctx):
        async with ctx.channel.typing():
            thing = discord.Embed(title="Don't ask to ask, Just ask!", description="Ask your question, instead of asking to help \nhttps://dontasktoask.com/", color= 0xF39C12)
        await (ctx.channel).send(embed = thing)
        print("Event. ", ctx.author.name, " did ask to ask!")
    
    @commands.command(name='goodnight', aliases=['night', 'gn'])
    async def goodnight(self, ctx, *, args = "nothing"):
        async with ctx.channel.typing():
            thing = discord.Embed(title="Good Night", description="Sleep tight", color= discord.Color.blue())
        await (ctx.channel).send(embed=thing)
        print(f"Event. {ctx.author.name}  said good night")
    
    @commands.command(name='goodmorning', aliases=['morning', 'gm'])
    async def goodmorning(self, ctx, *, args = "nothing"):
        async with ctx.channel.typing():
            thing = discord.Embed(title="Good Morning", description="Wishing you a good day", color= discord.Color.blue())
        await (ctx.channel).send(embed=thing)
        print(f"Event. {ctx.author.name}  said good morning")
    
    @commands.group()
    async def git(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid git command passed...')

    @git.command()
    async def push(self, ctx, remote: str, branch: str):
        await ctx.send('Pushing {} to {}'.format(remote, branch))
	
    @git.command()
    async def blame(self, ctx, branch: str):
        await ctx.send('#blame{}'.format(branch))

    @commands.command(name='codeblocks', aliases=['codeblock', 'cb', 'paste', 'myst'])
    async def codeblocks(self, ctx, *, args = "nothing"):
        async with ctx.channel.typing():
            thing = discord.Embed(title="Code Blocks", description="Use codeblocks to send lengthy code, paste it into https://paste.myst.rs/ and send the link of the paste into chat.", color= discord.Color.blue())
        await (ctx.channel).send(embed=thing)
        print(f"Event. {ctx.author.name}  used code blocks")
    
    @commands.command(name='howcodeblocks', aliases=['howcb', 'hcb', 'howcodeblock'])
    async def howcodeblocks(self, ctx, *, args = "nothing"):
        async with ctx.channel.typing():
            thing = discord.Embed(title="How to use Code Blocks", description="> 1. paste your code into https://paste.myst.rs/\n> 2. copy the link of the website completely\n> 3. send the link into chat.", color= discord.Color.blue())
        await (ctx.channel).send(embed=thing)
        print(f"Event. {ctx.author.name}  used how to use code blocks, bruh")
    @commands.command(name='codeblocktriggers', aliases=['cbt', 'codeblocktrigger', 'codeblockstriggers', 'cbtrigger', 'cbtriggers'])
    async def codeblocktriggers(self, ctx, *, args='nothing'):
        async with ctx.channel.typing():
            thing = discord.Embed(title="How to use Code Blocks Triggers", description="> when making codeblocks, add your language name on the beginning.\njust like this - ````python` for python language", color= discord.Color.blue())
        await (ctx.channel).send(embed=thing)
        print(f"Event. {ctx.author.name}  used how to use code blocks, bruh")

    @commands.group(name="ascii")
    async def ascii(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.trigger_typing()
            embed = discord.Embed(title="Ascii Modules", description="use []ascii <module>", color = discord.Color.blue())
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
                embed = discord.Embed(color = discord.Color.blue())
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
	bot.add_cog(user(bot))
