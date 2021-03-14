import discord
from discord.ext import commands
import sys
import os

token = os.getenv('token')

prefix = os.getenv('prefix')

selfnoise = commands.Bot(command_prefix=prefix)
