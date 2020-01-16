import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '&')

@client.event
async def on_ready():
  print('Online')

@client.command()
@commands.has_permission(manage_messages=True)
async def clear(ctx, amount=3):
  await ctx.channel.purge(limit=amount)



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
