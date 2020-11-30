
###################
####python 3.x#####
#discord.py==1.4.0#
###################

import discord
import requests

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 성공적으로 실행되었습니다.")
    game = discord.Game('!도움')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith('빈센아 실검'):
        json = requests.get('https://www.naver.com/srchrank?frm=main').json()
        ranks = json.get("data")
        data = []
        for r in ranks:
            rank = r.get("rank")
            keyword = r.get("keyword")
            if rank > 10:
                break
            data.append(f'**{rank}**위 {keyword}')

        dat = str(data)
        dat = dat.replace("'","")
        dat = dat.replace(", ","\n")
        dat = dat[1:-1]
        print(dat)
        embed = discord.Embed(title= '네이버 실시간 검색어 순위', description=(dat),colour=0x19CE60)
        await message.channel.send(embed=embed)


client.run('NzgxNzI3NjA0MTQyMTEyNzY5.X8B2kA.m6z1dZABxy12VHBBjDLwVnYGLpU')
