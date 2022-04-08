import os
import random
import sys
from time import sleep
from discord.ext import commands
from discord.ext import tasks

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print("Logged in as", bot.user)
    send_message.start()


@tasks.loop(seconds=20, count=10)
async def send_message():
    mudae = bot.get_channel(int(os.getenv('CHANNEL_ID_MUDAE')))
    owo = bot.get_channel(int(os.getenv('CHANNEL_ID_OWO')))
    meme = bot.get_channel(int(os.getenv('CHANNEL_ID_MEME')))

    await mudae.send("$w")
    sleep(2)
    await owo.send("owo hunt")
    sleep(2)
    await meme.send("pls meme")


@send_message.before_loop
async def before_send_message():
    await bot.wait_until_ready()
    if sys.argv[1] == "daily":
        await send_message_daily()


@send_message.after_loop
async def after_send_message():
    owo = bot.get_channel(int(os.getenv('CHANNEL_ID_OWO')))
    await owo.send("owo slot 10")
    sleep(2)
    await owo.send("owo cf 10 {}".format(random.choice(["head", "tail"])))
    sleep(2)
    await owo.send("owo inv")
    sleep(2)
    await owo.send("owo cowoncy")
    print("All job done")


async def send_message_daily():
    owo = bot.get_channel(int(os.getenv('CHANNEL_ID_OWO')))
    await owo.send("owo daily")
    sleep(2)
    await owo.send("owo lb")
    sleep(2)
    await owo.send("owo crate")
