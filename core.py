import os
import discord
from discord.ext import commands, tasks
import time
import asyncio
import datetime
import psutil
#Server Status Check Only
from rcon import Client
import gatekeeper.management as mgmt



client = commands.Bot(command_prefix = '>')
bot_token = ''



@client.event
async def on_ready():
    print('Successfully logged in as {0.user}'.format(client))
    

    
class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # Variables.
        self.ipaddr = '0000'
        self.port = 0000
        self.passwod = ''
        self.startHour = datetime.time(6)
        self.endHour = datetime.time(22)
        self.inactivityTime = 0
        self.oldStatus = 'Down'
        self.core.start()
        
####### Remains of TickCheck - Not sure what to do/where to put this code at the moment. ######################
    @tasks.loop(seconds=1.0)
    async def core(self):
        ### Runs server_status_check if server is up every 30 seconds. ######
        if self.bot.get_cog('Ticker').timePassed % 30 == 0:
            serverTest = await mgmt.Management.serverTest(self)
            if serverTest == True:
                self.serverStatus = await mgmt.Management.serverStatusCheck(self, self.ipaddr, self.port, self.passwod)
                # Updates the bot's status with the current server status.
                await self.bot.get_cog('MoodUpdater').statusUpdate(self, self.serverStatus)
                self.bot.get_cog('ServerActions').serverStatus = self.serverStatus
            else:
                await self.bot.get_cog('MoodUpdater').statusUpdate(self, 'Down')
        ### Runs after_hours_shutdown if server is not up, every 5 minutes. ######
        if self.bot.get_cog('Ticker').timePassed % 600 == 0:
            serverTest = await mgmt.Management.serverTest(self)
            if serverTest == False:
                await mgmt.Management.afterHoursShutdown(self, self.startHour, self.endHour)
            else:
                print('After-Hours Shutdown: Server is still running!')

#############################################################################################################

    @core.before_loop
    async def before_core(self):
        print('Waiting...')
        await self.bot.wait_until_ready()

client.add_cog(Core(client))

######### Loads all cogs in cogs subfolder so long as they end in .py, cutting off the file extension. ######
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
client.run(bot_token)
