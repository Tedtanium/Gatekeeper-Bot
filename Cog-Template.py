#This can be used to make new cogs! The bare bones, in addition to a debug message confirming it's loaded, is below.

import discord
from discord.ext import commands, tasks
import os
import psutil
import asyncio


client = commands.Bot(command_prefix = '>')

class <className>(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        #local variables needed initialized here.


    @commands.Cog.listener()
    async def on_ready(self):
        print('<className> cog loaded.')



def setup(bot):
    bot.add_cog(<className>(bot))