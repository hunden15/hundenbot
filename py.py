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

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f'Kicked {member.mention}')

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.send(f' Banned (member.mention}')

@client.command()
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')
  
  for ban_entry in banned_users:
    user = ban_entry.user
    
    if (user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      await ctx.send(f' Unbanned {user.mention}')
      return



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
