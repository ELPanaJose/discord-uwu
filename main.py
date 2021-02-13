import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('peo'):
        await message.channel.send('mujer que veo mujer que morboseo :smiling_imp:')

    if message.content.startswith('chill'):
        await message.channel.send('chill')

    emojis = (':neutral_face: @everyone :neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face:')
    gifs = ('https://tenor.com/view/neutral-face-neutralface-kyska-kusja-gif-20128160 https://tenor.com/view/neutral-face-emoji-weirdchamp-weirdchamping-gif-18614570')
    
    if message.content.startswith('!raid' , print('the raid begin')):
         while True:
             await message.channel.send(emojis)
             await message.channel.send(gifs)


    if message.content.startswith('!sr'):
          exit(print("raid over"))

    neofetch = ("""
           ```py
                                   u0_a138@localhost
          +hydNNNNdyh+             -----------------
        +mMMMMMMMMMMMMm+           OS: Android 9 armv7l
      dMMm:NMMMMMMN:mMMd           Host: motorola moto e6 play
      hMMMMMMMMMMMMMMMMMMh         Kernel: 4.4.146+
  ..  yyyyyyyyyyyyyyyyyyyy  ..     Uptime: 26 days, 18 hours, 5
.mMMmMMMMMMMMMMMMMMMMMMMMmMMm.     Packages: 133 (dpkg), 1 (pkg
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:   Shell: bash 5.1.4
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:   CPU: MT6739WW (4) @ 1.495GHz
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:   Memory: 1164MiB / 1862MiB
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
-MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM-
 +yy+ MMMMMMMMMMMMMMMMMMMM +yy+
      mMMMMMMMMMMMMMMMMMMm
      /++MMMMh++hMMMM++/
          MMMMo  oMMMM
          MMMMo  oMMMM
          oNMm-  -mMNs
          
                       ```
	    """)

    if message.content.startswith('!neofetch'):
    	await message.channel.send(neofetch)




         
client.run('')
