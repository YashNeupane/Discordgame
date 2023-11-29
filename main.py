import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from fuzzywuzzy import fuzz
import ffmpeg

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all()) 

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command(name="song")
async def song(ctx):
    """Provides a song snippet"""
    if ctx.author.voice is None:
        await ctx.send("You're not in a voice channel!")
        return

    ctx.voice_client.play(discord.FFmpegPCMAudio(source='indianajones.mp3'))

@bot.command(name="start")
async def start(ctx):
    if ctx.author.voice is None:
        await ctx.send("You're not in a voice channel!")
        return

    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
        await voice_channel.connect() #connect to channel
    else:
        await ctx.voice_client.move_to(voice_channel)

    #joining the channel
    await ctx.send("Let's play the game 🎶")

    return 


@bot.command(name='guess')
async def guess(ctx, *, guess: str):
    correct_title = "Indiana Jones"  # The actual title of the song

    similarity_score = fuzz.ratio(guess.lower(), correct_title.lower())

    if similarity_score >= 70:  # You can adjust this threshold
        await ctx.send(f"Correct! 🎉 You got {similarity_score}% of the title right.")
    else:
        await ctx.send(f"Sorry, that's not correct. 😢 You got {similarity_score}% of the title right.")


bot.run(TOKEN)