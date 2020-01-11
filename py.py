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
    await client.send_message(message.channel, "[도움말]\n!도움말 = 스넷봇 도움말을 확인합니다.")
  if message.content.startswith("닥쳐"):
    await client.send_message(message.channel, "욕하지마!!!!")
  if message.channel.is_private and message.author != "665460521050439710":
    await client.send_message(discord.utils.get(client.get_all_members(), id="419810897058463754"), message.author.name + "(" + message.author.id + ") : " + message.content)
  if message.content.startswith("!DM"):
    member = discord.utils.get(client.get_all_members(), id=message.content[4:22])
    await client.send_message(member, "[스넷봇] 제작자 답변 : " + message.content[23:1])
  if message.content.startswith("!뮤트"):
    author = message.guild.get_member(int(message.content[4:22]))
    role = discord.utils.get(message.guild.roles, name="뮤트")
    await author.add_roles(role)
    await client.send_message(message.channel, "[스넷봇 뮤트 시스템] (" + message.author.name + ") 님이 (" + author + ") 의 아이디를 뮤트시켰습니다."
  if message.content.startswith("!언뮤트"):
    author = message.guild.get_member(int(message.content[5:23]))
    role = discord.utils.get(message.guild.roles, name="뮤트")
    await author.remove_roles(role)
                              await client.send_message(message.channel, "[스넷봇 뮤트 시스템] (" + message.author.name + ") 님이 (" + author + ") 의 아이디를 뮤트를 해제시켰습니다."
    
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
