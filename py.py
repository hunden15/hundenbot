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
  if message.content.startswith("s!"):
    await client.send_message(message.channel, "'''안녕하세요.\n스넷봇 제작자 헌덴입니다.\n스넷봇은 현재 베타입니다.\n스넷봇을 사용해주셔서 감사드립니다.\n\nMade by. HUNDEN#1422\n\n스넷봇 도움말:\n1. s! -> 스넷봇 도움말을 확인합니다.\n2. s!정보 <유저닉네임> -> <유저닉네임>의 정보를 확인합니다.```")
  if message.content.startswith("s!정보"):
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
