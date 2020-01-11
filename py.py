import discord
import os
import datatime


client = discord.Client()


@client.event
async def on_ready():
  print("login")
  print(client.user.name)
  print(client.user.id)
  print("------------------")
  await client.change_presence(game=discord.Game(name='', type=1))

@client.event
async def on_message(message):
  if message.content.startswith("!정보"):
    data = datatime.datatime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
    embed = discord.Embed(color=0x00ff00)
    embed.addfield(name="이름", value=message.author.name, inline=True)
    embed.addfield(name="서버닉네임", value=message.author.display_name, inline=True)
    embed.addfield(name="가입일", value=str(data.year) + "년" + str(data.month) + "월" + str(data.day) + "일", inline=True)
    embed.addfield(name="아이디", value=message.author.id, inline=True)
    embed.set_thumbnail(url=message.author.avatar_url)
    await client.send_message(message.channel, embed=embed)
    
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
