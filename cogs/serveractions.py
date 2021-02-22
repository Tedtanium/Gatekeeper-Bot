import discord
from discord.ext import commands, tasks
import os
import psutil
import asyncio
import sys
import datetime
#from Gatekeeper-Bot-main.gatekeeper import management as mgmt
sys.path.append('E:/Scripts/Gatekeeper-Bot-main/gatekeeper')
import management as mgmt

client = commands.Bot(command_prefix = '>')

class ServerActions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.filepath = 'E:\\steamcmd\\ARK\\ShooterGame\\Binaries\\Win64\\ARK Serverstart Island.bat'
        self.serverStatus = 'Down'


    @commands.Cog.listener()
    async def on_ready(self):
        print('Server Actions cog loaded.')

    @client.command()
    async def startServer(self, ctx, *arg):
        await ctx.message.channel.send('Let\'s see...')
        #Tests to see if the server's already up; if it is it won't try to run another instance of it.
        serverTest = await mgmt.Management.serverTest(self)
        if serverTest == True:
            await ctx.message.add_reaction('❌')
            await ctx.message.channel.send('Nope, I can\'t do that! The gate is already open!')
            return        
        print(str(datetime.datetime.now().time()) + ' - Starting server via command sent from Discord!')
        await mgmt.Management.bootServer(self, self.filepath)
        await ctx.message.add_reaction('✅')
        self.serverStatus = 'Down'
        await asyncio.sleep(5)
        serverTest = await mgmt.Management.serverTest(self)
        if serverTest == True:
            await ctx.message.channel.send('Everything looks good! I will open the gate. Please stand back, this may take a while...')
            # Infinite loop that lasts until the server is fully up.
            while self.serverStatus != 'Up':
                await asyncio.sleep(10)
        # Gives a mention to the user that sent the command if they also included anything else in the command.
        if arg:
            await ctx.message.channel.send('I\'ve finished opening the gate, ' + ctx.message.author.mention + '. All who wish to head on through may do so.')
        else:
            await ctx.message.channel.send('Okay, we should be good now. Gate is open, for all who wish to head on through.')
            
    @client.command()
    async def stopServer(self, ctx):
        serverTest = await mgmt.Management.serverTest(self)
        # Future: Logic to make sure startServer isn't actively bringing the server up already.
        if serverTest == True:
            await ctx.message.channel.send('Got it! Lowering the gates.')
            await mgmt.Management.terminateServer()
            await asyncio.sleep(5)
            serverTest = await mgmt.Management.serverTest(self)
            if serverTest == False:
                print('Server successfully closed via command.')
                await ctx.message.add_reaction('🛑')
            else:
                await ctx.message.channel.send('The gate...didn\'t close. Something\'s wrong.')
        else:
            await ctx.message.channel.send('I can\'t do that. The gate is already closed!')


def setup(bot):
    bot.add_cog(ServerActions(bot))

