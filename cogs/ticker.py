import discord
from discord.ext import commands, tasks
import os
import psutil
import asyncio


client = commands.Bot(command_prefix = '>')

class Ticker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        #local variables needed initialized here.


    @commands.Cog.listener()
    async def on_ready(self):
        print('Ticker cog loaded.')



def setup(bot):
    bot.add_cog(Ticker(bot))
