# import lines
import time
import datetime
import os
import discord
#rcon to be able to determine server and player status
from rcon import Client
## etc.

# Init

# A place to dump variables that may change easily in the future.
class var_dump():
    log_path = os.path(D://steamcmd//ARK//ShooterGame//Saved//Logs//ShooterGame.log
    ipaddr = 0.0.0.0
    port = 0000
    passwd = 0000

class timer(): 
      
    # init method/constructor 
    def __init__(self): 
        self.sec = 0 
          
    # time check function every 30s
    def tick_check(self): 
        time.sleep(1)
        self.sec += 1
        if self.sec % 30 == 0:
          players_online = player_count()
          server_status_check()
          server_inactive = server_has_been_empty_checker(players_online)
        if self.sec % 300 == 0 and server_inactive == True:
          after_hours_shutdown()
       
# Management function
def puppet_master():
  master = timer() #initializes the timer object
  
  #temporary infinite loop since no run duration has been specified yet
  while(1):
    master.tick_check()
  

## playerCount function
def player_count():
   with Client(var_dump.ipaddr, var_dump.port, passwd=var_dump.passwd) as client:
     players_online = client.run('listplayers')
     if players_online == 'No Players Connected':
       player_count = 0
     else player_count = len(players_online)
     return(player_count)

                       
                       
                       
  # Commented the following out as it won't actually work for ARK, but will likely be usable for other servers going forward.                     
###def player_count():
  ###re_pattern = re.compile('(joined|left) this ARK!')
  ###join_left = re_pattern.findall(p.read_text(.//logs//ShooterGame.log))
  ###player_joined = join_left.count('joined')
  ###player_left = join_left.count('left')
  ###player_count = player_joined - player_left

## Server status checker function
### Future: Convert this to check for ShooterGameServer.exe and nothing in the log yet for a "Going up" state?
#def server_status_check:

## ServerHasBeenEmpty Checker function - Need to talk about how organization should happen with this one (how much of the function should be in timer?)
#def serverHasBeenEmpty():
#  serverHasBeenEmpty = True
   

## Server Starter function

## Server Terminator function

## After-Hours Shutdown function
def after_hours_shutdown():
  if datetime.datetime.now().hour >= 22 or if datetime.datetime.now().hour <= 6:
     os.system("TASKKILL /F /IM 'ShooterGameServer.exe'")
     time.sleep(10)
     os.system("shutdown /s /t 1)
# Discord-related functions:
## Mood Updater function
## Command Receiver function
