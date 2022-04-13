import os
import random
import sys
from time import sleep
from discord.ext import commands
from discord.ext import tasks
from dotenv import load_dotenv, find_dotenv, set_key

load_dotenv()
bot = commands.Bot(command_prefix='boogabotlala', self_bot=True)
id_channel_mudae = int(os.getenv('CHANNEL_ID_MUDAE'))
id_channel_meme = int(os.getenv('CHANNEL_ID_MEME'))
id_channel_owo = int(os.getenv('CHANNEL_ID_OWO'))
id_bot_owo = int(os.getenv('BOT_OWO_ID'))


@bot.event
async def on_ready():
    print("Logged in as", bot.user)
    send_message_mudae.start()


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if not message.guild and message.author.id == id_bot_owo:
        send_message_owo.cancel()
        dotenv_file = find_dotenv()
        set_key(dotenv_file, "OWO_STATUS", "BANNED")
        print("cancel task job send owo message, please verify manually")
        sys.exit()


@tasks.loop(minutes=1, count=10)
async def send_message_mudae():
    mudae = bot.get_channel(id_channel_mudae)
    await mudae.send("$w")


@tasks.loop(minutes=1, count=10)
async def send_message_meme():
    meme = bot.get_channel(id_channel_meme)
    await meme.send("pls meme")


@tasks.loop(minutes=1, count=10)
async def send_message_owo():
    owo = bot.get_channel(id_channel_owo)
    await owo.send("owo hunt")


@send_message_mudae.before_loop
async def before_send_message_mudae():
    await bot.wait_until_ready()


@send_message_mudae.after_loop
async def after_send_message_mudae():
    send_message_meme.start()


@send_message_meme.after_loop
async def after_send_message_meme():
    if (os.getenv('OWO_STATUS') == "CLEAR"):
        send_message_owo.start()
    else:
        print("skip owo message because status not clear, please change .env file")
        sys.exit()


@send_message_owo.after_loop
async def after_send_message_owo_three():
    owo = bot.get_channel(id_channel_owo)
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
