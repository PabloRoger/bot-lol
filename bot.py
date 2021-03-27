import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

from utils.lol import Lol, LolInfo
from utils.util import roman_to_int

load_dotenv()
DISCORD_API_KEY = os.getenv('DISCORD_API_KEY')

bot = commands.Bot(
    command_prefix='>',
    description='League of legends bot'
)

@bot.event
async def on_ready():
    print('Estoy ready papi')
    print(bot.user.name)
    print(bot.user.id)


@bot.command(descrption='Show all the commands')
async def helpMe(ctx, member:discord.Member = None):
    if member == None:
        member = ctx.author

    nameAuthor = member.display_name

    emb = discord.Embed(title='Comandos básicos')
    emb.set_author(name=nameAuthor)
    emb.add_field(name='>user {Nombre del Invocador} {Región}', value='Da info sobre el usuario. Ejemplo: >user ElThuHitos EUW', inline=False)
    emb.add_field(name='>rank {Nombre del Invocador} {Región}', value='Da info sobre la clasificacion del usuario. Ejemplo: >rank ElThuHitos EUW', inline=False)
    emb.add_field(name='>exotico {Nombre del Invocador (Opcional)}', value='Te da un peak muy exotico. El usuario es opcional Ejemplo: >exotico @ElThuHitos', inline=False)
    await ctx.send(embed=emb)

@bot.command(descrption='Show the user info')
async def user(ctx, summoner: str, region: str):
    lol = Lol(summoner, region)
    data = lol.greetings()

    greetings = data['greetings']
    icon_url = data['icon_url']

    emb = discord.Embed(title=greetings)
    emb.set_image(url=icon_url)
    await ctx.send(embed=emb)

@bot.command(descrption='Show the user rank')
async def rank(ctx, summoner: str, region: str):
    lol = Lol(summoner, region)
    ranks = lol.rank()

    tier = ranks['tier']
    rank = ranks['rank']
    league_points = ranks['leaguePoints']
    wins = ranks['wins']
    losses = ranks['losses']

    num = roman_to_int(rank)
    url = f'https://opgg-static.akamaized.net/images/medals/{tier.lower()}_{num}.png?image=q_auto:best&v=1'

    emb = discord.Embed(title='Clasificatoria en solitario', description=f'{tier} {rank}')
    emb.set_image(url=url)
    emb.insert_field_at(index=0, name='LP', value=league_points)
    emb.insert_field_at(index=1, name='V', value=wins)
    emb.insert_field_at(index=2, name='L', value=losses)
    await ctx.send(embed=emb)


@bot.command(description='Select a random peak')
async def exotico(ctx, member:discord.Member = None):
    if member == None:
        member = ctx.author

    nameAuthor = member.display_name

    lol = LolInfo()
    exoticPeak = lol.exotico()

    name = exoticPeak['name']
    attack = exoticPeak['info']['attack']
    defense = exoticPeak['info']['defense']
    magic = exoticPeak['info']['magic']
    difficulty = exoticPeak['info']['difficulty']
    tags = exoticPeak['tags']
    tags_str = ', '.join(tags).replace("'", '')

    url = f'https://ddragon.leagueoflegends.com/cdn/13.22.1/img/champion/{name}.png'

    emb = discord.Embed(title=f'{name}', description=f'A ver si tienes cojones a ganar con {name}', colour=discord.Colour.random())
    emb.set_author(name=f'Jugador: {nameAuthor}')
    emb.set_thumbnail(url=url)
    emb.add_field(name='Roles Asociados', value=f'{tags_str}')
    emb.add_field(name='Info Básica', value='', inline=False)
    emb.insert_field_at(index=2, name='Ataque', value=f'{attack}')
    emb.insert_field_at(index=3, name='Defensa', value=f'{defense}', inline=True)
    emb.insert_field_at(index=4, name='Magia', value=f'{magic}')
    emb.insert_field_at(index=5, name='Dificultad', value=f'{difficulty}')

    await ctx.send(embed=emb)

bot.run(DISCORD_API_KEY)