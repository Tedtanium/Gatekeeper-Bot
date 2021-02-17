import os
import discord
import time
import management

client = discord.Client()
bot_token = 'whywouldIputthisherewhereeveryonecouldseeit?'
start_server_cmd = '>>>>'
stop_server_cmd = '>>>>'


@client.event
async def on_ready():
    print('Successfully logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if discord.utils.find(lambda Ga: Ga.name == 'Gatekeeper', message.author.roles):
        if message.content.startswith(start_server_cmd):
            #To get the emoji in unicode, type \<:emoji:> in Discord, and copy the result.
            print('Starting server via command sent from Discord!')
            #start_server()
            await.asyncio.sleep(1)
            #if "ShooterGameServer.exe" in (p.name() for p in psutil.process_iter()) == True:
            await message.add_reaction('👍')
            await message.add_reaction('⬆️')
            await message.channel.send('Server is starting! Please stand back, this may take a while...')
            # if statement -> if server is up, responds back @ing the person who said this
                    #asyncio.wait_for(management.server_status == 'Up', None) ?
                        #await message.channel.send('Okay, we should be good now, ') 
            print(message.author.roles)

    if discord.utils.find(lambda Ga: Ga.name == 'Gatekeeper', message.author.roles):
        if message.content.startswith(stop_server_cmd):
            
            await message.add_reaction('👍')
            await message.add_reaction('🛑')
            await message.channel.send('Successfully got stop command!')
            #react
            #stop_server()

client.run(bot_token)

# Debug tool section.
# Sends a message in channel.
#await message.channel.send('Hello!')
