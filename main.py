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

 
    cpu =  ("""

             
            ```py


            ```


         """)


    if message.content.startswith('!cpu'):
    	await message.channel.send(cpu)

    gpu = ("""
           ```py



           ```
	
	    """)

    if message.content.startswith('!gpu'):
    	await message.channel.send(gpu)

client.run('token')
