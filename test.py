import requests
import discord
import random
from discord.ext import commands
from discord.ui import Button, View
import streamlit as st
import asyncio

st.set_page_config(
    page_title="discord_server_test",
    page_icon="😊",
    layout="wide",
)

st.title("Homun_bot")

hosting = st.button('호스팅')


 
app = commands.Bot(command_prefix='/',intents=discord.Intents.all())



headers = {
            'accept': 'application/json',
            'authorization': 'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyIsImtpZCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyJ9.eyJpc3MiOiJodHRwczovL2x1ZHkuZ2FtZS5vbnN0b3ZlLmNvbSIsImF1ZCI6Imh0dHBzOi8vbHVkeS5nYW1lLm9uc3RvdmUuY29tL3Jlc291cmNlcyIsImNsaWVudF9pZCI6IjEwMDAwMDAwMDAwODc4NTYifQ.Kz1Q31XCxpow-7vQUhjx8sejfVuQHi0T7BLfVoIXd4LErYMYJZ82oc9PX3Ls19rVxgvnNrwnpu2a2Ctg3vX8qO0214NgAh1Ab8M2hPPEksai7LY2enjhBGu7nvs8Ic9eq43p4DiGlpHQ68zZBbTo1WFbumayIrWkVAD-m7AHbkuguM0pMuXv8qL7ar6ZR-vVUsOetOuAannv6OpFhss3db1n4PuJM6S1TPyo2-Uo6T2FTp5Ue9C8TmIFnj97ZESorEU5KttbZ9qkL8yYnsK1A6glbYQksGMkCS0zQCp87BRQPccKAw41WlybHWcdjU3Zz3iDtMmQ5zv0GI_s0tzEmQ',
            'Content-Type': 'application/json',
            }
class Market_json:
    def __init__(self,name) -> None:
        self.name=name
    def item(self):
        json_market = {
        'Sort': '',
        'CategoryCode': 50000,
        'CharacterClass': '',
        'ItemTier': 0,
        'ItemGrade': '',
        'ItemName': self.name,
        'PageNo': 0,
        'SortCondition': 'ASC',
        }
        response_market =requests.post('https://developer-lostark.game.onstove.com/markets/items', headers=headers, json=json_market)
        content_market = response_market.json()
        search_market = content_market['Items']
        return search_market[0]
    

 
@app.event
async def on_ready():
    print('Done')
    await app.change_presence(status=discord.Status.online, activity=None)

@app.command()
async def 주사위(ctx):
    await ctx.send(random.randrange(0,100))


@app.command()    
async def 마켓(ctx,*,args):
    search = Market_json(args)    
    embed = discord.Embed(title='embed 기능 테스트',description='이게 embed란 말이지?', color = 0x62c1cc)
    try:
        embed.add_field(name=search.item()['Name'],value=search.item()['RecentPrice'])
    except:
        embed.add_field(name='품목을 정확히 입력해주세요',value='입력한 내용 '+args)
    embed.add_field(name='검색한 사람',value=ctx.message.author, inline=False)
    await ctx.send(embed = embed)

@app.command()
async def 버튼(ctx):
    button1 = Button(label="1번 버튼", style = discord.ButtonStyle.green)
    button2 = Button(label="2번 버튼", style = discord.ButtonStyle.green)
    button3 = Button(label="3번 버튼", style = discord.ButtonStyle.green)
    button4 = Button(label="4번 버튼", style = discord.ButtonStyle.green)
    button5 = Button(label="5번 버튼", style = discord.ButtonStyle.green)

    

    async def button_callback1(interaction:discord.Interaction):
        await interaction.response.send_message('1번 버튼 클릭!')              

    async def button_callback2(interaction:discord.Interaction):
        await interaction.response.send_message('2번 버튼 클릭!')

    async def button_callback3(interaction:discord.Interaction):
        await interaction.response.send_message('3번 버튼 클릭!')

    async def button_callback4(interaction:discord.Interaction):
        await interaction.response.send_message('4번 버튼 클릭!')

    async def button_callback5(interaction:discord.Interaction):
        await interaction.response.send_message('5번 버튼 클릭!')


    button1.callback = button_callback1
    button2.callback = button_callback2
    button3.callback = button_callback3
    button4.callback = button_callback4
    button5.callback = button_callback5


    view = View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)
    view.add_item(button5)

    await ctx.send(embed = discord.Embed(title='메뉴 선택하기',description="원하시는 버튼을 클릭해주세요", colour=discord.Colour.blue()), view=view)
a = 'MTA4NTc4MzcwODczMDE0Mjc1MA.GFR6w8.'
b = 'Pe8uEdvWDmM3c4uxWr25ZqUax1nKfCPy7oh-uc'
if hosting :   
    app.run(a+b)
    asyncio.sleep(86400)
    app.run(a+b)
else:
    pass
