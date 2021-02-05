# import lines
import time
import os
import discord
## etc.

# Init

# A place to dump variables that may change easily in the future.
class var_dump():
    log_path = os.path(D://steamcmd//ARK//ShooterGame//Saved//Logs//ShooterGame.log

class timer(): 
      
    # init method/constructor 
    def __init__(self): 
        self.sec = 0 
          
    # time check function every 30s
    def tickCheck(self): 
        time.sleep(1)
        self.sec += 1
        if self.sec % 30 == 0:
          player_count()
          server_status_check()
          server_has_been_empty_checker()
        if self.sec % 300 == 0:
          after_hours_shutdown()
       
# Management function
def puppet_master():
  master = timer() #initializes the timer object
  
  #temporary infinite loop since no run duration has been specified yet
  while(1):
    master.tick_check()
  

## playerCount function
def player_count():
  re_pattern = re.compile('(joined|left) this ARK!')
  join_left = re_pattern.findall(p.read_text(.//logs//ShooterGame.log))
  player_joined = join_left.count('joined')
  player_left = join_left.count('left')
  player_count = player_joined - player_left

## Server status checker function
### Future: Convert this to check for ShooterGameServer.exe and nothing in the log yet for a "Going up" state?
#def server_status_check:

## ServerHasBeenEmpty Checker function
###def serverHasBeenEmpty():
###  serverHasBeenEmpty = True

## Server Starter function

## Server Terminator function

## After-Hours Shutdown function

# Discord-related functions:
## Mood Updater function
## Command Receiver function
