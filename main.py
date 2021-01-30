import os
from dotenv import load_dotenv

load_dotenv()

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
async def sting(ctx, member: discord.Member):
    await ctx.send('command still in development')


@client.command()
async def pollenate(ctx):
    PollenRole = discord.utils.get(ctx.guild.roles, name="Pollen")
    await ctx.author.add_roles(PollenRole)

@client.command()
async def honey(ctx):
    PollenRole = discord.utils.get(ctx.guild.roles, name="Pollen")
    await ctx.author.remove_roles(PollenRole)
    await ctx.send('You made honey! What a hard worker.')

client.run(os.getenv("TOKEN"))