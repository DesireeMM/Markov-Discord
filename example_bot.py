# This example requires the 'message_content' intent.

import discord
import os
DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
import markov

text = markov.open_and_read_file('green-eggs.txt')
chains = markov.make_chains(text)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send(chains)

client.run(DISCORD_TOKEN)