import discord
from discord.ext import commands, tasks
import os
import psutil
import asyncio


client = commands.Bot(command_prefix = '>')

class stopServer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        #local variables needed initialized here.


    @commands.Cog.listener()
    async def on_ready(self):
        print('stopServer cog loaded.')

    async def terminateServer():
            os.system('TASKKILL /IM ' + 'ShooterGameServer.exe')


    @client.command()
    async def stopServer(self, ctx):
        await ctx.message.channel.send('Got it! Lowering the gates now...')
        await stopServer.terminateServer()
        await asyncio.sleep(5)
        serverTest = "ShooterGameServer.exe" in (p.name() for p in psutil.process_iter())
        if serverTest == False:
            print('Server successfully closed via command.')
            await ctx.message.add_reaction('🛑')
        else:
            await ctx.message.channel.send('The gate...didn\'t close. Something\'s wrong.')



def setup(bot):
    bot.add_cog(stopServer(bot))
