import os
import discord
from discord.ext import commands, tasks
import time
import asyncio
import datetime
import psutil
#Server Status Check Only
from rcon import Client



client = commands.Bot(command_prefix = '>')
bot_token = ''



@client.event
async def on_ready():
    print('Successfully logged in as {0.user}'.format(client))
    

    
class Ticker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.timePassed = 0
        self.ipaddr = '0.0.0.0'
        self.port = 0000
        self.passwod = '0000'
        self.startHour = datetime.time(6)
        self.endHour = datetime.time(22)
        self.tickCheck.start()
        
        

    def cog_unload(self):
        self.tickCheck.cancel()

######### TickCheck - The central timer function ############################################################

    @tasks.loop(seconds=1.0)
    async def tickCheck(self):
        self.timePassed += 1
        ## Heartbeat
        #if self.timePassed % 5 == 0:
            #print('Seconds passed since timer started: ' + str(self.timePassed))
        ### Runs server_status_check if server is up every 30 seconds. ######
        if self.timePassed % 30 == 0:
            serverTest = "ShooterGameServer.exe" in (p.name() for p in psutil.process_iter())
            if serverTest == True:
                self.serverStatus, self.playerCount = await self.bot.get_cog('statusCheck').serverStatusCheck(self.ipaddr, self.port, self.passwod)
                print('Server Status Check: The server is currently ' + self.serverStatus + ' with ' + str(self.playerCount) + ' players online.')
                # Updates the bot's status with the current server status.
                await self.bot.get_cog('moodUpdater').statusUpdate(self, self.serverStatus)
                self.bot.get_cog('startServer').serverStatus = self.serverStatus
                # Runs inactivityChecker cog.
                await self.bot.get_cog('inactivityChecker').inactivityChecker(self.playerCount)
            else:
                print('Server status check: Server is offline!')
                await self.bot.get_cog('moodUpdater').statusUpdate(self, 'Down')
        ### Runs after_hours_shutdown if server is not up, every 5 minutes. ######
        if self.timePassed % 600 == 0:
            serverTest = "ShooterGameServer.exe" in (p.name() for p in psutil.process_iter())
            if serverTest == False:
                await self.bot.get_cog('afterHoursShutdown').afterHoursShutdown(self.startHour, self.endHour)
            else:
                print('After-Hours Shutdown: Server is still running!')

#############################################################################################################

    @tickCheck.before_loop
    async def before_tick(self):
        print('Waiting...')
        await self.bot.wait_until_ready()


client.add_cog(Ticker(client))
######### Loads all cogs in cogs subfolder so long as they end in .py, cutting off the file extension. ######
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
client.run(bot_token)

# Debug tool section.
# Sends a message in channel.
#await message.channel.send('Hello!')
