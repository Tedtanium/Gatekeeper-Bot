import discord
from discord.ext import commands, tasks
import os
import psutil
import asyncio
import sys
sys.path.append('E:/Scripts/Gatekeeper-Bot-main/gatekeeper')
import management as mgmt
import datetime

client = commands.Bot(command_prefix = '>')

class Ticker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.timePassed = 0
        self.startHour = datetime.time(6)
        self.endHour = datetime.time(22)
        self.inactivityTime = 0
        self.oldStatus = 'Null'
        self.serverStatus = 'Down'
        self.tickCheck.start()
        
##### The meat of the cog. #########################################################        
    @tasks.loop(seconds=1.0)
    async def tickCheck(self):
        self.timePassed += 1
        ### Runs server_status_check if server is up every 30 seconds. ######
        if self.timePassed % 30 == 0:
            self.serverStatus = await mgmt.serverStatusCheck(self, 'listplayers')
                # Updates the bot's status with the current server status.
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Server | Status: " + self.serverStatus))
            await mgmt.statusHeartbeat(self)

        ### Runs after_hours_shutdown if server is not up, every 5 minutes. ######
        if self.timePassed % 600 == 0 and self.timePassed != 0:
            serverTest = await mgmt.serverTest(self)
            if serverTest == False:
                await mgmt.afterHoursShutdown(self, self.startHour, self.endHour)
            else:
                await mgmt.logger(self, 'After-Hours Shutdown: Server is still running!')
        if self.timePassed % 3600 == 0 and self.timePassed != 0:
            mgmt.canSave = True
####################################################################################



    @commands.Cog.listener()
    async def on_ready(self):
        await mgmt.logger(self, 'Ticker cog loaded.')
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Server | Status: ???"))


    @tickCheck.before_loop
    async def before_core(self):
        await mgmt.logger(self, '======= Script Started =======')
        await mgmt.logger(self, 'Waiting...')
        await self.bot.wait_until_ready()



def setup(bot):
    bot.add_cog(Ticker(bot))
