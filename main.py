import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '~')

# Event Detection

@client.event
async def on_ready():
    print('Buzz Buzz! (BeeBot is ready.)')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server')

# Commands

@client.command()
async def buzz(ctx):
    await ctx.send(f'Buzz! ({round(client.latency * 1000)} ms)')

@client.command()
async def pollenate(ctx, member : discord.Member):
    await 

client.run('ODA1MDc2ODIyMjAyNzc3Njcw.YBVoOA.8N5mY3M4Otlili-pS2Jy0xwFJlk')