#importing all the requried stuff
import discord
from discord.ext import commands
import asyncio
from datetime import datetime ,time, timedelta
#giving a prefix to the bot and creating it
hush = commands.Bot(command_prefix="*",intents=discord.Intents.default())
#giving a time to send the message
noTime = datetime.now()
time = noTime.hour
channel_id = 1038026099797528646
#for logs
@hush.event
async def on_ready():
    print("the bot is ready")

# async def on_ready():
#     # await bot.wait_until_ready()
#     channel = bot.get_channel(channel_id)
#     await channel.send("good day eh?")


@hush.event
async def on_message(message):
    if message.content.startswith('$time'):
        await message.channel.send(time)

@hush.event
async def on_message(message):
    if message.content == 'hello':
        await message.channel.send('hello world')
if __name__ == "__main__":
    hush.run('MTAzODAyNTI2ODQyNzc2MzcxMg.GOs6Lz.uBqZcK6hVF6r6Y4aFOVmj-Up-F9joA6ltqePqY')