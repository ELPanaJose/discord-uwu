import discord 
from discord.ext import commands

bot = commands.Bot(command_prefix='*', description="Test bot")

@bot.command()
async def ping(ctx):
	await ctx.send('pong')

# Event
@bot.event
async def on_ready():
   await bot.change_presence(activity=discord.Streaming(name="monda", url="https://twitch.tv/monda"))
   print('bruh')

bot.run('')
