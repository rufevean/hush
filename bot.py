#importing all the requried stuff
import discord
import json
from discord.ext import commands
import asyncio
from datetime import datetime ,time, timedelta
#giving a prefix to the bot and creating it
bot = commands.Bot(command_prefix="*", intents=discord.Intents.all())
#giving a time to send the message
noTime = datetime.now()
with open('token.json') as f:
    data = json.load(f)
    token = data["token"] # reads the token from another file
#for logs
@bot.event
async def on_ready():
    print("the bot is ready") #for our logs to check if the bot is started
    if noTime.hour==20:#checks if the time is 7 pm and then proceds to send a text file
       channel = bot.get_channel(1038026099797528646) #grabbing the test channel
       await channel.send("hello")

if __name__ == "__main__":
    bot.run(token) #starting the bot