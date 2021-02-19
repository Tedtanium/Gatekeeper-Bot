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

    async def bootServer(self):
        os.startfile(self.filepath)


    @commands.Cog.listener()
    async def on_ready(self):
        print('startServer cog loaded.')

    @client.command()
    async def startServer(self, ctx):
        #To get the emoji in unicode, type \<:emoji:> in Discord, and copy the result.
        print('Starting server via command sent from Discord!')
        serverTest = "ShooterGameServer.exe" in (p.name() for p in psutil.process_iter())
        print('First serverTest: ' + str(serverTest))
        if serverTest == True:
            await ctx.message.add_reaction('❌')
            await ctx.message.channel.send('I can\'t do that! It\'s already running!')
            return
        await startServer.bootServer(self)
        await asyncio.sleep(5)
        serverTest = "ShooterGameServer.exe" in (p.name() for p in psutil.process_iter())
        print('Second serverTest: ' + str(serverTest))
        if serverTest == True:
            await ctx.message.add_reaction('✅')
            await ctx.message.channel.send('Server is starting! Please stand back, this may take a while...')
            #if 
            #ctx.message.channel.send(ctx.message.author.mention() + '! The gates are open and ready to accept visitors.')


        # if statement -> if server is up, responds back @ing the person who said this
                #asyncio.wait_for(management.server_status == 'Up', None) ?
                    #await message.channel.send('Okay, we should be good now, ')    


def setup(bot):
    bot.add_cog(startServer(bot))

