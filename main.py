import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

"""@client.command()
async def createChannel(ctx, channelName):
	guild = ctx.guild

	mbed = d.Embed(
         title = 'succes',
         description = "{} channel created".format(channelName)
		)
if ctx.author.guild_permissions.manage_channels:
	await guild.create_text_channel(name = {}.format(channelName))
	await ctx.send(embed*mbed)"""
 
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('peo'):
        await message.channel.send('mujer que veo mujer que morboseo :smiling_imp:')

    if message.content.startswith('chill'):
        await message.channel.send('chill')

    #emojis = (':neutral_face: @everyone :neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face::neutral_face:')
    emojis = ('@everyone')
    gif = ('https://media.discordapp.net/attachments/807053711871443024/809997406677630996/neutral_face.png?width=458&height=458')
    
    if message.content.startswith('!raid' , print('the raid begin')):
         while True:
             await message.channel.send(emojis)
             await message.channel.send(gif)
          


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

    if message.content.startswith('SETSMS'):
    	test = os.system("cd SETSMS ; bash SETSMS.sh")
    	await message.channel.send("")

    if message.content.startswith('!atack'):
    	await message.channel.send("se hizo el ataque se demora unos 3-4 min", numero)

client.run('')
