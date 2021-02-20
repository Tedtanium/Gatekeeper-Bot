import discord
from discord.ext import commands, tasks
import os
import psutil
import asyncio


client = commands.Bot(command_prefix = '>')

class Ticker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.timePassed = 0
        self.tickCheck.start()
        
        
    @tasks.loop(seconds=1.0)
    async def tickCheck(self):
        self.timePassed += 1

    def cog_unload(self):
        self.tickCheck.cancel()
        

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ticker cog loaded.')

    @tickCheck.before_loop
    async def before_tick(self):
        print('Waiting...')
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(Ticker(bot))
