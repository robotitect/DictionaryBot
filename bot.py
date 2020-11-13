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

def create_embed(word, definition):
    to_return = discord.Embed(title = word)

    for word_type in definition:
        # print(word_type)
        for given_def in definition[word_type]:
            # print(given_def)
            to_return.add_field(name = word_type, value = given_def, inline = False)

    return to_return

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
            # await message.channel.send(definition)
            await message.channel.send(embed = create_embed(word, definition))
        else:
            await message.channel.send(
                f'{word}: definition not found'
            )


client.run(TOKEN)