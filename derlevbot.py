import discord
import time
import json
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

with open("config.json", "r") as f:
  config = json.load(f)

TOKEN = config["token"]
ownerid = config["owner_id"]
twitch = config["twitch"]


client = commands.Bot(command_prefix = "dlb!")
slash = SlashCommand(client, sync_commands=True)
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
  await client.change_presence(activity=discord.Streaming(name="slash commands", url=twitch))
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
@slash.slash(name="ping", description="Pings the bot")
async def _ping(ctx: SlashContext):
  e = discord.Embed(color=discord.Color.from_rgb(83, 50, 138))
  e.title = "Pong :ping_pong:"
  e.add_field(
    name="Latency:",
    value="{0}ms".format(round((client.latency * 1000), 1))
  )
  await ctx.send(embed=e, hidden=True)

# Invite command
@slash.slash(name="invite", description="Get the bot's invite link")
async def _invite(ctx: SlashContext):
  e = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
  e.title = ":mailbox_with_mail: Invite :mailbox_with_mail:"
  t = "Click here to invite me to your server"
  l = f"https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=519240&scope=bot%20applications.commands"
  e.description = "**[{}]({})**".format(t, l)
  await ctx.send(embed=e, hidden=True)

# Command to see who the Boss is 😉
@slash.slash(name="whoisboss", description="See who the bot owner is")
async def whoistheboss(ctx: SlashContext):
  e = discord.Embed(color=discord.Color.from_rgb(47, 49, 54))
  e.description = f"The Boss is <@{ownerid}>"
  await ctx.send(embed=e, hidden=True)

# Command to let the Bot react to a message for Votes
@slash.slash(
  name="vote",
  description="Reacts with voting emojis to a given message id",
  options=[
    create_option(
      name="msg",
      description="Message ID",
      required=True,
      option_type=3
    )
  ]
)
async def _vote(ctx: SlashContext, msg):
  vote = await ctx.channel.fetch_message(msg)
  await discord.Message.add_reaction(vote, emoji="yes:715189455199404092")
  await discord.Message.add_reaction(vote, emoji="no:715189454775779389")
  e = discord.Embed(color=discord.Color.from_rgb(47, 49, 54))
  e.description = ":white_check_mark: Done"
  await ctx.send(embed=e, hidden=True)

# Create Invite command
@slash.slash(
  name="createinvite",
  description="Create an infinite invite to a specific channel",
  options=[
    create_option(
      name="channel",
      description="Channel for invite",
      required=True,
      option_type=7
    )
  ]
)
async def _createinvite(ctx: SlashContext, channel: discord.TextChannel):
  invite = await channel.create_invite(reason=f"Command used by {ctx.author}", unique=True, max_age=60 * 60 * 24)
  e = discord.Embed(color=discord.Color.from_rgb(66, 177, 126))
  e.title = ":mailbox: Channel-Invite created :mailbox:"
  t = f"{invite}"
  l = f"{invite}"
  text = (
    f"Channel: <#{channel.id}>\n"
    "Invite: **[{}]({})**".format(t, l)
  )
  e.add_field(name="Invite details:", value=text)
  await ctx.send(embed=e, hidden=True)


client.run(TOKEN)
