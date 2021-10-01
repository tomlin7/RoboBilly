import discord, json, os

prefix = '[]'

owner = None
guild = None
news_channel = None
mails_channel = None

owner_id = 699589680408297553

guild_id = 750945243305869343
news_channel_name = '📰-basement-daily'
mails_channel_name = 'mails'

# environmental variables
NYT_TOKEN = os.getenv("NYT_TOKEN")
MONGO_URL = os.getenv("MONGO_URL")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

special_event = "Halloween"

def load_config(client):
    global guild, news_channel, mails_channel, guild_id, news_channel_name, mails_channel_name, owner, owner_id

    if guild_id is not None:
        guild = client.get_guild(guild_id)
        if guild is not None:
            for channel in guild.channels:
                if channel.name == news_channel_name:
                    news_channel = channel
                elif channel.name == mails_channel_name:
                    mails_channel = channel

    owner = guild.get_member(owner_id)