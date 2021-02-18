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
bot_token = 'Nzk2NDI1OTcyNjAxNDU0NjUz.X_XvfA.-frxvyDMx1CDG_ymS21plgO7ZP0'



@client.event
async def on_ready():
    print('Successfully logged in as {0.user}'.format(client))

@client.command()
async def startServer(ctx):
    #To get the emoji in unicode, type \<:emoji:> in Discord, and copy the result.
    print('Starting server via command sent from Discord!')
    await Ticker.startServer()
    #await asyncio.sleep(5)
    if "ShooterGameServer.exe" in (p.name() for p in psutil.process_iter()) == True:
        await ctx.message.add_reaction('⬆️')
        await ctx.message.channel.send('Server is starting! Please stand back, this may take a while...')
    # if statement -> if server is up, responds back @ing the person who said this
            #asyncio.wait_for(management.server_status == 'Up', None) ?
                #await message.channel.send('Okay, we should be good now, ')    
    
@client.command()
async def stopServer(ctx):
    await ctx.message.add_reaction('🛑')
    await ctx.message.channel.send('Successfully got stop command!')
    await Ticker.stopServer()
    
class Ticker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.timePassed = 0
        self.ipaddr = '127.0.0.1'
        self.port = 27020
        self.passwod = '_yeetles_'
        self.startHour = datetime.time(6)
        self.endHour = datetime.time(22)
        self.fileKill = 'ShooterGameServer.exe'
        self.inactivityTime = 0
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
        if self.timePassed % 5 == 0:
            serverTest = "ShooterGameServer.exe" in (p.name() for p in psutil.process_iter())
            if serverTest == True:
                self.serverStatus, self.playerCount = await self.serverStatusCheck(self.ipaddr, self.port, self.passwod)
                print('Server Status Check has been run! The server is ' + self.serverStatus + ' and there are ' + str(self.playerCount) + ' players online.')
                await self.inactivityChecker(self.playerCount)
            else:
                print('Server status check: Server is not running! Server status check has been skipped.')
        ### Runs after_hours_shutdown if server is not up, every 5 minutes. ######
        if self.timePassed % 600 == 0:
            if "ShooterGameServer.exe" in (p.name() for p in psutil.process_iter()) == False:
                self.afterHoursShutdown(self.startHour, self.endHour)
            else:
                print('After-Hours Shutdown: Server is still running! Check for what time it is has been skipped.')

#############################################################################################################

    @tickCheck.before_loop
    async def before_tick(self):
        print('Waiting...')
        await self.bot.wait_until_ready()

####### Server Status Checker ###############################################################################

    async def serverStatusCheck(self, ipaddr, port, passwod):
  # Instigates connection to RCON and tries to get a playercount; if this fails the server is still starting.
        try:
            with Client(ipaddr, port, passwd=passwod) as client:
                playersOnline = client.run('listplayers')
            serverStatus = 'Up'
            if 'No Players Connected' in playersOnline:
                playerCount = 0
            else: 
                playerCount = (playersOnline).count('\n')
        except:
        # If this is running and gives an error, the server is still going up. The player_count variable is dummied out for this instance.
            serverStatus = 'Starting'
            playerCount = -1
        return(serverStatus, playerCount)

#############################################################################################################


###### Server Inactivity Checker ############################################################################

    async def inactivityChecker(self, playersOnline):
        if playersOnline == 0:
            self.inactivityTime += 30
            if self.inactivityTime == 1800:
                print('Server has been inactive for 30 minutes.')
        else:
            self.inactivityTime = 0
        if self.inactivityTime >= 30:
            print(str(datetime.datetime.now().time()) + ' - Server has been inactive for two hours! Shutting it down...')
            await self.stopServer()
            self.inactivityTime = 0
        return


#############################################################################################################

####### After-Hours Shutdown ################################################################################

    async def afterHoursShutdown(start_hour, end_hour):
        if end_hour <= datetime.datetime.now().time() <= start_hour:
            os.system("shutdown /s /t 1")
        else:
            print('The time is ' + str(datetime.datetime.now().time()) + '. It\'s not time to shut down yet!')

#############################################################################################################

####### Server Starter ######################################################################################

    async def startServer():
        os.startfile('E:\\steamcmd\\ARK\\ShooterGame\\Binaries\\Win64\\ARK Serverstart Island.bat')

#############################################################################################################

####### Server Terminator ###################################################################################

    async def stopServer(self):
        try:
            os.system('TASKKILL /IM ' + self.fileKill)
        except:
            print("serverTeminator: Your governor is broken. Get in the CHOPPA!")

#############################################################################################################

client.add_cog(Ticker(client))
client.run(bot_token)

# Debug tool section.
# Sends a message in channel.
#await message.channel.send('Hello!')
