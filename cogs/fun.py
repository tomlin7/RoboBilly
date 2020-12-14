# contributors : Hex
import discord
from discord import member
from discord.ext import commands
import random
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
import asyncio

links = [
    "http://yeahlemons.com/",
    "http://imaninja.com/",
    "http://thatsthefinger.com/",
    "http://corndogoncorndog.com/",
    "http://iloveyoulikeafatladylovesapples.com/",
    "http://corndog.io/",
    "http://burnie.com/",
    "http://www.wutdafuk.com/",
    "http://www.infinitething.com/",
    "http://www.muchbetterthanthis.com/",
    "http://www.theendofreason.com/",
    "http://tunnelsnakes.com/",
    "http://www.coloursquares.com/",
    "http://crouton.net/",
    "http://eelslap.com/",
    "http://whitetrash.nl/",
    "http://metaphorsofinfinity.com/",
    "http://www.yesnoif.com/",
    "http://www.electricboogiewoogie.com/",
    "http://www.partridgegetslucky.com/",
    "http://buildshruggie.com/",
    "http://isitwednesdaymydudes.ml/",
    "http://heeeeeeeey.com/",
    "http://iamawesome.com/",
    "http://pixelsfighting.com/",
]

emoji_list = {
    "a": ":regional_indicator_a:",
    "b": ":regional_indicator_b:",
    "c": ":regional_indicator_c:",
    "d": ":regional_indicator_d:",
    "e": ":regional_indicator_e:",
    "f": ":regional_indicator_f:",
    "g": ":regional_indicator_g:",
    "h": ":regional_indicator_h:",
    "i": ":regional_indicator_i:",
    "j": ":regional_indicator_j:",
    "k": ":regional_indicator_k:",
    "l": ":regional_indicator_l:",
    "m": ":regional_indicator_m:",
    "n": ":regional_indicator_n:",
    "o": ":regional_indicator_o:",
    "p": ":regional_indicator_p:",
    "q": ":regional_indicator_q:",
    "r": ":regional_indicator_r:",
    "s": ":regional_indicator_s:",
    "t": ":regional_indicator_t:",
    "u": ":regional_indicator_u:",
    "v": ":regional_indicator_v:",
    "w": ":regional_indicator_w:",
    "x": ":regional_indicator_x:",
    "y": ":regional_indicator_y:",
    "z": ":regional_indicator_z:",
    "0": ":zero",
    "1": ":one:",
    "2": ":two:",
    "3": ":three:",
    "4": ":four:",
    "5": ":five:",
    "6": ":six:",
    "7": ":seven:",
    "8": ":eight:",
    "9": ":nine:",
    "_": " ",
}

logins = [
    "**Login:**\n**Email:** `starryhead@liar.com`\n**Password:** `passwot?`",
    "**Login:**\n**Email:** `blackismokes.com`\nPassword: `yeeehaaww`",
    "**Login:**\nEmail:** `ihateapplesxD@hotmail.com`\n**Password:** `pennydumb`",
    "**Login:**\n**Email:** `rooftopboi2@tired.com`\n**Password:** `lmao`",
    "**Login:**\n**Email:** `spicyhub69@flowervase.com`\n**Password:** `xyzk`",
    "**Login:**\n**Email:** `420Forbidden@NaN.com`\n**Password:** `NULL`",
    "**Login:**\n**Email:** `YourMom@exe.in`\n**Password:** `2 + 2 = 5`",
]

dms = [
    "Yeah she was your mom",
    "i love ~~you~~ washing machines",
    "man im tired",
    "tf was that bro",
    "i am 9 years old",
    "Wanna play Forknight?",
    "i just robbed my neighbour lmao",
    "do u like street lights?",
]

words = ["lmao", "potato", "no u", "MOM", "its small", "i like it"]

letters = ["e", "f", "s"]

ips = [
    "62.143.94.122",
    "37.111.208.88",
    "127.195.193.63",
    "172.249.219.149",
    "39.250.60.34",
    "191.184.2.171",
    "143.79.65.170",
    "17.36.141.6",
    "234.10.203.70",
    "115.107.247.111",
]

cursive = {
    "a": "𝓪",
    "b": "𝓫",
    "c": "𝓬",
    "d": "𝓭",
    "e": "𝓮",
    "f": "𝓯",
    "g": "𝓰",
    "h": "𝓱",
    "i": "𝓲",
    "j": "𝓳",
    "k": "𝓴",
    "l": "𝓵",
    "m": "𝓶",
    "n": "𝓷",
    "o": "𝓸",
    "p": "𝓹",
    "q": "𝓺",
    "r": "𝓻",
    "s": "𝓼",
    "t": "𝓽",
    "u": "𝓾",
    "v": "𝓿",
    "w": "𝔀",
    "x": "𝔁",
    "y": "𝔂",
    "z": "𝔃",
    "_": " ",
}

emo2 = {
    "a": "🄰",
    "b": "🄱",
    "c": "🄲",
    "d": "🄳",
    "e": "🄴",
    "f": "🄵",
    "g": "🄶",
    "h": "🄷",
    "i": "🄸",
    "j": "🄹",
    "k": "🄺",
    "l": "🄻",
    "m": "🄼",
    "n": "🄽",
    "o": "🄾",
    "p": "🄿",
    "q": "🅀",
    "r": "🅁",
    "s": "🅂",
    "t": "🅃",
    "u": "🅄",
    "v": "🅅",
    "w": "🅆",
    "x": "🅇",
    "y": "🅈",
    "z": "🅉",
    "_": " ",
}


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['8ball', '8 ball'])
    async def _8ball(self, ctx, *, que=None):
        if que is None:
            await ctx.send("What should i answer, dumbo")
            return

        choices = ["not looking good bud sorry to say",
                   "for sure", "my magics doesnt work at the moment", "100%", "ummmm not so sure",
                   "NO", "100% no", "i wish i could change it but my magics says no", "yes you are right",
                   "my reply is no", "i can tell you certainly, no", "sure, I literally couldn't care less",
                   " no???", "yes!!!!", " im not sure but ur def stupid", " i can tell you certainly, no",
                   "sure, I literally", "sure, why not", "can you not", "Is trump's skin orange?", "yes",
                   "when you grow a braincell, yes", "that would be a hell no", " hell to the yes",
                   "sure, why not", "yes, idiot"]

        await ctx.send(f":8ball:{random.choice(choices)}")

    # SIMP RATE
    # noinspection SpellCheckingInspection
    @commands.command(name="simprate", aliases=["Simprate"])
    async def simp_rate(self, ctx, _member: discord.Member = None):
        if _member is None:
            _member = ctx.message.author

        value = random.randint(0, 100)
        em = discord.Embed(
            title="SimpRate Machine",
            description=f"{_member.name} is {value} Simp.",
        )

        await ctx.send(embed=em)

    # GOOGLE
    @commands.command(name="google")
    async def google(self, ctx, *, q):
        await ctx.send(f"http://letmegooglethat.com/?q={q}".replace(" ", "+"))

    # GREEN TEXT
    # noinspection SpellCheckingInspection
    @commands.command(name="greentext", aliases=["Greentext"])
    async def green_text(self, ctx, *, text):
        await ctx.send(f"```css\n{text}\n```")

    # noinspection SpellCheckingInspection
    @commands.command()
    async def uselessweb(self, ctx):
        await ctx.send(f"{random.choice(links)}")

    # noinspection SpellCheckingInspection
    @commands.command(name="emojify")
    async def _emojify(self, ctx, msg):
        word = []
        for i in str(msg).lower():
            try:
                word.append(emoji_list[i])
            except KeyError:
                pass
        space = " "
        message = space.join(word)
        await ctx.send(message)

    # noinspection SpellCheckingInspection
    @commands.command(name="epicgamerrate", aliases=["egamerrate", "egr", "egrate"])
    async def epic_gamer_rate(self, ctx, _member: discord.Member = None):
        if _member is None:
            _member = ctx.message.author
            em = discord.Embed(
                title="EpicGamerRate Machine",
                description=f"You are {random.randint(0, 100)}% Epic Gamer 😎",
            )

            await ctx.send(embed=em)
        else:
            em = discord.Embed(
                title="EpicGamerRate Machine",
                description=f"{_member.nick} is {random.randint(0, 100)}% Epic Gamer 😎",
            )

            await ctx.send(embed=em)

    @commands.command(name="clap")
    async def clap(self, ctx, *, clap):
        await ctx.send(f"{clap}".replace(" ", "👏"))

    @commands.command(name="lenny")
    async def lenny(self, ctx):
        await ctx.send("( ͡° ͜ʖ ͡°)")

    @commands.command()
    async def imagine(self, ctx, *, ima):
        em = discord.Embed(title=f"{ima}")
        em.set_footer(text=f"{ctx.author.name} is trying really hard to imagine.")
        await ctx.send(embed=em)

    # noinspection SpellCheckingInspection
    @commands.command()
    async def hack(self, ctx, _member: discord.Member = None):
        if _member is None:
            await ctx.send("ok you did hack smthn, now mention someone else")
            return
        message = await ctx.send(f"Hacking {_member.name} now...")
        await asyncio.sleep(2)
        await message.edit(content="[▘]Getting Discord Login..(2FA bypassed)")
        await asyncio.sleep(2)
        await message.edit(content=f"[▖]**Found:**\n{random.choice(logins)}")
        await asyncio.sleep(2)
        await message.edit(
            content="[▝]Fetching DM's with closest friends(if there are any friends at all)"
        )
        await asyncio.sleep(2)
        await message.edit(content=f"[▗]**Last DM:** {random.choice(dms)}")
        await asyncio.sleep(2)
        await message.edit(content="[▖]Finding most common word...")
        await asyncio.sleep(2)
        await message.edit(content=f"[▘]**most used word:** {random.choice(words)}")
        await asyncio.sleep(2)
        await message.edit(
            content=f"[▝]**constantly used letter:** {random.choice(letters)}"
        )
        await asyncio.sleep(2)
        await message.edit(
            content=f"[▗]Injecting Trojan Virus into Discriminator #{_member.discriminator}"
        )
        await asyncio.sleep(2)
        await message.edit(
            content=f"[▝]Virus Injected, Emotes Stolen<a:dance:775321551205302292>"
        )
        await asyncio.sleep(2)
        await message.edit(content=f"[▖]Setting up Epic Store Account..")
        await asyncio.sleep(2)
        await message.edit(content=f"[▘]Hacking Epic Store Account..")
        await asyncio.sleep(2)
        await message.edit(
            content=f"[▗]Uninstalling **Fortnight**...<a:party:775459336091598879>"
        )
        await asyncio.sleep(2)
        await message.edit(content=f"[▖]Finding IP Address..")
        await asyncio.sleep(2)
        await message.edit(content=f"[▗]**IP Address:** {random.choice(ips)}")
        await asyncio.sleep(2)
        await message.edit(content=f"[▘]Selling Data to Government..")
        await asyncio.sleep(2)
        await message.edit(content=f"[▗]Reporting Account to Discord for breaking TOS..")
        await asyncio.sleep(2)
        await message.edit(content=f"[▘]Collecting Medical Records..")
        await asyncio.sleep(2)
        await message.edit(content=f"Finished hacking {_member.nick} \n"
                                   "The totally real and dangerous hack is complete...\n"
                                   "Now You Go To Jail.")

    @commands.command()
    async def kill(self, ctx, _member: discord.Member):
        deaths = [
            f"{ctx.message.author}"[:-5] + f" shoots {_member.name} in the head.",
            f"{_member.name} dies due to Depression.",
            f"{ctx.message.author}"[:-5]
            + f" drags {_member.name}'s ears too hard and rips them off.",
            f"{ctx.message.author}"[:-5]
            + f" killed {_member.name} by ripping the skin off of their face and making a mask out of it.",
            f"{ctx.message.author}"[:-5] + f" ripped {_member.name}'s Heart.",
            f"{ctx.message.author}"[:-5] + f" Alt+F4'd {_member.name}.exe!",
            f"{ctx.message.author}"[:-5] + f" swallowed {_member.name}.",
        ]

        if _member == ctx.message.author:
            await ctx.send("Ok you killed yourself, now mention someone else...")
        else:
            await ctx.send(f"{random.choice(deaths)}")

    @commands.command()
    async def cursive(self, ctx, msg):
        word = []
        for i in str(msg).lower():
            try:
                word.append(cursive[i])
            except KeyError:
                pass
        space = ""
        message = space.join(word)
        await ctx.send(message)

    # noinspection SpellCheckingInspection
    @commands.command()
    async def emojify2(self, ctx, msg):
        word = []
        for i in str(msg).lower():
            try:
                word.append(emo2[i])
            except KeyError:
                pass
        space = ""
        message = space.join(word)
        await ctx.send(message)

    @commands.command(aliases=['OwO'])
    async def owo(self, ctx):
        await ctx.send("OwO")


def setup(bot):
    bot.add_cog(Fun(bot))
