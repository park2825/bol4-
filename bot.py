import discord
import asyncio
import datetime
from datetime import date

client =  discord.Client()
botname = 'BOL4봇'
token = 'ODQzMzIxMTQ1MzE3OTE2Njcz.YKCKBQ.2f5kMsbq0JLcovxQAJQ9Q5Ua6qE'

@client.event
async def on_ready():
    bol4 = (date.today() - date(2016, 4, 22)).days

    print(client.user.name)
    print(client.user.id)

    server = len(client.guilds)
    users = 0
    for now_guild in client.guilds:
        users = users + len(now_guild.members)
    
    while True:
        await client.change_presence(status=discord.Status.online, activity=discord.Game('`볼사봇 도움말` 입력!'))
        await asyncio.sleep(10)
        await client.change_presence(status=discord.Status.online, activity=discord.Game(str(server)+'개의 서버 | '+str(users)+'개의 서버'))
        await asyncio.sleep(10)
        await client.change_presence(status=discord.Status.online, activity=discord.Game('지금은 볼사가 데뷔한지 '+str(bol4)+'일째!'))
        await asyncio.sleep(10)

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content.startswith('볼사봇 도움말'):
        e = discord.Embed(title=botname+'의 도움말', description=botname+'의 기능을 알려드립니다.', color=0xffc0cb)
        e.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/180306_Bolbbalgan4_at_a_fansinging_%281%29.jpg/250px-180306_Bolbbalgan4_at_a_fansinging_%281%29.jpg')
        e.add_field(name='볼사봇 도움말', value=botname+'의 기능을 알려드립니다.', inline=True)
        e.add_field(name='볼사봇 안지영/안졍/졍쓰', value='안지영의 정보를 알려드립니다.', inline=True)
        e.add_field(name='볼사봇 우지윤/우쥰/낯선아이', value='우지윤의 정보를 알려드립니다.', inline=True)
        e.add_field(name='볼사봇 볼빨간사춘기/볼사', value='볼빨간사춘기의 정보를 알려드립니다.', inline=True)
        e.set_footer(text='%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
        await message.channel.send(embed=e)
        print('%s#%s님이 도움말을 확인하였습니다.' % (message.author.name, message.author.discriminator))

    if message.content.startswith('볼사봇 안지영') or message.content.startswith('볼사봇 안졍') or message.content.startswith('볼사봇 졍쓰'):
        e = discord.Embed(title='안지영의 정보', description='안지영의 정보를 알려드립니다.', color=0xffc0cb)
        e.set_thumbnail(url='https://cdnweb01.wikitree.co.kr/webdata/editor/202004/02/img_20200402203302_0ab77b1b.webp')
        e.add_field(name='이름', value='안지영', inline=True)
        e.add_field(name='출생', value='1995년 9월 14일 (25세)\n경상북도 영주시', inline=True)
        e.add_field(name='국적', value='대한민국', inline=True)
        e.add_field(name='본관', value='순흥 안씨', inline=True)
        e.add_field(name='신체', value='165cm, 45kg, A형, 손 길이 17.5cm', inline=True)
        e.add_field(name='학력', value='영주동부초등학교\n동산여자중학교\n영주여자고등학교\n성신여자대학교', inline=True)
        e.add_field(name='소속그룹', value='볼빨간사춘기', inline=True)
        e.add_field(name='소속사', value='소파르뮤직', inline=True)
        e.add_field(name='데뷔', value='2016년 4월 22일\n볼빨간사춘기 EP엘범 RED lCKLE', inline=True)
        e.set_footer(text='%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
        await message.channel.send(embed=e)
        print('%s#%s님이 안지영의 정보를 확인하였습니다.' % (message.author.name, message.author.discriminator))

    if message.content.startswith('볼사봇 우지윤') or message.content.startswith('볼사봇 우쥰') or message.content.startswith('볼사봇 낯선아이'):
        e = discord.Embed(title='우지윤의 정보', description='우지윤의 정보를 알려드립니다.', colour=0xffc0cb)
        e.set_thumbnail(url='https://www.yeongnam.com/mnt/file/202006/20200619001337434_1.jpg')
        e.add_field(name='이름', value='우지윤', inline=True)
        e.add_field(name='예명', value='낯선아이', inline=True)
        e.add_field(name='출생', value='1966년 1월 6일 (25세)\n경상북도 영주시', inline=True)
        e.add_field(name='국적', value='대한민국', inline=True)
        e.add_field(name='신체', value='160cm, 44kg, A형', inline=True)
        e.add_field(name='소속사', value='ID:ODD', inline=True)
        e.add_field(name='데뷔', value='2016년 볼빨간사춘기 EP 앨범 RED lCKLE', inline=True)
        e.add_field(name='경력', value='볼빨간사춘기(2016년 4월 22일 ~ 2020년 4월 2일)', inline=True)
        e.add_field(name='종교', value='개신교', inline=True)
        e.set_footer(text='%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
        await message.channel.send(embed=e)
        print('%s#%s님이 우지윤의 정보를 확인하였습니다.' % (message.author.name, message.author.discriminator))

    if message.content.startswith('볼사봇 볼빨간사춘기'):
        bol4 = (date.today() - date(2016, 4, 22)).days

        e = discord.Embed(title='볼빨간사춘기의 정보', description='볼빨간사춘기의 정보를 알려드립니다.', color=0xffc0cb)
        e.set_thumbnail(url='https://pds.joins.com/news/component/htmlphoto_mmdata/202004/02/4f5ea1bd-1e9c-466c-a735-d44a5f9dbc1d.jpg')
        e.add_field(name='그룹명', value='볼빨간사춘기', inline=True)
        e.add_field(name='멤버', value='안지영, 우지윤(탈퇴)', inline=True)
        e.add_field(name='결성 연도 및 지역', value='2011년, 경상북도 영주시', inline=True)
        e.add_field(name='데뷔', value='2016년 4월 22일 EP 앨범 RED lCKLE', inline=True)
        e.add_field(name='데뷔일', value='D+'+str(bol4), inline=True)
        e.set_footer(text='%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
        await message.channel.send(embed=e)
        print('%s#%s님이 볼빨간사춘기의 정보를 확인하였습니다.' % (message.author.name, message.author.discriminator))




client.run(token)