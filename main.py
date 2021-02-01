# import lines
import time
import os
import discord
## etc.

# Init
class timer(): 
      
    # init method/constructor 
    def __init__(self): 
        self.sec = 0 
          
    # time check function every 30s
    def tickCheck(self): 
        time.sleep(1)
        self.sec += 1
        if self.sec % 30 == 0:
          playerCount()
          serverStatusChecker()
          serverHasBeenEmptyChecker()
        if self.sec % 300 == 0:
          afterHoursShutdown()
       
# Management function
def puppetMaster():
  master = timer() #initializes the timer object
  
  #temporary infinite loop since no run duration has been specified yet
  while(1):
    master.tickCheck()
  

## playerCount function
def playerCount():
  rePattern = re.compile('(joined|left) this ARK!')
  joinLeft = rePattern.findall(p.read_text(.//logs//ShooterGame.log))
  playerJoined = joinLeft.count('joined')
  playerLeft = joinLeft.count('left')
  playerCount = playerJoined - playerLeft

## serverStatus Checker function
## serverHasBeenEmpty Checker function
###def serverHasBeenEmpty():
###  serverHasBeenEmpty = True

## Server Starter function

## Server Terminator function

## After-Hours Shutdown function

# Discord-related functions:
## Mood Updater function
## Command Receiver function
