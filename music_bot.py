# Importing libraries
import discord
from discord.ext import commands
import os
import asyncio
import yt_dlp as youtube_dl
import time
from discord import *

# Discord bot Initialization
version = 1.1
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='.', intents=intents)
key = "Your Bot Token"
voice_clients = {}
yt_dl_opts = {'format': 'bestaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)
ffmpeg_options = {'options': "-vn"}


#ClientEvent
@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")


    #Commands
#1 - play
@client.command(name='play', help='Plays your YT video from URL')
async def play(ctx, *, msg):
    try:
        voice_client = await ctx.author.voice.channel.connect()
        voice_clients[voice_client.guild.id] = voice_client
    except:
        await ctx.send("Can't connect to Voice Channel!")
        print("Can't connect to Voice Channel!")

    try:
        url = msg
        loop = asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))
        song = data['url']
        player = discord.FFmpegPCMAudio(song, **ffmpeg_options)
        voice_clients[ctx.guild.id].play(player)

        await ctx.send(f'Playing from source: {msg}')
    except Exception as err:
        print(err)


#2 - pause
@client.command(name='pause', help='Pause playing music')
async def pause(ctx):
    await ctx.send('Paused')
    try:
        voice_clients[ctx.guild.id].pause()
    except Exception as err:
        print(err)


#3 - resume
@client.command(name='resume', help='Resume playing music')
async def resume(ctx):
    await ctx.send('Resumed')
    try:
        voice_clients[ctx.guild.id].resume()
    except Exception as err:
        print(err)


#4 - stop
@client.command(name='stop', help='Stop playing music and leave VC')
async def stop(ctx):
    await ctx.send('Stopped and left Voice Channel')
    try:
        voice_clients[ctx.guild.id].stop()
        await voice_clients[ctx.guild.id].disconnect()
    except Exception as err:
        print(err)
client.run(key)
