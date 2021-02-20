import discord
from discord.ext import commands, tasks
import os
import psutil
import asyncio


client = commands.Bot(command_prefix = '>')


class MoodUpdater(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        #local variables needed initialized here.


    @commands.Cog.listener()
    async def on_ready(self):
        print('moodUpdater cog loaded.')

    async def statusUpdate(self, ctx, serverStatus):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Server | Status: " + serverStatus))


def setup(bot):
    bot.add_cog(moodUpdater(bot))
