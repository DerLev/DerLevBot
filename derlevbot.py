import discord
import time
import json
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure

with open("config.json", "r") as f:
    config = json.load(f)

TOKEN = config["token"]
ownerid = config["owner_id"]
prefix = config["prefix"]
twitch = config["twitch"]


client = commands.Bot(command_prefix = f'{prefix}')
client.remove_command('help')


print('==========================')
print('Project: DerLevBot')
print('Author: DerLev')
print('==========================')
print('Contacting Discord...')

@client.event
async def on_ready():
  print('Connection established.')
  print('==========================')
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="startup..."), status=discord.Status.dnd)
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('==========================')
  time.sleep(1)
  await client.change_presence(activity=discord.Streaming(name="dlb!help", url=f'{twitch}'))
  print(f'Status set')


# If a command gives an error
@client.event
async def on_command_error(ctx, error):
  await discord.Message.delete(ctx.message)
  e = discord.Embed(color=discord.Color.from_rgb(250, 166, 26))
  e.title = "Hmm... somthing went wrong."
  e.description = f"`{error}`"
  await ctx.send(embed=e, delete_after=10)


# Ping command
@client.command(aliases=['p'])
async def ping(ctx):
  #await ctx.send('Pong! {0}'.format(round(bot.latency, 1))
  e = discord.Embed(color=discord.Color.from_rgb(83, 50, 138))
  e.title = "Pong :ping_pong:"
  e.add_field(
      name="Latency:",
      value="{0}ms".format(round((client.latency * 1000), 1))
  )
  await ctx.send(embed=e, delete_after=10)
  await discord.Message.delete(ctx.message)

# Help Command
@client.command(aliases=['?'])
async def help(ctx):
  await discord.Message.delete(ctx.message)
  e = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
  e.title = ":question: Help :question:"
  e.add_field(
    name = f" ·  `{prefix}vote <messageid>`",
    value = "Reacts with <:yes:715189455199404092> and <:no:715189454775779389> to a given message for voting"
  )
  e.add_field(
    name = f" ·  `{prefix}invite`",
    value = "Get the bot's invite-link\n***Aliases:*** *inv*"
  )
  e.add_field(
    name = f" ·  `{prefix}createinvite <channelmention>`",
    value = "Create an infinite invite to a specific channel\n***Aliases:*** *creinv*"
  )
  e.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url_as(size=128))
  await ctx.send(embed=e, delete_after=30)

# Invite command
@client.command(aliases=['inv'])
async def invite(ctx):
  await discord.Message.delete(ctx.message)
  e = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
  e.title = ":mailbox_with_mail: Invite :mailbox_with_mail:"
  t = "Click here to invite me to your server"
  l = f"https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=519240&scope=bot"
  e.description = "**[{}]({})**".format(t, l)
  await ctx.channel.trigger_typing()
  time.sleep(1)
  await ctx.send(embed=e, delete_after=10)

# Command to see who the Boss is 😉
@client.command(aliases=['wib'])
async def whoistheboss(ctx):
  await discord.Message.delete(ctx.message)
  e = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
  e.description = f"The Boss is <@{ownerid}>"
  await ctx.send(embed=e, delete_after=5)

# Command to let the Bot react to a message for Votes
@client.command()
async def vote(ctx, msg):
  await discord.Message.delete(ctx.message)
  vote = await ctx.channel.fetch_message(msg)
  await discord.Message.add_reaction(vote, emoji="yes:715189455199404092")
  await discord.Message.add_reaction(vote, emoji="no:715189454775779389")

# Create Invite command
@client.command(aliases=['creinv'])
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
  e.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url_as(size=128))
  await ctx.channel.trigger_typing()
  time.sleep(1)
  await ctx.send(embed=e)


client.run(TOKEN)
