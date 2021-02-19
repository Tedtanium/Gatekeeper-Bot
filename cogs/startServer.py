import discord
from discord.ext import commands, tasks
import os


class startServer(commands.Cog):
    def __init__(self, bot)
        self.bot = bot
        
    def setup(bot):
        client.add_cog(startServer(bot))
    
    #@client.command()
    #async def startServer(ctx):
        ##To get the emoji in unicode, type \<:emoji:> in Discord, and copy the result.
        #print('Starting server via command sent from Discord!')
        #serverTest = "ShooterGameServer.exe" in (p.name() for p in psutil.process_iter())
        #print('First serverTest: ' + str(serverTest))
        #if serverTest == True:
            #await ctx.message.add_reaction('❌')
            #await ctx.message.channel.send('I can\'t do that! It\'s already running!')
            #return
        #await Ticker.startServer()
        #await asyncio.sleep(5)
        #serverTest = "ShooterGameServer.exe" in (p.name() for p in psutil.process_iter())
        #print('Second serverTest: ' + str(serverTest))
        #if serverTest == True:
            #await ctx.message.add_reaction('✅')
            #await ctx.message.channel.send('Server is starting! Please stand back, this may take a while...')
            #if 
            #ctx.message.channel.send(ctx.message.author.mention() + '! The gates are open and ready to accept visitors.')


        # if statement -> if server is up, responds back @ing the person who said this
                #asyncio.wait_for(management.server_status == 'Up', None) ?
                    #await message.channel.send('Okay, we should be good now, ')    
