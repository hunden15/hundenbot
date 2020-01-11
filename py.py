import discord
import os


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
    await client.send_message(message.channel, "제작자: 헌덴(HUNDEN)\n[도움말]\n1. s! -> 스넷봇의 정보를 확인합니다.\n2. s!info <유저닉네임> -> 유저의 정보를 확인합니다.")
    
    
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
