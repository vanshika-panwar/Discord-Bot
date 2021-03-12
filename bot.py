import os
import random
import requests
import discord
import asyncio 
from discord.ext import commands    
from discord.ext.commands import Bot
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
# bot = commands.Bot(command_prefix='!')
# @bot.command(name='create-channel')

# @commands.has_role('admin')
# async def create_channel(ctx, channel_name='real-python'):
#     guild = ctx.guild
#     existing_channel = discord.utils.get(guild.channels, name=channel_name)
#     if not existing_channel:
#         print(f'Creating a new channel: {channel_name}')
#         await guild.create_text_channel(channel_name)

# @bot.event

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]
starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    msg = message.content

    if message.author == client.user:
        return
    await message.channel.send('Handling msgs')

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$delete'):
        #  await message.delete()
        async for msg in message.channel.history(limit=2):
           await msg.delete()

    if message.content.startswith('$clear'):
      tmp = await message.channel.send( 'Clearing messages...')
      async for msg in message.channel.history(limit=200):
           await msg.delete()

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


client.run(TOKEN)
