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
    ### Loads all cogs in cogs subfolder so long as they end in .py, cutting off the file extension. ######
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')

###########################################################################################################
        


    
@client.command()
async def stopServer(ctx):
    await ctx.message.channel.send('Got it! Lowering the gates now...')
    await Ticker.stopServer()
    await asyncio.sleep(5)
    serverTest = "ShooterGameServer.exe" in (p.name() for p in psutil.process_iter())
    if serverTest == False:
        print('Server successfully closed via command.')
        await ctx.message.add_reaction('🛑')
    else:
        await ctx.message.channel.send('The gate...didn\'t close. Something\'s wrong.')
    
class Ticker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.timePassed = 0
        self.ipaddr = '0.0.0.0'
        self.port = 0000
        self.passwod = '0000'
        self.startHour = datetime.time(6)
        self.endHour = datetime.time(22)
        self.fileKill = 'ShooterGameServer.exe'
        self.inactivityTime = 0
        self.tickCheck.start()
        
    async def load(ctx, extension):
        client.load_extension(f'cogs.{startServer}')
        

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
                self.serverStatus, self.playerCount = await self.serverStatusCheck(self.ipaddr, self.port, self.passwod)
                print('Server Status Check: The server is currently ' + self.serverStatus + ' with ' + str(self.playerCount) + ' players online.')
                await self.inactivityChecker(self.playerCount)
            else:
                print('Server status check: Server is offline! Server status check skipped.')
        ### Runs after_hours_shutdown if server is not up, every 5 minutes. ######
        if self.timePassed % 600 == 0:
            if "ShooterGameServer.exe" in (p.name() for p in psutil.process_iter()) == False:
                self.afterHoursShutdown(self.startHour, self.endHour)
            else:
                print('After-Hours Shutdown: Server is still running! Time check has been skipped.')

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
        if self.inactivityTime >= 7200:
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

    async def stopServer():
        try:
            os.system('TASKKILL /IM ' + 'ShooterGameServer.exe')
        except:
            print("serverTeminator: Your governor is broken. Get in the CHOPPA!")

#############################################################################################################

client.add_cog(Ticker(client))
client.run(bot_token)

# Debug tool section.
# Sends a message in channel.
#await message.channel.send('Hello!')
