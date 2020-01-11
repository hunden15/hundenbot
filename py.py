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
  if message.content.startswith("!정보"):
    await client.send_message(message.channel, "[도움말]\n!도움말 = 스넷봇 도움말을 확인합니다.")
    
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
