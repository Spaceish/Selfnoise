import discord
from discord.ext import commands
import os

token = os.getenv('token')

prefix = os.getenv('prefix')

selfnoise = commands.Bot(command_prefix=prefix, self_bot=True)

@selfnoise.event
async def on_ready():
    print('Logged in as')
    print(selfnoise.user.name)
    print(selfnoise.user.id)
    print('[------]')
    # change status to "Toate ca toate"
    await selfnoise.change_presence(game=discord.Game(name='Toate ca toate')) 

selfnoise.run(token)
