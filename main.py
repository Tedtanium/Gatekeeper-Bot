# import lines
import time
import os
import discord
## etc.

# Init

# Modules:
## Timer/Puppeteer Module
####def timer():
 #### sec = 0
 #### time.sleep(1)
 #### sec += 1
  ##### Runs these modules every 30 seconds.
  ####if sec % 30 == 0:
  ####  playerCount()
  ####  serverStatusChecker()
  ####  serverHasBeenEmptyChecker()
  ##### Runs this every 5 minutes.
 #### if sec % 300 == 0:
   #### afterHoursShutdown()

class timer(): 
      
    # init method/constructor 
    def __init__(self): 
        self.sec = 0 
          
    # time check function every 30s
    def tickCheck(self): 
        time.sleep(1)
        self.sec += 1

def puppetMaster():
  for i in -1:
    timer.tickCheck():
    if timer.tickCheck % 30 == 0:
      playerCount()
      serverStatusChecker()
      serverHasBeenEmptyChecker()
   if timer.tickCheck % 300 == 0:
      afterHoursShutdown()

  

## playerCount Module
def playerCount():
  rePattern = re.compile('(joined|left) this ARK!')
  joinLeft = rePattern.findall(p.read_text(.//logs//ShooterGame.log))
  playerJoined = joinLeft.count('joined')
  playerLeft = joinLeft.count('left')
  playerCount = playerJoined - playerLeft
  # Recurrence/timers?

## serverStatus Checker Module
## serverHasBeenEmpty Checker Module
###def serverHasBeenEmpty():
###  serverHasBeenEmpty = True

## Server Starter Module

## Server Terminator Module

## After-Hours Shutdown Module

# Discord-related Modules:
## Mood Updater Module
## Command Receiver Module
