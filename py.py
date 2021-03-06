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
  await client.change_presence(game=discord.Game(name='=help / =options 사용해주세요.', type=1))

@client.event
async def on_member_join(member):
  channel = discord.utils.get(member.guild.channels, name="welcome")
  await channel.send(f"[member.mention]님 환영합니다!")

@client.event
async def on_message(message):
  SN = "`[스넷봇 시스템]"
  serverf = "Online"
  servert = "Online"
  if message.content == "=":
    await client.send_message(message.channel, SN + " 기본 명령어: =help`")
  else:
    if message.content[1:5] == "help":
      await client.send_message(message.channel, "```[스넷봇 공식 시스템]\n=help :: 도움말 확인\n=contact :: 개발자에게 문의\n=server :: 서버 상태확인\n안녕 스넷봇 :: 스넷봇에게 인사\n=update :: 스넷봇 업데이트 기록을 확인합니다.\n\n공식 디스코드서버: https://discord.gg/QwGfSuj```")
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
      await client.send_message(message.channel, SN + "\n서버1 :: " + serverf + "\n서버2 :: " + servert + "`")
    if message.content[1:5] == "mote":
      if message.channel.id == "668730681421070356":
        author = message.guild.get_member(int(message.author.id))
        role = discord.utils.get(message.guild.roles, name="시청자")
        await author.add_roles(role)
      else:
        await client.send_message(message.channel, "[스넷봇 시스템] 해당 채널에서는 해당 명령어를 사용하실 수 없습니다.")
    if message.content[1:7] == "update":
      server = "NotErrors"
      if server == "NotErrors":
        await client.send_message(message.channel, "```[스넷봇 업데이트 시스템]\n현재버전: v1.0.4-RELEASE\n(v1.0.4-RELEASE) :: 업데이트 명령어 추가, 오류 수정, 버그 수정\n(v1.0.4-BETA) :: 오류 수정\n(v1.0.3) :: 버그,오류 수정\n(v1.0.2) :: 서버 업데이트\n(v1.0.1) :: 문의명령어 추가\n(v1.0.0) :: 서버 2채널 추가\n(v0.9.9) :: 서버 1채널 추가\n(v0.9.8) :: 오류 수정\n(v0.9.7) :: 시스템 점검, 시스템 업데이트\n(v0.9.7-Alpha) :: 도움말 명령어 추가\n(v0.9.7.10) :: 버그 수정, 오류 수정```") 
      else:
        await client.send_message(message.channel, "```[스넷봇 업데이트 시스템] 서버와 연결도중 오류가 발생하였습니다.\n오류코드: `NEDI09`,`HEIO92`\n오류 코드를 뮨의하실 때 같이 보내시면 됩니다.```")
    if message.content[1:8] == "options":
      await client.send_message(message.channel, "```[스넷봇 옵션 시스템]\n서버1채널 :: " + serverf + "\n서버2채널 :: " + servert + "\n\n오류방지: On\n봇 자동최적화: On\n서버 자동최적화: Off\n서버 자동재부팅: Off\n봇 자동재부팅: On\n서버 외부아이피 차단: Off\n실시간 차단: Off```")
  if message.content == "안녕 스넷봇":
    if message.author.id == "419810897058463754":
      await client.send_message(message.channel, "```[개발자 알림] 안녕하세요! 스넷봇 총개발자 " + message.author.name + "님!```")
    else:
      if message.author.id == "618778311291830292":
        await client.send_message(message.channel, "```[개발자 알림] 안녕하세요! 스넷봇 부개발자 " + message.author.name + "님!```")
      else:
        if message.author.id == "545485943415635969":
          await client.send_message(message.channel, "`[파트너 알림] 안녕하세요! 스넷봇 공식 파트너 " + message.author.name + "님!`")
        else:
          if message.author.id == "421291279939403788":
            await client.send_message(message.channel, "`[파트너 알림] 안녕하세요! 스넷봇 공식 파트너 " + message.author.name + "님!`")
          else:
            await client.send_message(message.channel, "안녕하세요! " + message.author.name + "님!")
      
      
      
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
