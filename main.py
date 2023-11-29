import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import ffmpeg

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all()) 

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
    return 

@bot.command(name="start")
async def start(ctx):
    """Adds two numbers together."""
    await ctx.send("Let's play the game 🎶")
    return 

@bot.command(name="song")
async def song(ctx):
    """Provides a song snippet"""
    if ctx.author.voice is None:
        await ctx.send("You're not in a voice channel!")
        return

    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
        await voice_channel.connect() #connect to channel
    else:
        await ctx.voice_client.move_to(voice_channel)

    # Play the song snippet here (example with a local file)
    ctx.voice_client.play(discord.FFmpegPCMAudio(source='indianajones.mp3'))


    return 

bot.run(TOKEN)