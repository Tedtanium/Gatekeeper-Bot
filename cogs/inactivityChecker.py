import discord
import datetime
from discord.ext import commands, tasks
import os
import psutil
import asyncio


client = commands.Bot(command_prefix = '>')

class inactivityChecker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.inactivityTime = 0
        #local variables needed initialized here.


    @commands.Cog.listener()
    async def on_ready(self):
        print('inactivityChecker cog loaded.')

    async def inactivityChecker(self, playersOnline):
        if playersOnline == 0:
            self.inactivityTime += 30
            if self.inactivityTime == 1800:
                print('Server has been inactive for 30 minutes.')
            if self.inactivityTime == 3600:
                print('Server has been inactive for 60 minutes.')
            if self.inactivityTime == 5400:
                print('Server has been inactive for 90 minutes.')
        else:
            self.inactivityTime = 0
        if self.inactivityTime >= 7200:
            print(str(datetime.datetime.now().time()) + ' - Server has been inactive for two hours! Shutting it down...')
            await self.bot.get_cog('stopServer').terminateServer()
            self.inactivityTime = 0
        return

def setup(bot):
    bot.add_cog(inactivityChecker(bot))
