import os
import random
import sys
from time import sleep
from discord.ext import commands
from discord.ext import tasks

bot = commands.Bot(command_prefix='boogabotlala', self_bot=True)


@bot.event
async def on_ready():
    print("Logged in as", bot.user)
    send_message_mudae.start()


@tasks.loop(minutes=1, count=10)
async def send_message_mudae():
    mudae = bot.get_channel(int(os.getenv('TEST_CHANNEL_ID_MUDAE')))
    await mudae.send("$w")


@tasks.loop(minutes=1, count=10)
async def send_message_meme():
    meme = bot.get_channel(int(os.getenv('CHANNEL_ID_MEME')))
    await meme.send("pls meme")


@tasks.loop(minutes=1, count=10)
async def send_message_owo():
    owo = bot.get_channel(int(os.getenv('TEST_CHANNEL_ID_OWO')))
    await owo.send("owo hunt")


@send_message_mudae.before_loop
async def before_send_message_mudae():
    await bot.wait_until_ready()


@send_message_mudae.after_loop
async def after_send_message_mudae():
    send_message_meme.start()


@send_message_meme.after_loop
async def after_send_message_meme():
    send_message_owo.start()


@send_message_owo.after_loop
async def after_send_message_owo_three():
    owo = bot.get_channel(int(os.getenv('TEST_CHANNEL_ID_OWO')))
    if len(sys.argv) == 2:
        if sys.argv[1] == "daily":
            await owo.send("owo daily")
            sleep(60)
            await owo.send("owo lb all")
            sleep(60)
            await owo.send("owo crate")
            sleep(60)
    await owo.send("owo slot 100")
    sleep(60)
    await owo.send("owo cf 100 {}".format(random.choice(["head", "tail"])))
    sleep(60)
    await owo.send("owo inv")
    sleep(60)
    await owo.send("owo cowoncy")
    print("All job done")
    sys.exit()
