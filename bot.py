import discord
from datetime import datetime
hush = discord.Client(intents=discord.Intents.default())
noTime = datetime.now()
time = noTime.hour
@hush.event
async def on_ready():
    print("the bot is ready")

@hush.event
async def on_message(message):
    if message.content.startswith('$time'):
        await message.channel.send(time)

@hush.event
async def on_message(message):
    if message.content.startswith('$hello'):
        await message.channel.send("hello world")

hush.run('MTAzODAyNTI2ODQyNzc2MzcxMg.GyQt9b.XI5gwYf4492OoVIuJGtpaL8WSnHntkRN5R6_oo')