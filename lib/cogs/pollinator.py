import discord

from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext import commands

class Pollinator(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        await self.bot.stdout.send("Pollinator Drones on Standby")
        print("Pollinator Drones on Standy")
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("pollinator")

    @command()
    async def buzz(self, ctx):
        await ctx.send(f'Buzz! ({round(self.bot.latency * 1000)} ms)')

    @command()
    async def sting(self, ctx, member: discord.Member):
        await ctx.send('command still in development')



    @command()
    async def pollinate(self, ctx):
        PollenRole = discord.utils.get(ctx.guild.roles, name="Pollen")
        if PollenRole in ctx.author.roles:
            await ctx.send('Youre already holding as much pollen as you can carry!')
        else:
            await ctx.author.add_roles(PollenRole)
            await ctx.send('You collected some pollen!')
        

    @command()
    async def honey(self, ctx):
        PollenRole = discord.utils.get(ctx.guild.roles, name="Pollen")
        if PollenRole in ctx.author.roles:
            await ctx.author.remove_roles(PollenRole)
            await ctx.send('You made honey! What a hard worker.')
        else:
            await ctx.send('Silly goose, you need pollen to make honey!')

def setup(bot):
    bot.add_cog(Pollinator(bot))