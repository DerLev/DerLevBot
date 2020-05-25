# Work with Python 3.6
import discord
from discord.ext import commands

TOKEN = open("TOKEN", "r").read()

client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="to startup..."), status='dnd')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------------------')
    await client.change_presence(activity=discord.Streaming(name=" ", url='https://twitch.tv/derlev'))
    print('Status set to "Streaming"')
    # await client.get_user(377103974081495042).send(':red_square::orange_square::yellow_square::green_square:   **Ready**   :green_square::yellow_square::orange_square::red_square:')


client.run(TOKEN)
