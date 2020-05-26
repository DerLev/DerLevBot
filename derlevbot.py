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
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
        await ctx.send(f'<:online:714858054683721818> Status changed to `Watching {status}`', delete_after=3)
        await discord.Message.delete(ctx.message)
        print(f'Status set to "Watching {status}"')
    else:
        await ctx.send('Only <@377103974081495042> can use this command')

@watching.error
async def watching_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        if ctx.author.id == 377103974081495042:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="DerLev [Official]"))
            await ctx.send(f'<:online:714858054683721818> Status changed to `Watching DerLev [Official]`', delete_after=3)
            await discord.Message.delete(ctx.message)
            print(f'Status set to "Watching DerLev [Official]"')
        else:
            await ctx.send('Only <@377103974081495042> can use this command')

# Command to set the Status of the bot to "Listening to ..."
@client.command()
async def listening(ctx, *, status):
    if ctx.author.id == 377103974081495042:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=status))
        await ctx.send(f'<:online:714858054683721818> Status changed to `Listening to {status}`', delete_after=3)
        await discord.Message.delete(ctx.message)
        print(f'Status set to "Listening to {status}"')
    else:
        await ctx.send('Only <@377103974081495042> can use this command')

@listening.error
async def listening_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        if ctx.author.id == 377103974081495042:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="DerLev"))
            await ctx.send(f'<:online:714858054683721818> Status changed to `Listening to DerLev`', delete_after=3)
            await discord.Message.delete(ctx.message)
            print(f'Status set to "Listening to DerLev"')
        else:
            await ctx.send('Only <@377103974081495042> can use this command')

# Command to set the Status of the bot to "Streaming ..."
@client.command()
async def streaming(ctx, *, status):
    if ctx.author.id == 377103974081495042:
        await client.change_presence(activity=discord.Streaming(name=status, url='https://twitch.tv/derlev'))
        await ctx.send(f'<:streaming:714859437382434887> Status changed to `Streaming {status}`', delete_after=3)
        await discord.Message.delete(ctx.message)
        print(f'Status set to "Streaming {status}"')
    else:
        await ctx.send('Only <@377103974081495042> can use this command')

@streaming.error
async def streaming_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        if ctx.author.id == 377103974081495042:
            await client.change_presence(activity=discord.Streaming(name=" ", url='https://twitch.tv/derlev'))
            await ctx.send(f'<:streaming:714859437382434887> Status changed to `Streaming`', delete_after=3)
            await discord.Message.delete(ctx.message)
            print(f'Status set to "Streaming"')
        else:
            await ctx.send('Only <@377103974081495042> can use this command')

# Command to set the Status of the bot to "Playing ..."
@client.command()
async def playing(ctx, *, status):
    if ctx.author.id == 377103974081495042:
        await client.change_presence(activity=discord.Game(name=status))
        await ctx.send(f'<:online:714858054683721818> Status changed to `Playing {status}`', delete_after=3)
        await discord.Message.delete(ctx.message)
        print(f'Status set to "Playing {status}"')
    else:
        await ctx.send('Only <@377103974081495042> can use this command')

@playing.error
async def playing_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        if ctx.author.id == 377103974081495042:
            await client.change_presence(activity=discord.Game(name=" "))
            await ctx.send(f'<:online:714858054683721818> Status changed to `Playing`', delete_after=3)
            await discord.Message.delete(ctx.message)
            print(f'Status set to "Playing"')
        else:
            await ctx.send('Only <@377103974081495042> can use this command')

# Command to set the Status of the bot to Online
@client.command()
async def online(ctx):
    if ctx.author.id == 377103974081495042:
        await client.change_presence(activity=discord.CustomActivity(name=""), status=discord.Status.online)
        await ctx.send(f'<:online:714858054683721818> Status changed to **Online**', delete_after=3)
        await discord.Message.delete(ctx.message)
        print(f'Status set to Online')
    else:
        await ctx.send('Only <@377103974081495042> can use this command')

# Command to set the Status of the bot to Idle
@client.command()
async def idle(ctx):
    if ctx.author.id == 377103974081495042:
        await client.change_presence(activity=discord.CustomActivity(name=""), status=discord.Status.idle)
        await ctx.send(f'<:idle:714859559054999635> Status changed to **Idle**', delete_after=3)
        await discord.Message.delete(ctx.message)
        print(f'Status set to Idle')
    else:
        await ctx.send('Only <@377103974081495042> can use this command')

# Command to set the Status of the bot to DnD
@client.command()
async def dnd(ctx):
    if ctx.author.id == 377103974081495042:
        await client.change_presence(activity=discord.CustomActivity(name=""), status=discord.Status.dnd)
        await ctx.send(f'<:dnd:714859559574831235> Status changed to **DnD**', delete_after=3)
        await discord.Message.delete(ctx.message)
        print(f'Status set to DnD')
    else:
        await ctx.send('Only <@377103974081495042> can use this command')


client.run(TOKEN)
