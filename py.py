import discord
import os
import datetime


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
  coins[message.author.id] = 1000
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
    if message.content[1:5] == "packs":
      await client.send_message(message.channel, "```[스넷봇 특별팩 판매]\n[VIP] :: 스넷봇 공식 VIP랭크\n[MVP] :: 스넷봇 공식 MVP랭크\n[MVP+] :: 스넷봇 공식 MVP+랭크```")
    else:
      if message.content[5:8] == "buy":
        await client.send_message(message.channel, "```[스넷봇 특별팩 판매] =packs buy <pack name>```")
      else:
        if message.content[9:18] == "special":
          if coins[message.author.id] >= 500:
            await client.send_message(message.channel, "[스넷봇 특별팩 판매] 서버와 연결도중 오류가 발생하여, 구입이 실패되었습니다.")
          else:
            await client.send_message(message.channel, "[스넷봇 특별팩 판매] 코인이 부족합니다.")
    if message.content[1:5] == "coin":
      await client.send_message(message.channel, "[스넷봇 코인 시스템]\n=coin :: 코인 도움말을 확인\n=coin ces :: 당신의 코인을 확인")
    else:
      if message.content[5:9] == "ces":
        mycoin = coins[message.author.id]
        await client.send_message(message.channel, "[스넷봇 코인 시스템] 당신이 보유중인 코인은 " + mycoin + "코인 입니다.")
          
  if message.content == "안녕 스넷봇":
    if message.author.id == "419810897058463754":
      await client.send_message(message.channel, "안녕하세요! 스넷봇 총개발자 헌덴님!")
    else:
      await client.send_message(message.channel, "안녕하세요! " + message.author.name + "님!")
      
      
      
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
