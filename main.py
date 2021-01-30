# import lines
import time
import os
import discord
## etc.

# Modules:
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
