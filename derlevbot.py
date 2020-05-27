import discord
import time
from discord.ext import commands

TOKEN = open("TOKEN", "r").read()

client = commands.Bot(command_prefix = 'dlb!')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="startup..."), status=discord.Status.dnd)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------------------')
    time.sleep(1)
    await client.change_presence(activity=discord.Streaming(name=" ", url='https://twitch.tv/derlev'))
    print('Status set to "Streaming"')
    # await client.get_user(377103974081495042).send(':red_square::orange_square::yellow_square::green_square:   **Ready**   :green_square::yellow_square::orange_square::red_square:')

# If a command gives an error, do nothing
#@client.event
#async def on_command_error(ctx, error):
#    pass


# Command to set the Status of the bot to "Watching ..."
@client.command()
async def watching(ctx, *, status):
    if ctx.author.id == 377103974081495042:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
        e = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
        e.description = f"<:online:714858054683721818> Status changed to `Watching {status}`"
        # await ctx.send(f'<:online:714858054683721818> Status changed to `Watching {status}`', delete_after=3)
        await discord.Message.delete(ctx.message)
        await ctx.send(embed=e, delete_after=3)
        print(f'Status set to "Watching {status}"')
    else:
        await ctx.send('Only <@377103974081495042> can use this command')

@watching.error
async def watching_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        if ctx.author.id == 377103974081495042:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="DerLev [Official]"))
            e = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
            e.description = "<:online:714858054683721818> Status changed to `Watching Derlev [Official]`"
            # await ctx.send(f'<:online:714858054683721818> Status changed to `Watching DerLev [Official]`', delete_after=3)
            await discord.Message.delete(ctx.message)
            await ctx.send(embed=e, delete_after=3)
            print(f'Status set to "Watching DerLev [Official]"')
        else:
            await ctx.send('Only <@377103974081495042> can use this command')

# Command to set the Status of the bot to "Listening to ..."
@client.command()
async def listening(ctx, *, status):
    if ctx.author.id == 377103974081495042:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=status))
        e = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
        e.description = f"<:online:714858054683721818> Status changed to `Listening to {status}`"
        # await ctx.send(f'<:online:714858054683721818> Status changed to `Listening to {status}`', delete_after=3)
        await discord.Message.delete(ctx.message)
        await ctx.send(embed=e, delete_after=5)
        print(f'Status set to "Listening to {status}"')
    else:
        await ctx.send('Only <@377103974081495042> can use this command')

@listening.error
async def listening_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        if ctx.author.id == 377103974081495042:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="DerLev"))
            e = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
            e.description = "<:online:714858054683721818> Status changed to `Listening to DerLev`"
            # await ctx.send(f'<:online:714858054683721818> Status changed to `Listening to DerLev`', delete_after=3)
            await discord.Message.delete(ctx.message)
            await ctx.send(embed=e, delete_after=5)
            print(f'Status set to "Listening to DerLev"')
        else:
            await ctx.send('Only <@377103974081495042> can use this command')

# Command to set the Status of the bot to "Streaming ..."
@client.command()
async def streaming(ctx, *, status):
    if ctx.author.id == 377103974081495042:
        await client.change_presence(activity=discord.Streaming(name=status, url='https://twitch.tv/derlev'))
        e = discord.Embed(color=discord.Color.from_rgb(187, 91, 224))
        e.description = f"<:streaming:714859437382434887> Status changed to `Streaming {status}`"
        # await ctx.send(f'<:streaming:714859437382434887> Status changed to `Streaming {status}`', delete_after=3)
        await discord.Message.delete(ctx.message)
        await ctx.send(embed=e, delete_after=5)
        print(f'Status set to "Streaming {status}"')
    else:
        await ctx.send('Only <@377103974081495042> can use this command')

@streaming.error
async def streaming_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        if ctx.author.id == 377103974081495042:
            await client.change_presence(activity=discord.Streaming(name=" ", url='https://twitch.tv/derlev'))
            e = discord.Embed(color=discord.Color.from_rgb(187, 91, 224))
            e.description = "<:streaming:714859437382434887> Status changed to `Streaming`"
            # await ctx.send(f'<:streaming:714859437382434887> Status changed to `Streaming`', delete_after=3)
            await discord.Message.delete(ctx.message)
            await ctx.send(embed=e, delete_after=5)
            print(f'Status set to "Streaming"')
        else:
            await ctx.send('Only <@377103974081495042> can use this command')

# Command to set the Status of the bot to "Playing ..."
@client.command()
async def playing(ctx, *, status):
    if ctx.author.id == 377103974081495042:
        await client.change_presence(activity=discord.Game(name=status))
        e = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
        e.description = f"<:online:714858054683721818> Status changed to `Playing {status}`"
        # await ctx.send(f'<:online:714858054683721818> Status changed to `Playing {status}`', delete_after=3)
        await discord.Message.delete(ctx.message)
        await ctx.send(embed=e, delete_after=5)
        print(f'Status set to "Playing {status}"')
    else:
        await ctx.send('Only <@377103974081495042> can use this command')

@playing.error
async def playing_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        if ctx.author.id == 377103974081495042:
            await client.change_presence(activity=discord.Game(name=" "))
            e = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
            e.description = "<:online:714858054683721818> Status changed to `Playing`"
            # await ctx.send(f'<:online:714858054683721818> Status changed to `Playing`', delete_after=3)
            await discord.Message.delete(ctx.message)
            await ctx.send(embed=e, delete_after=5)
            print(f'Status set to "Playing"')
        else:
            await ctx.send('Only <@377103974081495042> can use this command')

# Command to set the Status of the bot to Online
@client.command()
async def online(ctx):
    if ctx.author.id == 377103974081495042:
        await client.change_presence(activity=discord.CustomActivity(name=""), status=discord.Status.online)
        e = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
        e.description = "<:online:714858054683721818> Status changed to `Online`"
        # await ctx.send(f'<:online:714858054683721818> Status changed to **Online**', delete_after=3)
        await discord.Message.delete(ctx.message)
        await ctx.send(embed=e, delete_after=5)
        print(f'Status set to Online')
    else:
        await ctx.send('Only <@377103974081495042> can use this command')

# Command to set the Status of the bot to Idle
@client.command()
async def idle(ctx):
    if ctx.author.id == 377103974081495042:
        await client.change_presence(activity=discord.CustomActivity(name=""), status=discord.Status.idle)
        e = discord.Embed(color=discord.Color.from_rgb(250, 166, 26))
        e.description = "<:idle:714859559054999635> Status changed to `Idle`"
        # await ctx.send(f'<:idle:714859559054999635> Status changed to **Idle**', delete_after=3)
        await discord.Message.delete(ctx.message)
        await ctx.send(embed=e, delete_after=5)
        print(f'Status set to Idle')
    else:
        await ctx.send('Only <@377103974081495042> can use this command')

# Command to set the Status of the bot to DnD
@client.command()
async def dnd(ctx):
    if ctx.author.id == 377103974081495042:
        await client.change_presence(activity=discord.CustomActivity(name=""), status=discord.Status.dnd)
        e = discord.Embed(color=discord.Color.from_rgb(240, 71, 71))
        e.description = "<:dnd:714859559574831235> Status changed to `DnD`"
        # await ctx.send(f'<:dnd:714859559574831235> Status changed to **DnD**', delete_after=3)
        await discord.Message.delete(ctx.message)
        await ctx.send(embed=e, delete_after=5)
        print(f'Status set to DnD')
    else:
        await ctx.send('Only <@377103974081495042> can use this command')

# Command to let the Bot react to a message for Votes
@client.command()
async def vote(ctx, msg):
    await discord.Message.delete(ctx.message)
    vote = await ctx.channel.fetch_message(msg)
    await discord.Message.add_reaction(vote, emoji="yes:715189455199404092")
    await discord.Message.add_reaction(vote, emoji="no:715189454775779389")

@vote.error
async def vote_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await discord.Message.delete(ctx.message)
        e = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
        e.title = "<:yes:715189455199404092> Vote <:no:715189454775779389>"
        e.description = "For me to react with the Emotes,\nyou need to give me the message id."
        await ctx.send(embed=e, delete_after=10)

client.run(TOKEN)
