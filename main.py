import discord
import os
from largeC import *
    
client = discord.Client()

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!chill'):
         await message.channel.send('chill {0.author}'.format(message))

    emojis = ('@everyone')
    gif = ('https://media.discordapp.net/attachments/807053711871443024/809997406677630996/neutral_face.png?width=458&height=458')

    if message.content.startswith('!raid', print(chr(27)+"[1;33m"+"the raid begin")):
        while True:
            await message.channel.send(emojis)
            await message.channel.send(gif)

    if message.content.startswith('!ayuda'):
        await message.channel.send(ayuda)

    if message.content.startswith('!sr'):
        exit(print("raid over"))

    if message.content.startswith('!neofetch'):
        await message.channel.send(neofetch)

    if message.content.startswith('!SETSMS'):
        os.system("cd SETSMS ; bash SETSMS.sh")
        await message.channel.send("esta en SETSMS!")

    if message.content.startswith('!atack'):
        await message.channel.send(f"se ataco a : ||{numero}|| se demora unos 3-4 minutos")

    if message.content.startswith('test'):
        await message.channel.send(numero)
        os.write(f"{numero}")

client.run('')
