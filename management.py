import bot-functions
import local-functions
import time
import datetime
import os
import discord
import psutil
from rcon import Client



#Initialization and dump of variables.
class var_dump():
    ipaddr = '0.0.0.0'
    port = 0000
    passwod = '0000'
    start_hour = datetime.time(6)
    end_hour = datetime.time(22)
    seconds = 0 
    

#Executes things on a clock!
def tick_check(): 
    while(1):
        time.sleep(1)
        var_dump.seconds += 1
        if var_dump.seconds % 30 == 0 and "ShooterGameServer.exe" in (p.name() for p in psutil.process_iter()) == True:
            server_status, players_online = local-functions.server_status_check(var_dump.ipaddr, var_dump.port, var_dump.passwod)
            local-functions.server_inactivity_checker(players_online)
        if var_dump.seconds % 600 == 0 and "ShooterGameServer.exe" in (p.name() for p in psutil.process_iter()) == False:
            local-functions.after_hours_shutdown(var_dump.start_hour, var_dump.end_hour)
      
      
      
# Management function
def puppet_master():
    while(1):
        tick_check() 

# Keys in the ignition!
puppet_master()
