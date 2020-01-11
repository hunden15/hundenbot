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
  if message.content.startswith("!도움말"):
    await client.send_message(message.channel, "[도움말]\n!도움말 = 스넷봇 도움말을 확인합니다.\n\n[ 문의는 디스코드봇 1대1채팅으로 해주세요. ]")
  if message.content.startswith("닥쳐"):
    await client.send_message(message.channel, "욕하지마!!!!")
  if message.channel.is_private and message.author.id != "665460521050439710":
    await client.send_message(discord.utils.get(client.get_all_members(), id="419810897058463754"), message.author.name + "(" + message.author.id + ") : " + message.content)
  if message.content.startswith("!DM"):
    if message.author.id == "419810897058463754":
      member = discord.utils.get(client.get_all_members(), id=message.content[4:22])
      await client.send_message(member, "[스넷봇] 제작자 답변 : " + message.content[23:])
    else:
      await client.send_message(message.channel, "[스넷봇] 당신은 이 명령어를 사용할 권한이 없습니다."
    
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
