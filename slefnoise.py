import discord
from discord.ext import commands
from sp import slowprint as sp

token = "ODU1NzQ1OTU0ODAzNDgyNjM1.YeRMTA"+".zYUpDrseNR2C8k8SyPzK3JuaeZw"

prefix = ".-."

selfnoise = commands.Bot(command_prefix=prefix, self_bot=True)

@selfnoise.event
async def on_ready():
    sp('Logged in as ->')
    sp(selfnoise.user.name)
    sp(selfnoise.user.id)
    sp('[------] Made by SpaceDot. [------] (btw -../.-/.-./../..-/... e gei lll)')
    # change status to "Toate ca toate"
    await selfnoise.change_presence(activity=discord.Game(name="Toate ca toate"))

@selfnoise.command()
async def ping(ctx):
    # replies with pong
    # and pong's latency
    await ctx.reply(f"Pong! {round(selfnoise.latency * 1000)}ms") 

# avatar command
@selfnoise.command()
async def avatar(ctx, member: discord.Member):
    # replies with member's avatar
    await ctx.reply(member.avatar_url)

selfnoise.run(token, bot=False)