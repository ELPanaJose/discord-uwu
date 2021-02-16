import discord 
from discord.ext import commands

bot = commands.Bot(command_prefix='*', description="Test bot")
# Event
@bot.event
async def on_ready():
   await bot.change_presence(activity=discord.Streaming(name="elpanajose.ga", url="https://twitch.tv/monda"))
   print("\033[4;35m"+"twitch status succesfully added")

bot.run('')	
