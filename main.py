# import lines -- time helps create a timer, datetime allows us to pick out what hour it is gracefully, os allows for filesystem management and execution/killing of programs, discord allows for bot, psutil allows for scanning existing running processes, and rcon allows remote console into a server.
import time
import datetime
import os
import discord
import psutil
from rcon import Client

# Init

# A place to dump variables that may change easily in the future.
class var_dump():
    ipaddr = '0.0.0.0'
    port = 0000
    passwd = '0000'
    inactivity_time = 0
    start_hour = datetime.time(6)
    end_hour = datetime.time(22)
      
    # init method/constructor 
def __init__(self): 
    self.sec = 0 
    self.inactivity_time = 0
                       
          
    # time check function every 30s
def tick_check(self): 
    time.sleep(1)
    self.sec += 1
    if self.sec % 30 == 0 and "ShooterGameServer.exe" in (p.name() for p in psutil.process_iter()) == True:
      server_status, players_online = server_status_check()
      server_inactivity_checker(players_online)
    if self.sec % 600 == 0 and "ShooterGameServer.exe" in (p.name() for p in psutil.process_iter()) == False:
      after_hours_shutdown()
       
# Management function
def puppet_master():
  master = timer() #initializes the timer object
  
  #temporary infinite loop since no run duration has been specified yet
  while(1):
    master.tick_check()
  

## playerCount function
def server_status_check():
  # Instigates connection to RCON and tries to get a playercount; if this fails the server is still starting.
    try:
        with Client(var_dump.ipaddr, var_dump.port, passwd=var_dump.passwd) as client:
            players_online = client.run('listplayers')
        server_status = 'Up'
        if 'No Players Connected' in players_online:
            player_count = 0
       # Fairly certain this output is stored as a list. If not, we can probably make it one...
        else: 
            player_count = (players_online).count('\n')
    except:
        # If this is running and gives an error, the server is still going up. The player_count variable is dummied out for this instance.
        server_status = 'Starting'
        player_count = -1
    return(server_status, player_count)

# Server inactivity checker - This will close the server two hours after everyone has logged out.
def server_inactivity_checker(players_online):
    if players_online == 0:
        var_dump.inactivity_time += 30
    else:
        var_dump.inactivity_time = 0
    if var_dump.inactivity_time >= 7200:
        print(datetime.datetime.now().time() + '- Server has been inactive for two hours! Shutting it down...')
        sleep(3)
    return(var_dump.inactivity_time)
    # Disabled until ready. server_terminator()

## Server Starter function

## Server Terminator function

## After-Hours Shutdown function - This is running on the assumption that it's a 24h clock and not a 12h, which is untested at this time.
def after_hours_shutdown():
    if var_dump.end_hour <= datetime.datetime.now().time() <= var_dump.start_hour:
        os.system("shutdown /s /t 1")
    else:
        return('The time is ' + str(datetime.datetime.now().time()) + '. It\'s not time to shut down yet!')
                       
# Discord-related functions:

## Mood Updater function

## Command Receiver function

                       
# Keys in the ignition!                       
puppet_master()                       

                       
                       
                       
  # Commented the following out as it won't actually work for ARK, but will likely be usable for other servers going forward.                     
###def player_count():
  ###re_pattern = re.compile('(joined|left) this ARK!')
  ###join_left = re_pattern.findall(p.read_text(.//logs//ShooterGame.log))
  ###player_joined = join_left.count('joined')
  ###player_left = join_left.count('left')
  ###player_count = player_joined - player_left
