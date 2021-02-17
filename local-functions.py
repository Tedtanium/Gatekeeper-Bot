# import lines -- time helps create a timer, datetime allows us to pick out what hour it is gracefully, os allows for filesystem management and execution/killing of programs, discord allows for bot, psutil allows for scanning existing running processes, and rcon allows remote console into a server.
import time
import datetime
import os
import psutil
from rcon import Client

# A place to dump variables that may change easily in the future or should be initialized with 0.
class local_var_dump():
    inactivity_time = 0
      


## playerCount function
def server_status_check(ipaddr, port, passwod):
  # Instigates connection to RCON and tries to get a playercount; if this fails the server is still starting.
    try:
        with Client(ipaddr, port, passwd=passwod) as client:
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
def after_hours_shutdown(start_hour, end_hour):
    if end_hour <= datetime.datetime.now().time() <= start_hour:
        os.system("shutdown /s /t 1")
    else:
        return('The time is ' + str(datetime.datetime.now().time()) + '. It\'s not time to shut down yet!')
                      
                       
                       
                       
  # Commented the following out as it won't actually work for ARK, but will likely be usable for other servers going forward.                     
###def player_count():
  ###re_pattern = re.compile('(joined|left) this ARK!')
  ###join_left = re_pattern.findall(p.read_text(.//logs//ShooterGame.log))
  ###player_joined = join_left.count('joined')
  ###player_left = join_left.count('left')
  ###player_count = player_joined - player_left
