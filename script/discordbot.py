# discord 라이브러리 사용 선언
import discord
from selenium import webdriver
import commandLine

class chatbot(discord.Client):
    
    # 프로그램이 처음 실행되었을 때 초기 구성
    async def on_ready(self):
        # 상태 메시지 설정
        # 종류는 3가지: Game, Streaming, CustomActivity
        game = discord.Game("내용")

        # 계정 상태를 변경한다.
        # 온라인 상태, game 중으로 설정
        await client.change_presence(status=discord.Status.online, activity=game)

        # 준비가 완료되면 콘솔 창에 "READY!"라고 표시
        print("READY")

    # 봇에 메시지가 오면 수행 될 액션
    async def on_message(self, message):
        channel = message.channel
        
        # SENDER가 BOT일 경우 반응을 하지 않도록 한다.
        if message.author.bot:
            return None

        msg = "";
        # message.content = message의 내용
        if message.content == commandLine.COMMAND_HELLO :
            msg = ("안녕하세요 %s 님"% message.author.nick)
                
        if len(msg) != 0:
            await channel.send(msg)
            
        return None


# 프로그램이 실행되면 제일 처음으로 실행되는 함수
if __name__ == "__main__":
    # 객체를 생성
    client = chatbot()
    # TOKEN 값을 통해 로그인하고 봇을 실행
    client.run("ODc3MTU0NDc0NTU1MjExODE3.YRufww.WkPHhxA_I895tCp809OZZBcqOL8")
