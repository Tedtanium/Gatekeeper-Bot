import discord
from discord.ext import commands, tasks
import os
import psutil
import asyncio
from rcon import Client


client = commands.Bot(command_prefix = '>')

class statusCheck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        #local variables needed initialized here.


    @commands.Cog.listener()
    async def on_ready(self):
        print('statusCheck cog loaded.')

    async def serverStatusCheck(self, ipaddr, port, passwod):
  # Instigates connection to RCON and tries to get a playercount; if this fails the server is still starting.
        try:
            with Client(ipaddr, port, passwd=passwod) as client:
                playersOnline = client.run('listplayers')
            serverStatus = 'Up'
            if 'No Players Connected' in playersOnline:
                playerCount = 0
            else: 
                playerCount = (playersOnline).count('\n')
        except:
        # If this is running and gives an error, the server is still going up. The player_count variable is dummied out for this instance.
            serverStatus = 'Starting'
            playerCount = -1
        return(serverStatus, playerCount)

def setup(bot):
    bot.add_cog(statusCheck(bot))



