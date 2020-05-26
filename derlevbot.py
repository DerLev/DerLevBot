import discord
import time
from discord.ext import commands

TOKEN = open("TOKEN", "r").read()

client = commands.Bot(command_prefix = 'dlb!')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="startup..."), status='dnd')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------------------')
    time.sleep(1)
    await client.change_presence(activity=discord.Streaming(name=" ", url='https://twitch.tv/derlev'))
    print('Status set to "Streaming"')
    # await client.get_user(377103974081495042).send(':red_square::orange_square::yellow_square::green_square:   **Ready**   :green_square::yellow_square::orange_square::red_square:')

# If a command gives an error, do nothing
@client.event
async def on_command_error(ctx, error):
    pass


# Command to set the Status of the bot to "Watching ..."
@client.command()
async def watching(ctx, *, status):
    if ctx.author.id == 377103974081495042:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status), status='online')
        await ctx.send(f'Status changed to `Watching {status}`')
        print(f'Status set to "Watching {status}"')
    else:
        await ctx.send('Only <@377103974081495042> can use this command')

@watching.error
async def watching_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        if ctx.author.id == 377103974081495042:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="DerLev [Official]"), status='online')
            await ctx.send(f'Status changed to `Watching DerLev [Official]`')
            print(f'Status set to "Watching DerLev [Official]"')
        else:
            await ctx.send('Only <@377103974081495042> can use this command')

# Command to set the Status of the bot to "Listening to ..."
@client.command()
async def listening(ctx, *, status):
    if ctx.author.id == 377103974081495042:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=status), status='online')
        await ctx.send(f'Status changed to `Listening to {status}`')
        print(f'Status set to "Listening to {status}"')
    else:
        await ctx.send('Only <@377103974081495042> can use this command')

@listening.error
async def listening_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        if ctx.author.id == 377103974081495042:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="DerLev"), status='online')
            await ctx.send(f'Status changed to `Listening to DerLev`')
            print(f'Status set to "Listening to DerLev"')
        else:
            await ctx.send('Only <@377103974081495042> can use this command')

# Command to set the Status of the bot to "Streaming ..."
@client.command()
async def streaming(ctx, *, status):
    if ctx.author.id == 377103974081495042:
        await client.change_presence(activity=discord.Streaming(name=status, url='https://twitch.tv/derlev'))
        await ctx.send(f'Status changed to `Streaming {status}`')
        print(f'Status set to "Streaming {status}"')
    else:
        await ctx.send('Only <@377103974081495042> can use this command')

@streaming.error
async def streaming_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        if ctx.author.id == 377103974081495042:
            await client.change_presence(activity=discord.Streaming(name=" ", url='https://twitch.tv/derlev'))
            await ctx.send(f'Status changed to `Streaming`')
            print(f'Status set to "Streaming"')
        else:
            await ctx.send('Only <@377103974081495042> can use this command')

# Command to set the Status of the bot to "Playing ..."
@client.command()
async def playing(ctx, *, status):
    if ctx.author.id == 377103974081495042:
        await client.change_presence(activity=discord.Game(name=status))
        await ctx.send(f'Status changed to `Playing {status}`')
        print(f'Status set to "Playing {status}"')
    else:
        await ctx.send('Only <@377103974081495042> can use this command')

@playing.error
async def playing_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        if ctx.author.id == 377103974081495042:
            await client.change_presence(activity=discord.Game(name=" "))
            await ctx.send(f'Status changed to `Playing`')
            print(f'Status set to "Playing"')
        else:
            await ctx.send('Only <@377103974081495042> can use this command')


client.run(TOKEN)
