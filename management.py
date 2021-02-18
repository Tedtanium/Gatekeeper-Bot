import bot_functions
import local_functions
import time
import datetime
import os
import discord
import psutil
import asyncio
from rcon import Client



#Initialization and dump of malleable variables.
class var_dump():
    ipaddr = '0.0.0.0'
    port = 0000
    passwod = '0000'
    start_hour = datetime.time(6)
    end_hour = datetime.time(22)
    seconds = 0 
    to = 0
    

#Executes things on a clock!
async def tick_check():
    print('tick_check has started!')
    while(var_dump.to != 1):
        await asyncio.sleep(1)
        var_dump.seconds += 1
        print('Checking to see if ARK Server is going up...')
        if var_dump.seconds % 30 == 0 and "ShooterGameServer.exe" in (p.name() for p in psutil.process_iter()) == True:
            server_status, players_online = local-functions.server_status_check(var_dump.ipaddr, var_dump.port, var_dump.passwod)
            local-functions.server_inactivity_checker(players_online)
        if var_dump.seconds % 600 == 0 and "ShooterGameServer.exe" in (p.name() for p in psutil.process_iter()) == False:
            local-functions.after_hours_shutdown(var_dump.start_hour, var_dump.end_hour)
        var_dump.to += 1
      
      
      
# Management function
# Currently broken; the only thing that ends up running is bot_functions.client.run.
async def puppet_master():
    print('HELLO?!')
    await tick_check() 
    await bot_functions.client.run(bot_functions.bot_token)

# Keys in the ignition!
asyncio.run(puppet_master(), debug=true)
