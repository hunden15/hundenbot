import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '=')

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
@client.command()
async def mute(ctx, member : discord.Member):
  guild = ctx.guild
  
  for role in guild.roles:
    if role.name == "Muted":
      await member.add_roles(role)
      await ctx.send("{} has {} has been muted" .format(member.mention,ctx.author.mention))
      return
    
      overwrite = discord.PermissionsOverwrite(send_messages=False)
      newRole = await guild.create_role(name="Muted")
      
      for channel in guild.text_channels:
        await channel.set_permissions(newRole,overwrite=overwrite)
        
      await member.add_roles(newRole)
      await ctx.send("{} has {} has been muted" .format(member.mention,ctx.author.mention))
      
      
@client.command()
async def unmute(ctx, member : discord.Member):
  guild = ctx.guild
  
  for role in guild.roles:
    if role.name == "Muted":
      await member.remove_roles(role)
      await ctx.send("{} has {} has been unmuted" .format(member.mention,ctx.author.mention))
      return



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
