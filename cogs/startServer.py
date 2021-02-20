import discord
from discord.ext import commands, tasks
import os
import psutil
import asyncio

client = commands.Bot(command_prefix = '>')

class startServer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.filepath = 'E:\\steamcmd\\ARK\\ShooterGame\\Binaries\\Win64\\ARK Serverstart Island.bat'
        self.serverStatus = 'Down'

    async def bootServer(self):
        os.startfile(self.filepath)


    @commands.Cog.listener()
    async def on_ready(self):
        print('startServer cog loaded.')

    @client.command()
    async def startServer(self, ctx, *arg):
        #To get the emoji in unicode, type \<:emoji:> in Discord, and copy the result.
        print('Starting server via command sent from Discord!')
        await ctx.message.channel.send('Let\'s see...')
        serverTest = "ShooterGameServer.exe" in (p.name() for p in psutil.process_iter())
        print('First serverTest: ' + str(serverTest))
        if serverTest == True:
            await ctx.message.add_reaction('❌')
            await ctx.message.channel.send('Nope, I can\'t do that! The gate is already open!')
            return
        await startServer.bootServer(self)
        await asyncio.sleep(5)
        serverTest = "ShooterGameServer.exe" in (p.name() for p in psutil.process_iter())
        print('Second serverTest: ' + str(serverTest))
        if serverTest == True:
            await ctx.message.add_reaction('✅')
            await ctx.message.channel.send('Everything looks good! I will open the gate. Please stand back, this may take a while...')
            #Prepares to send a message back to the sender notifying them that the server is up.
            while self.serverStatus != 'Up':
                print('Waiting for server to finish booting...')
                await asyncio.sleep(30)
        # Gives a mention to the user that sent the command if they also included anything else in the command.
        if arg:
            await ctx.message.channel.send('I\'ve finished opening the gate, 'ctx.message.author.mention + '. All who wish to head on through may do so.')
        else:
            await ctx.message.channel.send('Okay, we should be good now. Gate is open, for all who wish to head on through.')


def setup(bot):
    bot.add_cog(startServer(bot))

