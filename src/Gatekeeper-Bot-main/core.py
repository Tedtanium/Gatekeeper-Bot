import os
import discord
from discord.ext import commands, tasks
import asyncio



client = commands.Bot(command_prefix = '>')
bot_token = 'Nzk2NDI1OTcyNjAxNDU0NjUz.X_XvfA.0WJkxCYn43pXMPhjyYk5mVH0kao'



@client.event
async def on_ready():
    print('Successfully logged in as {0.user}'.format(client))
    

    
class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



######### Loads all cogs in cogs subfolder so long as they end in .py, cutting off the file extension. ######
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
client.run(bot_token)
