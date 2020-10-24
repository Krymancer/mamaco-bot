import os
import discord
from discord.ext import commands

from dotenv import load_dotenv

from random import random,randrange
from datetime import datetime

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

prefix = 'm!'
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name="etero")
async def etero(ctx, arg=None):
    if not arg:
        await ctx.send('KKKKKKK burro, tem que mencionar alguem.')
    else:
        if random() > 0.5:
            await ctx.send(arg + ' É  etero kkkkkkkk')
        else:
            await ctx.send(arg + ' Não é etero. Que bom, continue assim!')

@bot.command(name="quenhe")
async def quenhe(ctx, arg=None):
    if not arg:
        await ctx.send('KKKKKKK burro, tem que mencionar alguem.')
    else:
        await ctx.send(f'Quem é {arg}?\n\nPara o cego {arg} é a luz.\nPara o faminto {arg} é o pão.\nPara o sedento {arg} é a fonte de água viva.\nPara o morto {arg} é a vida.\nPara o enfermo {arg} é a cura.\nPara o prisioneiro {arg} é a liberdade.\nPara o solitário {arg} é o companheiro.\nPara o viajante {arg} é o caminho.\nPara o sábio {arg} é a sabedoria.\nPara a medicina {arg} é o médico dos médicos.\nPara o réu {arg} é o advogado.\nPara o advogado {arg} é o Juiz.\nPara o Juiz {arg} é a justiça.\nPara o cansado {arg} é o alívio.\nPara o pedreiro {arg} é a pedra principal.\nPara o jardineiro {arg} é a rosa de Sharon.\nPara o triste {arg} é a alegria.\nPara o leitor {arg} é a palavra.\nPara o pobre {arg} é o tesouro.\nPara o devedor {arg} é o perdão.\n\nPara mim {arg} é TUDO!')

@bot.command(name="hora")
async def hora(ctx,arg=None):
    now = datetime.now()
    datestr = now.strftime("%d/%m/%Y %H:%M:%S")
    await ctx.send(datestr)

@bot.command(name="pau")
async def hora(ctx,arg=None):
    await ctx.send(f"Parabens seu pau tem {randrange(1,30)}cm!")


bot.run(TOKEN)