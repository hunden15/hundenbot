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
  patners = []
    
  if message.content == "=":
    await client.send_message(message.channel, SN + " 기본 명령어: =help`")
  else:
    if message.content[1:5] == "help":
      await client.send_message(message.channel, "```[스넷봇 공식 시스템]\n=help :: 도움말 확인\n=contact :: 개발자에게 문의\n=server :: 서버 상태확인\n안녕 스넷봇 :: 스넷봇에게 인사\n\n공식 디스코드서버: https://discord.gg/QwGfSuj```")
    if message.content[1:3] == "dm":
      if message.author.id == "419810897058463754":
        member = discord.utils.get(client.get_all_members(), id=message.content[3:19])
        await client.send_message(member, "```[스넷봇 인공지능] : " + message.content[20:] + "```")
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
    if message.content[1:7] == "patner":
      await client.send_message(message.channel, "```[스넷봇 파트너 시스템]\n=patner :: 파트너시스템 도움말을 확인\n=patner list :: 파트너를 확인합니다.\n=patner apply :: 파트너를 신청합니다.[디코봇 1대1로]")
    else:
      if message.content[7:12] == "list":
        await client.send_message(message.channel, "```[스넷봇 파트너 시스템]" + "\n".join(patners))
      if message.content[7:11] == "add":
        if message.author.id == "419810897058463754":
          if message.content[11:]:
            await client.send_message(message.channel, "```[스넷봇 파트너 시스템] " + message.content[11:] + "님이 파트너목록에 추가되었습니다.")
            patners.append(message.content[11:])
          else:
            await client.send_message(message.channel, "```[스넷봇 파트너 시스템] 파트너목록에 추가할 유저의 이름을 적어주세요.")
        else:
          await client.send_message(message.channel, "```[스넷봇 파트너 시스템] 당신은 이 명령어를 사용할 권한이 없습니다.")
      if message.content[7:14] == "remove":
        if message.author.id == "419810897058463754":
          if message.content[14:]:
            await client.send_message(message.channel, "```[스넷봇 파트너 시스템] " + message.content[14:] + "님을 파트너목록에서 지우셨습니다.")
            patners.remove(message.content[14:])
          else:
            await client.send_message(message.channel, "```[스넷봇 파트너 시스템] 파트너목록에서 삭제할 유저의 이름을 적어주세요.")
        else:
          await client.send_message(message.channel, "```[스넷봇 파트너 시스템] 당신은 이 명령어를 사용할 권한이 없습니다.")
      if message.content[7:13] == "apply":
        if message.content[13:]
          if message.channel.is_private and message.author.id != "665768509707518033":
            await client.send_message(discord.utils.get(client.get_all_members(), id="419810897058463754"), message.author.name + "(" + message.author.id + ") : " + message.content[13:])
          else:
            await client.send_message(message.channel, "```[스넷봇 파트너 시스템] 해당 기능은 봇 1대1 채팅에서만 사용이 가능합니다.")
        else:
          await client.send_message(message.channel, "```[스넷봇 파트너 시스템] 파트너 되면 어떻게할건지 적어주세요!")
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
