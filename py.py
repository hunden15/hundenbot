import discord
import os
import datetime
import json


client = discord.Client()


@client.event
async def on_ready():
  print("login")
  print(client.user.name)
  print(client.user.id)
  print("------------------")
  await client.change_presence(game=discord.Game(name='', type=1))

@client.event
async def on_member_join(member):
  with open('users.json', 'r') as f:
    users = json.load(f)
  
  await update_data(users, member)
  
  with open('users.json', 'w') as f:
    json.dump(users, f)

async def update_data(users, user):
  if not user.id in users:
    users[user.id] = {}
    users[user.id]['experience'] = 0
    users[user.id]['level'] = 1

async def add_experience(users, user, exp):
  users[user.id]['experience'] += exp

async def level_up(users, user, channel):
  experience = users[user.id]['experience']
  lvl_start = users[user.id]['level']
  lvl_end = int(experience ** (1/4))
  
  if lvl_start < lvl_end:
    await client.send_message(channel, '{} has leveled up to level {}'.format(user.mention, lvl_end))
    users[user.id]['level'] = lvl_end

@client.event
async def on_message(message):
  SN = "`[스넷봇 시스템]"
  with open('users.json', 'r') as f:
    users = json.load(f)
  
  await update_data(users, message.author)
  await add_experience(users, message.author, 5)
  await level_up(users, message.author, message.channel)
  
  with open('users.json', 'w') as f:
    json.dump(users, f)
    
  if message.content == "=":
    await client.send_message(message.channel, SN + " 기본 명령어: =help`")
  else:
    if message.content[1:5] == "help":
      embed = discord.Embed(color=0x0028ff)
      embed.add_field(name="[스넷봇 도움말 시스템]", value="=help :: 도움말 확인을 합니다.\n=info :: 나의 정보를 확인합니다.\n=contact :: 제작자에게 문의를 합니다.[봇 갠디코로만 가능]", inline=True)
      await client.send_message(message.channel, embed=embed)
    if message.content[1:3] == "dm":
      if message.author.id == "419810897058463754":
        member = discord.utils.get(client.get_all_members(), id=message.content[3:19])
        await client.send_message(member, SN + " 제작자 : " + message.content[20:] + "`")
      else:
        await client.send_message(message.channel, SN + " " + message.author.name + "님 당신은 이 명령어를 사용할 권한이 없습니다.`")
    if message.content[1:8] == "contact":
      if message.content[8:]:
        if message.channel.is_private and message.author.id != "665768509707518033":
          await client.send_message(discord.utils.get(client.get_all_members(), id="419810897058463754"), message.author.name + "(" + message.author.id + ") : " + message.content[8:])
      else:
        await client.send_message(message.channel, SN + " 제작자에게 문의 보낼 메세지를 적어주세요.`")
    if message.content[1:6] == "":
      
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
