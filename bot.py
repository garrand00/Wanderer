from dotenv import load_dotenv
import os
import asyncio
import discord
from discord.ext import commands

load_dotenv()

token = os.getenv('BOT_TOKEN')
extentions = []
# Loading Cogs
for filename in os.listdir('.\cogs'):
    if filename.endswith('.py'):
        extentions.append(f'cogs.{filename[:-3]}')


activity = discord.Activity(name="Don't tell Minstrel!", type=discord.ActivityType.playing)
client = commands.Bot(command_prefix=";;", intents=discord.Intents.all(), activity=activity)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

async def load():
    for extension in extentions:
        await client.load_extension(extension)

async def main():
    async with client:
        await load()
        await client.start(token)

asyncio.run(main())