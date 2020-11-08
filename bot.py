# bot.py
import os
import random

import discord
from dotenv import load_dotenv
from PyDictionary import PyDictionary

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

dictionary = PyDictionary()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('def'):
        word = message.content.split(' ')[1]
        definition = dictionary.meaning(word)
        print(definition)
        print(type(definition))

        if (definition):
            await message.channel.send(definition)
        else:
            await message.channel.send(
                f'{word}: definition not found'
            )


client.run(TOKEN)