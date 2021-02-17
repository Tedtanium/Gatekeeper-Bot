import bot-start
import main
import time
import datetime
import os
import discord
import psutil
from rcon import Client



#Initialization of variables.
class var_dump():
    ipaddr = '0.0.0.0'
    port = 0000
    passwd = '0000'
    inactivity_time = 0
    start_hour = datetime.time(6)
    end_hour = datetime.time(22)
    seconds = 0 
    

#Executes things on a clock!
def tick_check(): 
    while(1):
        time.sleep(1)
        var_dump.seconds += 1
        if var_dump.seconds % 30 == 0 and "ShooterGameServer.exe" in (p.name() for p in psutil.process_iter()) == True:
            server_status, players_online = main.server_status_check()
            main.server_inactivity_checker(players_online)
        if var_dump.seconds % 600 == 0 and "ShooterGameServer.exe" in (p.name() for p in psutil.process_iter()) == False:
            main.after_hours_shutdown()
      
      
      
# Management function
def puppet_master():
    while(1):
        tick_check() 

# Keys in the ignition!
puppet_master()
