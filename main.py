# import lines
import time
import os
import discord
## etc.

# Init
sec = 0
serverHasBeenEmptyChecker.serverHasBeenEmpty = True

# Modules:
## Timer/Puppeteer Module
def timer():
  time.sleep(1)
  sec += 1
  # Runs these modules every 30 seconds.
  if sec % 30 == 0:
    playerCount()
    serverStatusChecker()
    serverHasBeenEmptyChecker()
  # Runs this every 5 minutes.
  if sec % 300 == 0:
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
## Server Starter Module
## Server Terminator Module
## After-Hours Shutdown Module

# Discord-related Modules:
## Mood Updater Module
## Command Receiver Module
