import discord
import os
from discord.ext import commands
import asyncio
import datetime
import logging
import redis
from time import gmtime, strftime


logging.basicConfig(level=logging.INFO)

client = commands.Bot(command_prefix ='.')
client.remove_command('help')

extensions = ['cogs.ban', 'cogs.CommandEvents', 'cogs.kickcmd', 'cogs.clear',
'cogs.ran', 'cogs.avatar', 'cogs.userinfo','cogs.errors', 'cogs.mute',
'cogs.Commands','cogs.help', 'cogs.delete']





if __name__== '__main__':
    for ext in extensions:
        client.load_extension(ext)







@client.command()
async def ping(ctx):
        await ctx.send(f'Pong? haha, ok latency is {round(client.latency * 1000)}ms')






client.run('NzA3MDQ0MzQ1Mjk5MjA2MTQ0.XrIdAA.G5gkms1vzu61aypDLqa-KjI_dhU')
