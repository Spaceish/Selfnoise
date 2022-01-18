import discord
from discord.ext import commands
import os
from sp import slowprint as sp

token = os.getenv('token')

prefix = os.getenv('prefix')

selfnoise = commands.Bot(command_prefix=prefix, self_bot=True)

@selfnoise.event
async def on_ready():
    sp('Logged in as')
    sp(selfnoise.user.name)
    sp(selfnoise.user.id)
    sp('[------] Made by SpaceDot. [------]')
    # change status to "Toate ca toate"
    await selfnoise.change_presence(game=discord.Game(name='Toate ca toate')) 

selfnoise.run(token, bot = False)
