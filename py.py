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
async def on_message(message):
  SN = "`[스넷봇 시스템]"
    
  if message.content == "=":
    await client.send_message(message.channel, SN + " 기본 명령어: =help`")
  else:
    if message.content[1:5] == "help":
      embed = discord.Embed(color=0x0028ff)
      embed.add_field(name="[스넷봇 도움말 시스템]", value="=help :: 도움말 확인을 합니다.\n=info :: 나의 정보를 확인합니다.\n=contact :: 제작자에게 문의를 합니다.[봇 갠디코로만 가능]\n안녕 스넷봇 :: 스넷봇에게 말을 걸어보세요!\n=server :: 스넷봇서버의 상태를 알려줍니다.", inline=True)
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
    if message.content[1:7] == "server":
      serverf = "Online"
      servert = "Online"
      await client.send_message(message.channel, SN + "\n서버1 :: " + serverf + "\n서버2 :: " + servert + "`")
  if message.content == "안녕 스넷봇":
    if message.author.id == "419810897058463754":
      await client.send_message(message.channel, "안녕하세요! 스넷봇 총개발자 헌덴님!")
    else:
      if message.author.id == "421291279939403788":
        await client.send_message(message.channel, "안녕하세요! 유튜버 후야님!")
      if message.author.id == "545485943415635969":
        await client.send_message(message.channel, "안녕하세요! 유튜버 초루하르시님!")
      if message.author.id == "400509470003953664":
        await client.send_message(message.channel, "안녕하세요! 유튜버 카울님!")
      if message.author.id == "377423308628557825":
        await client.send_message(message.channel, "안녕하세요! 유튜버 침대종현님!")
      if message.author.id == "409699052456771606":
        await client.send_message(message.channel, "안녕하세요! 유튜버 후돌이프론님!")
      if message.author.id == "505609869772980234":
        await client.send_message(message.channel, "안녕하세요! 유튜버 YEOMDDA님!")
      if message.author.id == "618778311291830292":
        await client.send_message(message.channel, "안녕하세요! 부개발자 큐브님!")
      else:
        await client.send_message(message.channel, "안녕하세요! " + message.author.name + "님!")
      
      
      
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
