import os
import time
import asyncio
import datetime
import psutil
from rcon import Client

serverStatus = 'Down'
ipaddr = '127.0.0.1'
port = 27020
passwod = '_yeetles_'
lastSave = -1
startHour = datetime.time(6)
endHour = datetime.time(22)
        
###################### Start Server #####################

async def bootServer(self, filepath):
    os.startfile(filepath)
        
#########################################################

###################### Stop Server ######################

async def terminateServer():
    target = 'ShooterGameServer.exe'
    os.system('TASKKILL /IM ' + target)

#########################################################

##############  Server exe is Running Test ##############

async def serverTest(self):
    serverProcessExists = "ShooterGameServer.exe" in (p.name() for p in psutil.process_iter())
    return(serverProcessExists)
    
#########################################################

###################### Status Check #####################

async def serverStatusCheck(self, cmd):
# Instigates connection to RCON and tries to get a playercount; if this fails the server is still starting.
    global serverStatus, ipaddr, port, passwod
    serverProcessExists = await serverTest(self)
    if serverProcessExists == True:
        try:
            with Client(ipaddr, port, passwd=passwod) as client:
                # If statement that catches worldsave command without polluting serverStatus.
                if cmd == 'saveworld':
                    client.run(cmd)
                    return
                playersOnline = client.run(cmd)
            serverStatus = 'Up'
            if 'No Players Connected' in playersOnline:
                playerCount = 0
            else: 
                playerCount = (playersOnline).count('\n')
        except:
        # If this is running and gives an error, the server is still going up. The player_count variable is dummied out for this instance.
            serverStatus = 'Starting'
            playerCount = -1
        await inactivityChecker(self, playerCount)
    else:
        serverStatus = 'Down'
    return(serverStatus)

#########################################################

#################### Inactivity Check ###################

async def inactivityChecker(self, playersOnline):
    if playersOnline == 0:
        self.inactivityTime += 30
    else:
        self.inactivityTime = 0
    if self.inactivityTime >= 7200:
        await logger(self, str(datetime.datetime.now().strftime("%H:%M:%S")) + 'Server has been inactive for two hours! Shutting it down...')
        await terminateServer()
        self.inactivityTime = 0
    return

#########################################################

################## After-Hours Shutdown #################

async def afterHoursShutdown(self):
    global startHour, endHour
    if endHour <= datetime.datetime.now().time() or datetime.datetime.now().time <= startHour:
        os.system("shutdown /s /t 1")
    else:
        await logger(self, 'After-Hours Shutdown: It\'s not even late yet!')

#########################################################

#################### Status Heartbeat ###################

async def statusHeartbeat(self):
    if self.oldStatus != self.serverStatus:
        await logger(self, 'Server state change: ' + self.oldStatus + ' -> ' + self.serverStatus)
        self.oldStatus = self.serverStatus
    if self.inactivityTime % 1800 == 0 and self.inactivityTime != 0 and self.serverStatus == 'Up':
        await logger(self, str(int(self.inactivityTime / 60)) + ' minutes have passed in inactivity.')

#########################################################

####################### Logger ##########################

async def logger(self, msg):
    # Logic that determines what file is to be opened and written to. Logs change on the daily.
    targetFile = str(datetime.date.today().year) + '-' + str(datetime.date.today().month) + '-' + str(datetime.date.today().day) + '-Gatekeeper-Log.txt'
    targetPath = ".\\logs\\"
    open(targetPath + targetFile, "a").writelines('[' + str(datetime.datetime.now().strftime("%H:%M:%S")) + '] - ' + msg + '\n')
    open(targetPath + targetFile).close()
    print('[' + str(datetime.datetime.now().strftime("%H:%M:%S")) + '] - ' + msg)

#########################################################
