import discord
import time
from discord.ext import commands

TOKEN = open("TOKEN", "r").read()

client = commands.Bot(command_prefix = 'dlb!')
client.remove_command('help')


ownerid = 377103974081495042


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="startup..."), status=discord.Status.dnd)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------------------')
    time.sleep(1)
    await client.change_presence(activity=discord.Streaming(name="dlb!help", url='https://twitch.tv/derlev'))
    print('Status set to "Streaming dlb!help"')

# If a command gives an error, do nothing
#@client.event
#async def on_command_error(ctx, error):
#    pass


# Command to see who the Boss is 😉
@client.command()
async def whoistheboss(ctx):
    await discord.Message.delete(ctx.message)
    e = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
    e.description = f"The Boss is <@{ownerid}>"
    await ctx.send(embed=e, delete_after=5)

# Help Command
@client.command()
async def help(ctx):
    await discord.Message.delete(ctx.message)
    e = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
    e.title = ":question: Help :question:"
    e.add_field(
        name=" ·  `dlb!vote <messageid>`",
        value="Reacts with <:yes:715189455199404092> and <:no:715189454775779389> to a given message for voting"
    )
    e.add_field(
        name=" ·  `dlb!vote2 <messageid>`",
        value="Reacts with 👍 and 👎 to a given message for voting"
    )
    e.add_field(
        name=" ·  `dlb!invite`",
        value="Get the bot's invite-link"
    )
    e.add_field(
        name=" ·  `dlb!createinvite <channelmention>`",
        value="Create an infinite invite to a specific channel"
    )
    e.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.guild.get_member(ctx.author.id).avatar_url_as(size=128))
    await ctx.send(embed=e)

# Invite command
@client.command()
async def invite(ctx):
    await discord.Message.delete(ctx.message)
    e = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
    e.title = ":mailbox_with_mail: Invite :mailbox_with_mail:"
    t = "Click here to invite me to your server"
    l = f"https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot"
    e.description = "**[{}]({})**".format(t, l)
    await ctx.channel.trigger_typing()
    time.sleep(1)
    await ctx.send(embed=e, delete_after=10)

# Command to set the Status of the bot to "Watching ..."
@client.command()
async def watching(ctx, *, status):
    if ctx.author.id == ownerid:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
        e = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
        e.description = f"<:online:714858054683721818> Status changed to `Watching {status}`"
        await discord.Message.delete(ctx.message)
        await ctx.send(embed=e, delete_after=5)
        print(f'Status set to "Watching {status}"')
    else:
        await discord.Message.delete(ctx.message)
        await ctx.send(f'Only <@{ownerid}> can use this command', delete_after=3)

@watching.error
async def watching_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        if ctx.author.id == ownerid:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="dlb!help"))
            e = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
            e.description = "<:online:714858054683721818> Status changed to `Watching dlb!help`"
            await discord.Message.delete(ctx.message)
            await ctx.send(embed=e, delete_after=5)
            print(f'Status set to "Watching dlb!help"')
        else:
            await discord.Message.delete(ctx.message)
            await ctx.send(f'Only <@{ownerid}> can use this command', delete_after=3)

# Command to set the Status of the bot to "Listening to ..."
@client.command()
async def listening(ctx, *, status):
    if ctx.author.id == ownerid:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=status))
        e = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
        e.description = f"<:online:714858054683721818> Status changed to `Listening to {status}`"
        await discord.Message.delete(ctx.message)
        await ctx.send(embed=e, delete_after=5)
        print(f'Status set to "Listening to {status}"')
    else:
        await discord.Message.delete(ctx.message)
        await ctx.send(f'Only <@{ownerid}> can use this command', delete_after=3)

@listening.error
async def listening_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        if ctx.author.id == ownerid:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="dlb!help"))
            e = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
            e.description = "<:online:714858054683721818> Status changed to `Listening to dlb!help`"
            await discord.Message.delete(ctx.message)
            await ctx.send(embed=e, delete_after=5)
            print(f'Status set to "Listening to dlb!help"')
        else:
            await discord.Message.delete(ctx.message)
            await ctx.send(f'Only <@{ownerid}> can use this command', delete_after=3)

# Command to set the Status of the bot to "Streaming ..."
@client.command()
async def streaming(ctx, *, status):
    if ctx.author.id == ownerid:
        await client.change_presence(activity=discord.Streaming(name=status, url='https://twitch.tv/derlev'))
        e = discord.Embed(color=discord.Color.from_rgb(187, 91, 224))
        e.description = f"<:streaming:714859437382434887> Status changed to `Streaming {status}`"
        await discord.Message.delete(ctx.message)
        await ctx.send(embed=e, delete_after=5)
        print(f'Status set to "Streaming {status}"')
    else:
        await discord.Message.delete(ctx.message)
        await ctx.send(f'Only <@{ownerid}> can use this command', delete_after=3)

@streaming.error
async def streaming_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        if ctx.author.id == ownerid:
            await client.change_presence(activity=discord.Streaming(name="dlb!help", url='https://twitch.tv/derlev'))
            e = discord.Embed(color=discord.Color.from_rgb(187, 91, 224))
            e.description = "<:streaming:714859437382434887> Status changed to `Streaming dlb!help`"
            await discord.Message.delete(ctx.message)
            await ctx.send(embed=e, delete_after=5)
            print(f'Status set to "Streaming dlb!help"')
        else:
            await discord.Message.delete(ctx.message)
            await ctx.send(f'Only <@{ownerid}> can use this command', delete_after=3)

# Command to set the Status of the bot to "Playing ..."
@client.command()
async def playing(ctx, *, status):
    if ctx.author.id == ownerid:
        await client.change_presence(activity=discord.Game(name=status))
        e = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
        e.description = f"<:online:714858054683721818> Status changed to `Playing {status}`"
        await discord.Message.delete(ctx.message)
        await ctx.send(embed=e, delete_after=5)
        print(f'Status set to "Playing {status}"')
    else:
        await discord.Message.delete(ctx.message)
        await ctx.send(f'Only <@{ownerid}> can use this command', delete_after=3)

@playing.error
async def playing_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        if ctx.author.id == ownerid:
            await client.change_presence(activity=discord.Game(name="dlb!help"))
            e = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
            e.description = "<:online:714858054683721818> Status changed to `Playing dlb!help`"
            await discord.Message.delete(ctx.message)
            await ctx.send(embed=e, delete_after=5)
            print(f'Status set to "Playing dlb!help"')
        else:
            await discord.Message.delete(ctx.message)
            await ctx.send(f'Only <@{ownerid}> can use this command', delete_after=3)

# Command to set the Status of the bot to Online
@client.command()
async def online(ctx):
    if ctx.author.id == ownerid:
        await client.change_presence(activity=discord.CustomActivity(name=""), status=discord.Status.online)
        e = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
        e.description = "<:online:714858054683721818> Status changed to `Online`"
        await discord.Message.delete(ctx.message)
        await ctx.send(embed=e, delete_after=5)
        print(f'Status set to Online')
    else:
        await discord.Message.delete(ctx.message)
        await ctx.send(f'Only <@{ownerid}> can use this command', delete_after=3)

# Command to set the Status of the bot to Idle
@client.command()
async def idle(ctx):
    if ctx.author.id == ownerid:
        await client.change_presence(activity=discord.CustomActivity(name=""), status=discord.Status.idle)
        e = discord.Embed(color=discord.Color.from_rgb(250, 166, 26))
        e.description = "<:idle:714859559054999635> Status changed to `Idle`"
        await discord.Message.delete(ctx.message)
        await ctx.send(embed=e, delete_after=5)
        print(f'Status set to Idle')
    else:
        await discord.Message.delete(ctx.message)
        await ctx.send(f'Only <@{ownerid}> can use this command', delete_after=3)

# Command to set the Status of the bot to DnD
@client.command()
async def dnd(ctx):
    if ctx.author.id == ownerid:
        await client.change_presence(activity=discord.CustomActivity(name=""), status=discord.Status.dnd)
        e = discord.Embed(color=discord.Color.from_rgb(240, 71, 71))
        e.description = "<:dnd:714859559574831235> Status changed to `DnD`"
        await discord.Message.delete(ctx.message)
        await ctx.send(embed=e, delete_after=5)
        print(f'Status set to DnD')
    else:
        await discord.Message.delete(ctx.message)
        await ctx.send(f'Only <@{ownerid}> can use this command', delete_after=3)

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
        e.description = "You need to give me a Message ID"
        await ctx.send(embed=e, delete_after=10)

# Command to let the Bot react to a message for Votes
@client.command()
async def vote2(ctx, msg):
    await discord.Message.delete(ctx.message)
    vote = await ctx.channel.fetch_message(msg)
    await discord.Message.add_reaction(vote, emoji="👍")
    await discord.Message.add_reaction(vote, emoji="👎")

@vote2.error
async def vote2_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await discord.Message.delete(ctx.message)
        e = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
        e.title = "👍 Vote 👎"
        e.description = "You need to give me a Message ID"
        await ctx.send(embed=e, delete_after=10)

# Command for "DerLev [Official]"
@client.command()
async def noti(ctx, user: discord.Member, type):
    await discord.Message.delete(ctx.message)
    if ctx.author.id == ownerid:
        if type == "vip":
            channel = await user.create_dm()
            e = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
            e.title = "VIP-Status"
            e.description = f"Hallo {user.mention}.\n\nLeider müssen wir dir mitteilen, dass dein VIP-Status entfernt wurde,\nweil du zu lange inaktiv warst.\n\n~ {client.user.mention}"
            e.set_footer(text=f"Gesendet von {ctx.author}", icon_url=ctx.guild.get_member(ctx.author.id).avatar_url_as(size=128))
            await channel.send(embed=e)
            e2 = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
            e2.title = f":incoming_envelope: Sent to {user} :incoming_envelope:"
            await ctx.send(embed=e2, delete_after=10)
        if type == "mod":
            channel = await user.create_dm()
            e = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
            e.title = "Mod-Status"
            e.description = f"Hallo {user.mention}.\n\nLeider müssen wir dir mitteilen, dass deine Moderations-Rechte entfernt wurden,\nweil du zu lange inaktiv warst.\nDu kannst {ctx.author.mention} anschreiben, falls dies\nein Missverständnis war.\n\n~ {client.user.mention}"
            e.set_footer(text=f"Gesendet von {ctx.author}", icon_url=ctx.guild.get_member(ctx.author.id).avatar_url_as(size=128))
            await channel.send(embed=e)
            e2 = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
            e2.title = f":incoming_envelope: Sent to {user} :incoming_envelope:"
            await ctx.send(embed=e2, delete_after=10)
        if type == "admin":
            channel = await user.create_dm()
            e = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
            e.title = "Admin-Status"
            e.description = f"Hallo {user.mention}.\n\nLeider müssen wir dir mitteilen,\ndass deine Administrations-Rechte entfernt wurden,\nweil du zu lange inaktiv warst.\nDu kannst {ctx.author.mention} anschreiben, falls dies\nein Missverständnis war.\n\n~ {client.user.mention}"
            e.set_footer(text=f"Gesendet von {ctx.author}", icon_url=ctx.guild.get_member(ctx.author.id).avatar_url_as(size=128))
            await channel.send(embed=e)
            e2 = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
            e2.title = f":incoming_envelope: Sent to {user} :incoming_envelope:"
            await ctx.send(embed=e2, delete_after=10)

@noti.error
async def noti_error(ctx, error):
    await discord.Message.delete(ctx.message)

# Create Invite command
@client.command()
async def createinvite(ctx, channel: discord.TextChannel):
    await discord.Message.delete(ctx.message)
    invite = await channel.create_invite(reason=f"Command used by {ctx.author}")
    e = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
    e.title = ":mailbox: Channel-Invite created :mailbox:"
    t = f"{invite}"
    l = f"{invite}"
    text = (
        f"Channel: <#{channel.id}>\n"
        "Invite: **[{}]({})**".format(t, l)
    )
    e.add_field(name="Invite details:", value=text)
    e.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.guild.get_member(ctx.author.id).avatar_url_as(size=128))
    await ctx.channel.trigger_typing()
    time.sleep(1)
    await ctx.send(embed=e)

@createinvite.error
async def createinvite_error(ctx, error):
    await discord.Message.delete(ctx.message)

client.run(TOKEN)
