import os
import discord
from discord.ext import commands, tasks
import time
import asyncio
import datetime
import psutil
from rcon import Client

class Management():
    def __init__(self):
        serverStatus = 'Down'
        
###################### Start Server #####################

    async def bootServer(filepath):
        os.startfile(filepath)
        
#########################################################

###################### Stop Server ######################

    async def terminateServer(target):
            os.system('TASKKILL /IM ' + target)

#########################################################

###################### Status Check #####################

    async def serverStatusCheck(self, ipaddr, port, passwod):
  # Instigates connection to RCON and tries to get a playercount; if this fails the server is still starting.
        try:
            with Client(ipaddr, port, passwd=passwod) as client:
                playersOnline = client.run('listplayers')
            self.serverStatus = 'Up'
            if 'No Players Connected' in playersOnline:
                playerCount = 0
            else: 
                playerCount = (playersOnline).count('\n')
        except:
        # If this is running and gives an error, the server is still going up. The player_count variable is dummied out for this instance.
            serverStatus = 'Starting'
            playerCount = -1
        return(self.serverStatus, playerCount)

#########################################################

#################### Inactivity Check ###################

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

#########################################################

################## After-Hours Shutdown #################

    async def afterHoursShutdown(self, start_hour, end_hour):
        if end_hour <= datetime.datetime.now().time() <= start_hour:
            os.system("shutdown /s /t 1")
        else:
            print('After-Hours Shutdown: The time is ' + str(datetime.datetime.now().time()) + '. It\'s not even late yet!')

#########################################################

