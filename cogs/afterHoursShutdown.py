import discord
from discord.ext import commands, tasks
import os
import psutil
import asyncio
import datetime


client = commands.Bot(command_prefix = '>')

class afterHoursShutdown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        #local variables needed initialized here.


    @commands.Cog.listener()
    async def on_ready(self):
        print('afterHoursShutdown cog loaded.')

    async def afterHoursShutdown(self, start_hour, end_hour):
        if end_hour <= datetime.datetime.now().time() <= start_hour:
            os.system("shutdown /s /t 1")
        else:
            print('After-Hours Shutdown: The time is ' + str(datetime.datetime.now().time()) + '. It\'s not even late yet!')

def setup(bot):
    bot.add_cog(afterHoursShutdown(bot))
