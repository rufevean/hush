#importing all the requried stuff
import discord
from discord.ext import commands
import asyncio
from datetime import datetime ,time, timedelta
#giving a prefix to the bot and creating it
bot = commands.Bot(command_prefix="*", intents=discord.Intents.all())
#giving a time to send the message
noTime = datetime.now()
token  = open("token.txt", "r").read()
# time = noTime.hour
channel_id = 1038026099797528646
#for logs
@bot.event
async def on_ready():
    print("the bot is ready") #for our logs to check if the bot is started


@bot.event
async def on_message(message):
    if message.author.bot: #doesnt reply to bots
        return
    message1 = "*time"
    message2 = "*hello"
    if message.content == message1: #checks if the message is message1
        await message.reply("wait") #replies with wait
    elif message.content == message2: #checks if the message is message2
        await message.reply("hello bot") #rplies with the hello bot
if __name__ == "__main__":
    bot.run(token) #starting the bot