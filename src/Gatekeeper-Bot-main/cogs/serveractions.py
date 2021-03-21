import discord
from discord.ext import commands, tasks
import os
import asyncio
import sys
import datetime
import ../management as mgmt

client = commands.Bot(command_prefix = '>')

class ServerActions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.filepath = 'C:\\steamcmd\\ARK\\ShooterGame\\Binaries\\Win64\\ARK Serverstart Island.bat'


    @commands.Cog.listener()
    async def on_ready(self):
        await mgmt.logger(self, 'Server Actions cog loaded.')

    @client.command()
    async def startServer(self, ctx, *arg):
        # Restricts bot usage to specific channels. Second one is test channel!
        if ctx.message.channel.id == 813498747803402251 or ctx.message.channel.id == 811405916418867232: 
            await ctx.message.channel.send('Let\'s see...')
            #Tests to see if the server's already up; if it is it won't try to run another instance of it.
            serverTest = await mgmt.serverTest(self)
            if serverTest == True:
                await ctx.message.add_reaction('❌')
                await ctx.message.channel.send('Nope, I can\'t do that! The gate is already open!')
                return        
            await mgmt.logger(self, 'Starting server via command sent from user ' + str(ctx.message.author) + '!')
            await mgmt.bootServer(self, self.filepath)
            await ctx.message.add_reaction('✅')
            mgmt.serverStatus = 'Starting'
            await asyncio.sleep(5)
            serverTest = await mgmt.serverTest(self)
            if serverTest == True:
                await ctx.message.channel.send('Everything looks good! I will open the gate. Please stand back, this may take a while...')
                # Loop that lasts until the server is fully up or is down.
                while mgmt.serverStatus != 'Up':
                    await asyncio.sleep(10)
            # Gives a mention to the user that sent the command if they also included anything else in the command.
            if arg:
                await ctx.message.channel.send('I\'ve finished opening the gate, ' + ctx.message.author.mention + '. All who wish to head on through may do so.')
            else:
                await ctx.message.channel.send('Okay, we should be good now. Gate is open, for all who wish to head on through.')
        return
        
            
    @client.command()
    async def stopServer(self, ctx):
        if ctx.message.channel.id == 813498747803402251 or ctx.message.channel.id == 811405916418867232:
            serverTest = await mgmt.serverTest(self)
            if serverTest == True:
                await ctx.message.channel.send('Got it! Lowering the gate.')
                await mgmt.terminateServer()
                await asyncio.sleep(5)
                serverTest = await mgmt.serverTest(self)
                await ctx.message.add_reaction('💾')
                if serverTest == False:
                    await mgmt.logger(self, 'Server successfully closed via command from user ' + str(ctx.message.author) + '!')
                    await ctx.message.add_reaction('🛑')
                else:
                    await ctx.message.channel.send('The gate...didn\'t close. Something\'s wrong.')
                    await ctx.message.add_reaction('❌')
            else:
                await ctx.message.channel.send('I can\'t do that. The gate is already closed!')
                await ctx.message.add_reaction('❌')
        return

    @client.command()
    async def saveWorld(self, ctx):
        if ctx.message.channel.id == 813498747803402251 or ctx.message.channel.id == 811405916418867232:
            serverTest = await mgmt.serverTest(self)
            if serverTest == True:
                # Manual saves can only be made once per hour.
                if mgmt.lastSave == datetime.datetime.now().hour:
                    await ctx.message.channel.send('It\'s been too soon since the last save! I can\'t do that!')
                    await ctx.message.add_reaction('❌')
                    return
                else:
                    await mgmt.serverStatusCheck(self, 'saveworld')
                    await mgmt.logger(self, str(ctx.message.author) + ' instigated a manual save!')
                    await ctx.message.add_reaction('💾')
                    await ctx.message.channel.send('Okay! The save is complete.')
                    # Establishes hour cooldown.                    
                    mgmt.lastSave = datetime.datetime.now().hour

def setup(bot):
    bot.add_cog(ServerActions(bot))

