#This cog is very unfinished!
import discord

from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext import commands
from discord import Embed

client = discord.Client()

class listener(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        await self.bot.stdout.send("Listener Drones on Standby")
        print("Listener Drones on Standy")
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("listener")

    # @command()
    # async def reed(self, ctx):
    #     messages = await ctx.channel.history(limit=500).flatten()
    #     end = 0
        
    #     for msg in messages:
    #         if (msg.author == ctx.guild.get_member(89553652477358080)) and (end == 0):
    #             reedMessage = msg.content
    #             pfp = msg.author.avatar_url

    #             if isinstance(reedMessage, str) and isinstance(pfp, str):

    #                 embed = Embed(description=reedMessage)
    #                 embed.set_author(name=user.name, icon_url=pfp)
    #                 await ctx.send(embed=embed)
    #                 end = 1

    #             return
    #         print("searching...")
    #     await ctx.send("The prophet has not spoken here in some time...")

def setup(bot):
    bot.add_cog(listener(bot))