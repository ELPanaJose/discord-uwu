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

                pai@pai-hplaptop14cm0xxx 
                ------------------------ 
                OS: Ubuntu 20.04.2 LTS x86_64 
                Host: HP Laptop 14-cm0xxx 
                Kernel: 5.4.0-65-generic 
                Uptime: 12 hours, 28 mins 
                Packages: 2474 (dpkg), 17 (snap) 
                Shell: zsh 5.8 
                Resolution: 1366x768 
                DE: GNOME 
                WM: Mutter 
                WM Theme: Adwaita 
                Theme: Yaru-ark [GTK2/3] 
                Icons: BigSur-black [GTK2/3] 
                Terminal Font: Roboto Mono for Powerline Bold Italic 14 
                CPU: AMD A6-9225 RADEON R4 2C+3G (2) @ 2.600GHz 
                GPU: AMD ATI Radeon R2/R3/R4/R5 Graphics 
                Memory: 2955MiB / 3817MiB 
          
                                                                  
                           ```
	    """)

    if message.content.startswith('!neofetch'):
    	await message.channel.send(neofetch)




         
client.run('')
